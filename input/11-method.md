# Method and Material


The example adopted an engineering design study with a controlled, paired comparison of service variants. The design made the transaction policy the intended difference while keeping the event identities and retry schedule constant.

Synthetic data were selected to show how a method can be documented without exposing institutional records. This choice was suitable for a teaching document but supplied no evidence of how real users, devices or production systems behaved.

## Research Design


RQ1 was addressed by comparing the number of persisted records with the number of unique accepted event identities. RQ2 was addressed by paired run-level p95 latency summaries and a review of which failure stages could be distinguished in the trace records.

A purely demonstrative walkthrough would have shown the interface but would not have established comparative behavior. A production case study could have added environmental realism, although uncontrolled workload and configuration differences would have required a different approach to attribution.

## Reliability and Validity


For an actual execution, reliability would depend on versioned workloads, recorded configurations, stable timing boundaries and repeated runs. Reusing event IDs across variants would make paired comparisons possible, while randomized run order would reduce confounding from warm-up and resource contention.

Construct validity required counting business records rather than treating HTTP success as proof of correctness. External validity was restricted by the single-node laboratory boundary. In this document, the stronger limitation was that all observations were invented fixtures, so no empirical validity or reliability was claimed.

## Workload, Instrumentation and Analysis


The illustrative workload contained 1,000 unique valid events and 200 retransmissions of existing identities, yielding 1,200 requests. A separate conflict fixture reused an identity with a different payload; conflict cases were not mixed into the 1,200-request correctness denominator.

The latency material contained five paired run-level p95 values per variant at an illustrative arrival rate of 100 requests per second. Averaging these five summaries described run-to-run central tendency; it did not recover the pooled request-level p95. The retained CSV in Appendix A made this distinction explicit.

## Ethics and Reproduction Protocol


No participants, institutional records or production endpoints were used. Tenant IDs and event IDs were fictional, and examples contained no authentication secrets or personal attributes. No ethics approval, consent process or organizational endorsement was asserted.

A real run would record the service revision, database version, schema migration, container digest and workload seed before starting. The protocol would warm each variant, apply the identical workload, export raw measurements, and compare database invariants with the expected identity set. The commands in Appendix B illustrated that protocol and were not executed to produce the synthetic results.

