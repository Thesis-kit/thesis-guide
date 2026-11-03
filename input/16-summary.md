# Summary


The illustrative thesis considered reliable retry handling in a fictional campus event service. The starting problem was an uncertain request outcome after loss of a response: an event might already have committed even though the sender did not receive confirmation. The objective was to frame a comparison between simple insertion and a durable, tenant-scoped deduplication policy.

Two research questions organized the example. RQ1 concerned duplicate event and outbox persistence under a defined retry workload, while RQ2 concerned latency cost and diagnostic limitations. The intended contribution was a traceable framework linking identity requirements to an explicit persistence boundary and an evidence matrix, rather than the invention of a database or telemetry system.

The described method combined engineering design with a controlled paired comparison. The workload fixture represented 1,000 unique valid events and 200 retransmissions, with conflict cases specified separately. Five paired run-level p95 latency summaries and a hand-authored status trace demonstrated how material and analysis could be documented. No implementation benchmark, participant study or production deployment was conducted.

The proposed artifact associated one stored outcome with a tenant/event identity and paired the event with an outbox record inside one transaction. A matching replay returned the stored outcome, while changed content for an existing identity entered a conflict path. The short Python listing expressed an adapter contract and did not constitute an executed, concurrency-safe database implementation.

In the synthetic correctness table, the baseline contained 1,200 event rows and the protected variant contained 1,000, corresponding to 200 and zero excess rows respectively. The invented latency summaries averaged 26 milliseconds for the baseline and 30 milliseconds for the protected variant. Their mean paired difference was 4 milliseconds, about 15.4 percent of the baseline mean; this calculation was not a pooled request-level percentile.

The example trace illustrated accepted, replayed and conflicting outcomes. Its categories supplied a model for diagnostic presentation, while durable counts remained the relevant correctness observation. The evidence matrix separated these fixtures from unexecuted conflict, rollback and concurrency cases so that coverage could not be mistaken for passed tests.

The discussion answered both questions only within the constructed example. No empirical performance, production reliability, end-to-end delivery or scientific novelty was established. The conclusions emphasized matching evidence to a bounded guarantee and stated that concurrency, retention expiry and external consumption remained unresolved. The document therefore served as an annotated model of research presentation rather than a completed master research study.

