# Current State Analysis and Project Specifications


The scenario assumed that a campus sender retried an event when no response arrived within its timeout. The baseline stored every accepted submission with a new internal row identifier, even if the sender supplied an identity already encountered.

The analysis separated uncertainty about transport from uncertainty about persistence. A timeout established that a response was not observed; it did not establish that the original transaction had failed. This distinction determined which observations were needed during validation.

## Existing Workflow and Failure Modes


In the invented workflow, a room device submitted an event through an application programming interface (API). A downstream process later consumed an outbox record. Staff needed a consistent event history and enough diagnostic information to explain repeated submissions.

Three scenario failure points were considered: rejection before persistence, a database rollback, and loss of the response after commit. The third case exposed the baseline weakness because a repeated request could be processed as a second business event. These were constructed cases, not incidents observed at a university.

## Derived Requirements and Acceptance Criteria


The requirements prioritized durable identity over a memory-only cache because the example included service restarts. Identity was scoped by tenant so that unrelated organizations could use the same event label without unintentionally sharing a deduplication boundary.

Table 1 connected each scenario need to an explicit check. The acceptance criteria were design choices for this example, not universal service-level targets.

Table: Scenario requirements and acceptance criteria. {widths="1,3,3"}
| ID | Requirement | Acceptance criterion |
|---|---|---|
| R1 | Suppress repeated valid identity | One event and one outbox row per tenant/event pair |
| R2 | Detect conflicting payload | Reject changed content for an existing identity |
| R3 | Preserve atomic persistence | Event and outbox both commit or both roll back |
| R4 | Expose outcome stage | Record accepted, replayed, conflict or failed status |
| R5 | Quantify latency tradeoff | Compare five paired run-level p95 summaries |

The matrix kept diagnostic completeness separate from correctness. A useful trace could explain a failure without proving that duplicate business effects were impossible.

## Constraints and Priorities


The example allowed one PostgreSQL transaction for the event and outbox tables and required a durable key after restart. It did not assume that a remote consumer participated in that transaction, so end-to-end delivery semantics remained outside the established boundary.

Correctness was prioritized over a small increase in latency in the synthetic decision framework. Chapter 4 therefore examined identity semantics, database enforcement and observability separately, rather than treating a faster response or a richer dashboard as a substitute for persistence guarantees.

