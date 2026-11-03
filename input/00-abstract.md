---
title: Reliable Retry Handling in a Campus Event Service
subtitle: An Illustrative ICT Master Thesis
author: Matti Meikäläinen
degree_programme: Information Technology
professional_major: Software Engineering
submission_date: October 2026
language: en
degree: master
tiivistelma: true
sammanfattning: false
keywords: idempotency, distributed systems, observability, validation
advisors:
- Minna Hämäläinen (Senior Lecturer)
allow_multiple_alternative_abstracts: false
title_fi: Luotettavat uudelleenyritykset kampuksen tapahtumapalvelussa
degree_programme_fi: Tieto- ja viestintätekniikka
professional_major_fi: Ohjelmistotekniikka
keywords_fi: uudelleenyritykset, hajautetut järjestelmät, havainnoitavuus, validointi
title_sv: Tillförlitliga återförsök i en händelsetjänst
degree_programme_sv: Informationsteknik
professional_major_sv: Programvaruteknik
keywords_sv: återförsök, distribuerade system, observerbarhet, validering
---

# Abstract


Campus integrations were used as a fictional setting for studying event retries after lost responses. The example addressed the risk that a repeated request could create a second business record.

The illustrative objective was to compare a simple insertion service with a transactional deduplication design. The contribution was framed as a traceable comparison of correctness and latency under a bounded retry workload.

An engineering design study and a controlled comparison were described. Synthetic fixtures represented 1,000 unique events, 200 retries and five paired run-level latency summaries; no experiment or participant study was actually conducted.

In the synthetic example, duplicate records decreased from 200 to zero. Mean run-level p95 latency increased from 26 to 30 milliseconds, and payload conflicts were treated separately from valid retries.

The example illustrated a correctness–latency tradeoff rather than a general performance claim. Production effectiveness, external delivery guarantees and long-term behavior remained unestablished.

