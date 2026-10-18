# Exercise Graph
## Premise
Creating a "graph" of physical exercises, containing a corpus of exercises that can be inserted into a strength training programme for any given person (client). this graph is meant to help populate sets, sessions and monthly programmes for clients, given a coach's preferred session structure, based on a client's needs.

When a client tracks results for a given session, the exercise graph should also be able to recommend weights, based on the amount of energy reported by a user, their progress thus far in past sessions, and coach-set goals for progressive overload. 

At this point, i'm not sure what is needed on the client side - a "client graph" that also keeps track of a client's progress on different metrics over time, what their strong exercises are, what they should focus on, and what weights (kg) they should use next

## Definitions
1. `Coach`
    - Personal fitness trainer, who trains clients in individual or group settings
    - For each `session` (group or individual), a `programme` for the session is created.
2. `Client`
    - A trainee, in an individual or group settings
    - Attends a `session`, and works out following the `programme` created by the `coach`
3. `Session`
    - A single scheduled, timed training session involving 1 coach and 1 or many clients
4. `Programme`
    - What a `client` should do in a session, standardised to every session regardless of client
    - This can contain `circuits` of 2-5 exercisess
        - `exercises` will have a fixed number of `sets` and `reps`
        - `exercises` can be grouped into `circuit` where each exercise in a `circuit` will be repeated in a circuitous sequence for the same number of sets
    - `reps`: number of time to repeat each exercise as it is encountered
    - `sets`: number of times to complete a full quantity of reps
5. `Exercise`
    - An atomically defined physical movement, pertinent to a specific body part, with a prescribed form of completion, designed to provide a physical challenge to the client
6. `plan`
    - a sequence of `programmes` for chronologically ordered `sessions`, planned to cover a month/ quarter/ year
7. `target-client-programme-session-exercise-weights`
    - not sure what to call this, but external to the programme, is the weights that a user should use per exercise, for a given session, for each exercise into the programme
    - this is external to the programme, and is more of a user's coach-assisted/suggested weights/ weight range
    - This is set in conjunction with a user's own assessment of their capability pre-session, a coach's/ graph recommendation pre-session, which accounts for past performance, coach's goals etc. 
8. `actual-client-programme-session-exercise-weights`
    - This is the actual weights used

## Features of the exercise corpus (corpus)
To start to build an exercise graph, a corpus of exercises is maintained. it should contain a continually growing list of exercises to provide new stimulus to clients, and should not remain static

For each exercise, there needs to be a (more or less) list of standardised information maintained per exercise
- push/ pull
- part of body
- muscles worked
- single sided/ bilateral
- please recommend

## Applications of graph
Non comprehensive
Given a full corpus, the "graph" should help coaches
- suggest complementary/ contrarian exercises to add into a single `circuit`, `programme` or `plan`
- suggest reps given the `circuit`, `programme` or `plan`

Given a programme, and Given a client's record, which includes
- coach goals
- client exercise records
- client trajectory,
- influence 

suggest `target-client-programme-session-exercise-weights` to a `client` pre-session, taking into account how a client is feeling

## Application