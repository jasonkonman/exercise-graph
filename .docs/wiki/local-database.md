# Database choice and local PostgreSQL

Decision and verification date: 2026-10-18.

## Decision

Use **PostgreSQL 17 as the single authoritative application database**. Persist
the curated exercise corpus, typed graph relations, evidence claims, review
decisions, and later coach/client programme records there. Keep reviewed JSON
seeds and exports in Git where their licences permit it.

PostgreSQL runs locally in this cloud workspace. Version 17.11 was installed and
tested without root access or Docker. Docker is available, but is not required
by this workflow. No application schema or recommendation logic is implemented yet.

## Do embedded databases help?

| Tool | Where it helps | Where it complicates this project | Decision |
| --- | --- | --- | --- |
| SQLite | Single-user/offline application, a portable file, relational constraints and short graph traversals | A later multi-user service may need migration; one writer at a time; maintaining SQLite and PostgreSQL paths adds dialect, migration, and test differences | A credible alternative for an explicitly embedded product. Do not add it alongside PostgreSQL now. |
| DuckDB | Analytical SQL over large exports, CSV/Parquet ingestion, corpus audits, offline experiments | A second writable store needs synchronization and backup rules; its analytical focus does not solve application permissions or graph provenance | Defer. If needed, read immutable exports and keep outputs derived/rebuildable. |
| Chroma | Finding relevant passages or exercise descriptions by embedding similarity, with metadata filters | Model/download dependencies, chunking choices, embedding/index versions, deletions, and synchronization with reviewed records | Defer. It does not replace the authoritative claim/evidence/relationship model. |
| PostgreSQL | Transactions, foreign keys, typed relations, JSONB, recursive queries, and a multi-user application path | A server process needs startup and a retained data directory | Selected. A local helper makes the service manageable here. |

SQLite is capable of representing this POC graph; the reason to choose PostgreSQL
is the planned coach/client application and avoiding a second persistence path.
Embedded storage is simpler when it is the only store. It becomes more complicated
when several databases hold overlapping authoritative records.

For search, begin with structured filters and PostgreSQL text search. If a measured
semantic-retrieval problem emerges, evaluate pgvector before adding a separate
vector service. pgvector is an extension, not part of the current installation.
Store embedding model/version and source revision, filter against current review
permissions/status, and keep any vector index rebuildable. Retrieved similarity
must never be presented as scientific support for a training claim.

This is a workload-based design decision, not a comparative performance benchmark.
DuckDB and Chroma were not installed or benchmarked for this task.

## Local commands

Run from `/workspace/exercise-graph`:

```sh
scripts/dev-postgres.sh install
scripts/dev-postgres.sh start
scripts/dev-postgres.sh status
scripts/dev-postgres.sh psql -X -v ON_ERROR_STOP=1 -c 'SELECT current_database(), version();'
scripts/dev-postgres.sh stop
```

The installer targets the current Debian 13 environment and PostgreSQL major 17.
It downloads distribution packages through signed Debian metadata, verifies them
through APT, and extracts them into workspace storage. It does not modify system
APT sources, install system packages, disable verification, or require root.
It reuses an existing installation; it does not automatically upgrade a running
cluster. Future minor-version refreshes should be planned with a backup and the
service stopped. Major-version upgrades need an explicit migration.

The helper relies on the runtime libraries already present in this Debian image;
this is not a general-purpose portable PostgreSQL installer. On another operating
system, use native PostgreSQL 17 and the same eventual application migrations.

Defaults:

- Database: `exercise_graph`; database user: the current operating-system user.
- Retained state: `/workspace/.exercise-graph/postgres`, outside the Git checkout.
- Binaries: `runtime/usr/lib/postgresql/17/bin` under that state directory.
- Cluster data: `data/`; private socket: `socket/`; server log: `server.log`.
- Socket port identifier: `55432`. TCP listeners are disabled.
- Authentication: Unix peer authentication; socket access is owner-only. No
  application password or network secret is required for this development instance.

`EXERCISE_GRAPH_PG_ROOT` overrides the state directory and
`EXERCISE_GRAPH_PG_PORT` overrides the socket port. Keep these consistent between
commands. State paths must be absolute and use letters, digits, `.`, `_`, `-`, and
`/`; the helper rejects spaces and shell metacharacters. The default is a sibling
`.exercise-graph/postgres` directory relative to the checkout's parent.

For an eventual application, use the Unix-socket connection parameters directly:
host `/workspace/.exercise-graph/postgres/socket`, port `55432`, database
`exercise_graph`, and the current OS user. This is a development superuser, not a
production role/access-control design.

`start` initializes a new cluster only if needed, reuses a running instance, and
performs a real SQL query. A conflicting cluster major version is rejected.
`stop` stops only this helper's configured cluster. No destructive reset command
is provided. An existing cluster's configuration is not rewritten on each start.

To create and restore a custom-format development backup:

```sh
scripts/dev-postgres.sh pg_dump --format=custom --file=/tmp/exercise-graph.dump
# Restore into an empty database created for the purpose; choose its name explicitly.
scripts/dev-postgres.sh pg_restore --dbname=exercise_graph_restore --exit-on-error /tmp/exercise-graph.dump
```

The destination database in the second command must already exist. The helper also
supports `psql -d postgres -c 'CREATE DATABASE exercise_graph_restore'`.
Choose backup storage and retention appropriate to the data; `/tmp` is just an
example and is not durable backup storage.

## Checks completed

- Clean installation to a separate state directory, plus reuse of the main install.
- Cluster initialization, database creation, repeated startup, status, stop/restart.
- Transactional insert/update and rollback, JSONB filtering, a recursive three-node
  traversal, and rejection of foreign-key and self-edge check violations.
- Committed synthetic records survived a server stop/restart.
- Custom-format dump restored into a separate database; restored record count
  was asserted. Synthetic schemas and the restore database were removed afterward.
- Europe PMC returned the Currier 2023 record/abstract and open-access full-text XML
  (`PMC10579494`). A subsequent [focused science review](exercise-science-review.md)
  is now documented; independent human verification and policy approval remain pending.

These checks establish the current development instance. They do not validate an
application schema, a future task's snapshot restoration, or production deployment.
The environment draft records installation and restart instructions separately;
processes must be started again after a task/environment restart.

## Sources inspected for the comparison

- [PostgreSQL official query documentation](https://github.com/postgres/postgres/blob/65e944d92b082cc16e2265a91bab8b73934a0e74/doc/src/sgml/queries.sgml)
  and constraints/JSON documentation cited in the corpus research document.
- [DuckDB official README](https://github.com/duckdb/duckdb/blob/main/README.md):
  analytical SQL and CSV/Parquet use. No concurrency benchmark was performed.
- [SQLite official API header](https://github.com/sqlite/sqlite/blob/master/src/sqlite.h.in):
  transactions, locking/busy results, and foreign-key configuration. SQLite is a
  relational alternative, not a vector database.
- [Chroma official README](https://github.com/chroma-core/chroma/blob/main/README.md):
  document embeddings, collection IDs, metadata filters, and similarity queries.
- [pgvector official README](https://github.com/pgvector/pgvector/blob/master/README.md):
  optional vector similarity capabilities within PostgreSQL.

Upstream branch URLs above were inspected on the decision date; they can change.
No package versions of these optional tools have been selected for the project.
