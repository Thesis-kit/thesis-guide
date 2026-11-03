# Introduction


The illustrative setting was a campus integration service receiving room-access and equipment-status events. A sender could lose the response after the server had already committed an event, making the outcome uncertain from the sender’s perspective.

The engineering challenge was to distinguish a valid retransmission from a new event without silently accepting conflicting content. The thesis example investigated this challenge at the database transaction boundary rather than claiming to solve every failure mode in a distributed workflow.

## Context and Research Problem


HTTP semantics distinguish idempotent methods from operations for which automatic repetition needs additional knowledge. This distinction motivated explicit application handling of repeated event submissions rather than an assumption that every POST could be repeated safely [@http].

The fictional local gap was the absence of a documented link between retry identity, stored results and an observable audit trail. This was a scenario assumption, not a finding from interviews or a claim that the wider literature lacked retry-handling techniques. A real thesis would substantiate that gap with case evidence and a broader research review.

## Objective and Research Questions


The example objective was to design and evaluate a transaction boundary that associated one accepted event with one stored outcome. The intended deliverable was a service design with a repeatable evaluation protocol and traceable acceptance criteria.

**RQ1:** Under the specified retry workload, how did transactional deduplication affect duplicate event and outbox records compared with simple insertion? **RQ2:** What latency cost and diagnostic limitations accompanied that protection in the same controlled scenario?

## Contribution, Scope and Delimitations


The proposed teaching contribution was a requirements-to-evidence framework for evaluating retry protection, including conflicting-payload cases. PostgreSQL and OpenTelemetry were existing tools; their inclusion alone was not presented as an original research contribution.

The scenario included one service, one database and tenant-scoped event identifiers. External message delivery, real personal data, multi-region replication and long-term operational effectiveness were excluded. These boundaries kept the comparison inspectable but prevented conclusions about an entire campus integration platform.

## Method and Thesis Structure


The illustrative approach combined engineering design with a controlled comparison of two variants. Correctness criteria concerned duplicate persistence, conflict rejection and atomic event/outbox creation, while latency and trace completeness provided separate quality observations.

Chapter 2 defined the method and material, Chapter 3 derived specifications, and Chapter 4 compared the relevant technical approaches. Chapter 5 presented the illustrative artifact and synthetic evidence; Chapter 6 interpreted the questions and limitations, and Chapter 7 provided a factual summary. Appendices A–C retained example records, listings and authoring coverage.

