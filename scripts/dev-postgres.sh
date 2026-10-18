#!/usr/bin/env bash
# Workspace-local PostgreSQL for the Debian 13 cloud environment; no root required.
set -euo pipefail
umask 077

repo_root=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
state=${EXERCISE_GRAPH_PG_ROOT:-"$(dirname -- "$repo_root")/.exercise-graph/postgres"}
port=${EXERCISE_GRAPH_PG_PORT:-55432}
user=$(id -un)
[[ "$state" =~ ^/[a-zA-Z0-9._/-]+$ ]] || {
    echo 'Use an absolute PostgreSQL state path without spaces or shell metacharacters.' >&2
    exit 1
}
[[ "$port" =~ ^[0-9]{4,5}$ ]] && ((10#$port >= 1024 && 10#$port <= 65535)) || {
    echo 'EXERCISE_GRAPH_PG_PORT must be between 1024 and 65535.' >&2
    exit 1
}
runtime="$state/runtime"
bin="$runtime/usr/lib/postgresql/17/bin"
data="$state/data"
socket="$state/socket"

require_install() {
    [[ -x "$bin/postgres" ]] || {
        echo 'Run scripts/dev-postgres.sh install first.' >&2
        exit 1
    }
}

psql_local() {
    "$bin/psql" -X -v ON_ERROR_STOP=1 -h "$socket" -p "$port" -U "$user" "$@"
}

case "${1:-status}" in
    install)
        if [[ -x "$bin/postgres" ]]; then
            "$bin/postgres" --version
            exit 0
        fi
        . /etc/os-release
        [[ "$ID" == debian && "$VERSION_ID" == 13 ]] || {
            echo 'This installer targets Debian 13. Use native PostgreSQL 17 on other hosts.' >&2
            exit 1
        }
        mkdir -p "$state/apt/lists/partial" "$state/apt/cache/archives/partial" \
            "$state/packages" "$runtime"
        # Use signed Debian repositories without changing system APT configuration.
        cat > "$state/apt/sources.list" <<'EOF'
deb [signed-by=/usr/share/keyrings/debian-archive-keyring.gpg] https://deb.debian.org/debian trixie main
deb [signed-by=/usr/share/keyrings/debian-archive-keyring.gpg] https://deb.debian.org/debian-security trixie-security main
EOF
        cat > "$state/apt/apt.conf" <<EOF
Dir::Etc::parts "-";
Dir::Etc::main "-";
Dir::Etc::sourcelist "$state/apt/sources.list";
Dir::Etc::sourceparts "-";
Dir::State::lists "$state/apt/lists";
Dir::Cache "$state/apt/cache";
APT::Sandbox::User "$user";
APT::Update::Error-Mode "any";
Acquire::Retries "2";
EOF
        APT_CONFIG="$state/apt/apt.conf" /usr/bin/apt-get update
        (
            cd "$state/packages"
            APT_CONFIG="$state/apt/apt.conf" /usr/bin/apt-get download \
                postgresql-17 postgresql-client-17 libpq5
            for package in ./*.deb; do
                dpkg-deb -x "$package" "$runtime"
            done
        )
        "$bin/postgres" --version
        "$bin/psql" --version
        ;;
    start)
        require_install
        mkdir -p "$socket"
        chmod 700 "$socket"
        if [[ ! -f "$data/PG_VERSION" ]]; then
            "$bin/initdb" -D "$data" -L "$runtime/usr/share/postgresql/17" \
                --username="$user" --auth-local=peer --auth-host=reject \
                --encoding=UTF8 --locale=C.UTF-8
            cat >> "$data/postgresql.conf" <<'EOF'

# Development instance: private Unix socket only, authenticated by OS identity.
listen_addresses = ''
unix_socket_permissions = 0700
EOF
        fi
        [[ "$(cat "$data/PG_VERSION")" == 17 ]] || {
            echo 'Existing cluster is not PostgreSQL 17; refusing to modify it.' >&2
            exit 1
        }
        if ! "$bin/pg_ctl" -D "$data" status >/dev/null 2>&1; then
            "$bin/pg_ctl" -D "$data" -l "$state/server.log" \
                -o "-k $socket -p $port" -w -t 30 start
        fi
        if [[ "$(psql_local -d postgres -Atc "SELECT count(*) FROM pg_database WHERE datname = 'exercise_graph'")" == 0 ]]; then
            "$bin/createdb" -h "$socket" -p "$port" -U "$user" exercise_graph
        fi
        psql_local -d exercise_graph -c 'SELECT current_database(), version();'
        ;;
    stop)
        require_install
        if "$bin/pg_ctl" -D "$data" status >/dev/null 2>&1; then
            "$bin/pg_ctl" -D "$data" -m fast -w -t 30 stop
        fi
        ;;
    status)
        require_install
        "$bin/pg_ctl" -D "$data" status
        psql_local -d exercise_graph -c 'SELECT current_database(), version();'
        ;;
    psql|pg_dump|pg_restore)
        require_install
        command=$1
        shift
        exec "$bin/$command" -h "$socket" -p "$port" -U "$user" \
            -d exercise_graph "$@"
        ;;
    *)
        echo 'Usage: scripts/dev-postgres.sh {install|start|stop|status|psql|pg_dump|pg_restore} [arguments]' >&2
        exit 2
        ;;
esac
