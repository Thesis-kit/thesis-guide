# Appendix A. Synthetic Data and Test Specifications


Chapter 5 referred to this appendix for the run-level latency values and detailed test cases. The CSV values could reproduce the example arithmetic, while the test inventory specified what a real implementation would need to check.

## Run-Level Latency Fixture


The retained file contained one row per illustrative run, with paired p95 latency values in milliseconds. Its five pairs were identical to the values in Chapter 5 and Figure 4.

The mean of the baseline column was 26 and the mean of the protected column was 30. These column means summarized five run-level percentiles; request-level distributions were not retained because no requests were measured.

```text caption="Synthetic paired summaries retained as CSV." source="assets/synthetic-runs.csv"
run,baseline_p95_ms,protected_p95_ms
1,22,25
2,24,27
3,25,29
4,27,31
5,32,38
```

## Extended Test Inventory


The inventory varied failure condition and tenant fixture across twelve groups. Six scenarios per group created 72 specification rows, deliberately exercising multi-page table rendering.

Every row remained not executed. Repetition across groups illustrated how a test inventory could preserve explicit identifiers without manufacturing passing outcomes.

Table: Detailed specification inventory; every case is unexecuted. {widths="1,1,3,2"}
| Case | Need | Scenario | Status |
|---|---|---|---|
| T01-1 | R1 | Tenant fixture 1: Same identity, same digest | Not executed |
| T01-2 | R2 | Tenant fixture 1: Same identity, changed digest | Not executed |
| T01-3 | R1 | Tenant fixture 1: Same event ID, different tenant | Not executed |
| T01-4 | R3 | Tenant fixture 1: Rollback before outbox insert | Not executed |
| T01-5 | R3 | Tenant fixture 1: Concurrent identical insertions | Not executed |
| T01-6 | R4 | Tenant fixture 1: Response lost after commit | Not executed |
| T02-1 | R1 | Tenant fixture 2: Same identity, same digest | Not executed |
| T02-2 | R2 | Tenant fixture 2: Same identity, changed digest | Not executed |
| T02-3 | R1 | Tenant fixture 2: Same event ID, different tenant | Not executed |
| T02-4 | R3 | Tenant fixture 2: Rollback before outbox insert | Not executed |
| T02-5 | R3 | Tenant fixture 2: Concurrent identical insertions | Not executed |
| T02-6 | R4 | Tenant fixture 2: Response lost after commit | Not executed |
| T03-1 | R1 | Tenant fixture 3: Same identity, same digest | Not executed |
| T03-2 | R2 | Tenant fixture 3: Same identity, changed digest | Not executed |
| T03-3 | R1 | Tenant fixture 3: Same event ID, different tenant | Not executed |
| T03-4 | R3 | Tenant fixture 3: Rollback before outbox insert | Not executed |
| T03-5 | R3 | Tenant fixture 3: Concurrent identical insertions | Not executed |
| T03-6 | R4 | Tenant fixture 3: Response lost after commit | Not executed |
| T04-1 | R1 | Tenant fixture 4: Same identity, same digest | Not executed |
| T04-2 | R2 | Tenant fixture 4: Same identity, changed digest | Not executed |
| T04-3 | R1 | Tenant fixture 4: Same event ID, different tenant | Not executed |
| T04-4 | R3 | Tenant fixture 4: Rollback before outbox insert | Not executed |
| T04-5 | R3 | Tenant fixture 4: Concurrent identical insertions | Not executed |
| T04-6 | R4 | Tenant fixture 4: Response lost after commit | Not executed |
| T05-1 | R1 | Tenant fixture 5: Same identity, same digest | Not executed |
| T05-2 | R2 | Tenant fixture 5: Same identity, changed digest | Not executed |
| T05-3 | R1 | Tenant fixture 5: Same event ID, different tenant | Not executed |
| T05-4 | R3 | Tenant fixture 5: Rollback before outbox insert | Not executed |
| T05-5 | R3 | Tenant fixture 5: Concurrent identical insertions | Not executed |
| T05-6 | R4 | Tenant fixture 5: Response lost after commit | Not executed |
| T06-1 | R1 | Tenant fixture 6: Same identity, same digest | Not executed |
| T06-2 | R2 | Tenant fixture 6: Same identity, changed digest | Not executed |
| T06-3 | R1 | Tenant fixture 6: Same event ID, different tenant | Not executed |
| T06-4 | R3 | Tenant fixture 6: Rollback before outbox insert | Not executed |
| T06-5 | R3 | Tenant fixture 6: Concurrent identical insertions | Not executed |
| T06-6 | R4 | Tenant fixture 6: Response lost after commit | Not executed |
| T07-1 | R1 | Tenant fixture 7: Same identity, same digest | Not executed |
| T07-2 | R2 | Tenant fixture 7: Same identity, changed digest | Not executed |
| T07-3 | R1 | Tenant fixture 7: Same event ID, different tenant | Not executed |
| T07-4 | R3 | Tenant fixture 7: Rollback before outbox insert | Not executed |
| T07-5 | R3 | Tenant fixture 7: Concurrent identical insertions | Not executed |
| T07-6 | R4 | Tenant fixture 7: Response lost after commit | Not executed |
| T08-1 | R1 | Tenant fixture 8: Same identity, same digest | Not executed |
| T08-2 | R2 | Tenant fixture 8: Same identity, changed digest | Not executed |
| T08-3 | R1 | Tenant fixture 8: Same event ID, different tenant | Not executed |
| T08-4 | R3 | Tenant fixture 8: Rollback before outbox insert | Not executed |
| T08-5 | R3 | Tenant fixture 8: Concurrent identical insertions | Not executed |
| T08-6 | R4 | Tenant fixture 8: Response lost after commit | Not executed |
| T09-1 | R1 | Tenant fixture 9: Same identity, same digest | Not executed |
| T09-2 | R2 | Tenant fixture 9: Same identity, changed digest | Not executed |
| T09-3 | R1 | Tenant fixture 9: Same event ID, different tenant | Not executed |
| T09-4 | R3 | Tenant fixture 9: Rollback before outbox insert | Not executed |
| T09-5 | R3 | Tenant fixture 9: Concurrent identical insertions | Not executed |
| T09-6 | R4 | Tenant fixture 9: Response lost after commit | Not executed |
| T10-1 | R1 | Tenant fixture 10: Same identity, same digest | Not executed |
| T10-2 | R2 | Tenant fixture 10: Same identity, changed digest | Not executed |
| T10-3 | R1 | Tenant fixture 10: Same event ID, different tenant | Not executed |
| T10-4 | R3 | Tenant fixture 10: Rollback before outbox insert | Not executed |
| T10-5 | R3 | Tenant fixture 10: Concurrent identical insertions | Not executed |
| T10-6 | R4 | Tenant fixture 10: Response lost after commit | Not executed |
| T11-1 | R1 | Tenant fixture 11: Same identity, same digest | Not executed |
| T11-2 | R2 | Tenant fixture 11: Same identity, changed digest | Not executed |
| T11-3 | R1 | Tenant fixture 11: Same event ID, different tenant | Not executed |
| T11-4 | R3 | Tenant fixture 11: Rollback before outbox insert | Not executed |
| T11-5 | R3 | Tenant fixture 11: Concurrent identical insertions | Not executed |
| T11-6 | R4 | Tenant fixture 11: Response lost after commit | Not executed |
| T12-1 | R1 | Tenant fixture 12: Same identity, same digest | Not executed |
| T12-2 | R2 | Tenant fixture 12: Same identity, changed digest | Not executed |
| T12-3 | R1 | Tenant fixture 12: Same event ID, different tenant | Not executed |
| T12-4 | R3 | Tenant fixture 12: Rollback before outbox insert | Not executed |
| T12-5 | R3 | Tenant fixture 12: Concurrent identical insertions | Not executed |
| T12-6 | R4 | Tenant fixture 12: Response lost after commit | Not executed |

The table was a specification artifact. Its length and number of cases did not establish coverage of all failure modes or successful system behavior.
