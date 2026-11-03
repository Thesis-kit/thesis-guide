# Theoretical Background


The conceptual framework separated request semantics, persistence constraints and diagnostic visibility. These categories matched the HTTP, database and telemetry documentation used as technical anchors [@http] [@postgres] [@otel].

The comparison asked which mechanism addressed which requirement and where each mechanism stopped. This was the example author’s analytical organization, not a claim that three documentation pages constituted a complete state-of-the-art review.

## Retry Semantics and Application Identity


RFC 9110 defined idempotency by the intended effect of repeated identical requests. It also distinguished repeatable methods from operations whose safe repetition required additional knowledge, which justified an explicit retry policy for the example POST interface [@http].

The application policy used a tenant/event pair and a payload digest, rather than transport connection identity. This was a design inference for the scenario: the same event could arrive through a new connection, while a reused ID with changed content represented a conflict rather than a valid retransmission.

## Durable Constraints and Transaction Boundaries


PostgreSQL unique constraints restricted repeated values in a column or group of columns. Its documentation described automatic unique-index creation and the significance of null handling, motivating non-null identity fields in the illustrative schema [@postgres].

A memory-only cache offered a different boundary: it could avoid a lookup during one process lifetime but did not itself establish restart-safe uniqueness. The example therefore compared the cache as an alternative rather than presenting it as equivalent to a durable database constraint.

## Observability and Diagnostic Evidence


OpenTelemetry described traces, metrics and logs as distinct signals for observing system activity. These categories supported the example’s separation of request path, latency summaries and event-status records [@otel].

The design interpretation was that correlation could help identify whether a retry reached persistence, while table invariants remained the correctness evidence. A complete trace was not proof that a remote downstream effect occurred only once, and a missing trace was not proof that persistence failed.

## Synthesis and Design Rationale


Table 2 compared three options against the scenario requirements. The comparison was qualitative and concerned the specified failure model; it did not rank database products or benchmark alternative architectures.

A durable identity constraint plus atomic event/outbox persistence was selected for the example because it directly exposed the R1–R3 invariants. Telemetry remained complementary evidence for R4, while R5 required an explicit latency comparison.

Table: Analytical comparison within the fictional scenario. {widths="2,2,2,2"}
| Criterion | Simple insertion | Process-local cache | Durable key + transaction |
|---|---|---|---|
| Repeated identity | New row | May replay while cached | Database-enforced boundary |
| Process restart | No retained protection | Cache state lost | Key retained |
| Payload conflict | Not distinguished | Additional logic needed | Explicit digest comparison |
| Remote delivery | Not established | Not established | Not established |

None of these options alone established the behavior of an external consumer. The selected design was therefore evaluated for local persistence, not described as a universal exactly-once delivery solution.

