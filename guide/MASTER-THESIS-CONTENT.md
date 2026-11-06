# Writing Your Master’s Thesis: Structure and Content

Use this guide to plan, write and review your master’s thesis. It explains the purpose of each section and how to connect your research questions, methods, evidence and conclusions. The structure follows the sample manuscript in this repository; agree any changes with your supervisor and follow your programme’s current requirements.

For file organisation and Markdown syntax, use [Writing Chapters](CHAPTERS.md). For citations, use [References and Citations](REFERENCES.md). Fill in your thesis details and abstract language settings using [Abstracts and Metadata](ABSTRACT-METADATA.md).

## 1. What makes the work a master’s thesis?

A master’s thesis investigates a precise research problem or engineering challenge, explains why existing knowledge or practice is insufficient, applies a justified research approach, and produces a contribution supported by systematic evidence.

Your thesis should demonstrate:

- Comprehensive research depth and critical thinking.
- A rigorously justified problem supported by relevant literature.
- Critical analysis of the state of the art, including comparisons and gaps.
- A named, justified research design with reproducible procedures.
- A significant, well-argued contribution to knowledge or practice.
- Systematic validation and honest assessment of reliability, validity, and limitations.

A completed application or successful demonstration alone does not establish these qualities. Explain what was learned, how the evidence supports that learning, and the conditions under which the conclusions hold. Research quality depends on the argument and evidence, not on reaching a particular page count. Confirm any length requirements with your programme.

## 2. The four questions that must run through the whole thesis

| Question | Required answer | Main locations |
|---|---|---|
| **Problem** | What precise problem is investigated, for whom, and in what setting? | Introduction; Current State Analysis / Specifications |
| **Why** | Why does it persist, and what do existing research or approaches fail to address? | Introduction; Current State Analysis; Theoretical Background |
| **How** | What justified approach was used to investigate or address it? | Method and Material; Results and Analysis |
| **Validation** | What evidence shows the approach’s correctness, usefulness, or limits? | Method and Material; Results; Discussion and Conclusions |

These four framing questions are not a substitute for the thesis’s own research questions.

## 3. Complete document structure

| Order | Section | Role in this manuscript structure |
|---|---|---|
| — | Title page | Required |
| — | Preface / acknowledgements | Optional |
| — | Abstract | Required |
| — | Table of Contents | Required |
| — | List of Abbreviations | When applicable |
| 1 | Introduction | Required |
| 2 | Method and Material | Required |
| 3 | Current State Analysis / Project Specifications | Required; select the appropriate approach |
| 4 | Theoretical Background | Required |
| 5 | Results and Analysis | Required |
| 6 | Discussions and Conclusions | Required |
| 7 | Summary | Required |
| — | References | Required; unnumbered |
| — | Appendices | When applicable |

Chapters 3 and 4 may exchange places when theory is needed before the current-state analysis; explain the order and agree it with your supervisor. Personalise chapter titles to your topic while preserving their functions. Cover both discussion and conclusions within Chapter 6, with clear subsections where helpful.

### Title page

Fill in the metadata at the beginning of `input/00-abstract.md`; the PDF pipeline generates the title page. Your title should describe the investigated subject and scope clearly and, where possible, indicate the contribution rather than naming only a broad technology. See [Abstracts and Metadata](ABSTRACT-METADATA.md) for the fields.

### Preface / acknowledgements

Use this optional section for acknowledgements and personal context. A more personal tone is appropriate here; keep the main research chapters formal and evidence-based.

### Abstract

Provide a standalone account on **one page maximum**, with identifiable components in plain running text:

1. Background and why the topic matters.
2. Objective and research purpose.
3. Specific research design, methods, and data sources.
4. Main results and outcomes.
5. Conclusions and implications.

Supply your author name, title, date, degree, programme, specialisation, supervisors and relevant keywords through the first file’s metadata. The pipeline formats the abstract header and calculates its page-count field. Check the generated header rather than typing a separate one into the abstract text. Make the contribution and validation outcome apparent where space allows.

Do not include citations, figures, tables, numbered subsections, or promises about future work. Describe completed research in the past tense and use impersonal language. If Finnish or Swedish is required, supply the translated abstract and matching metadata as described in [Abstracts and Metadata](ABSTRACT-METADATA.md).

### Table of Contents and abbreviations

Write your headings in Markdown; the pipeline generates the contents and appendix entries. Do not type a separate contents page or manually add appendix entries. Check that headings and destinations are correct in the PDF. Provide an alphabetical abbreviation list when needed, and explain abbreviations at first use in the text as well.

## 4. Chapter 1: Introduction

The Introduction establishes the research argument. It must contain all of the following:

| Element | What it must explain |
|---|---|
| Problem context | The research or industry setting, supported by relevant sources |
| Problem statement | A precise knowledge gap or engineering challenge; a company request alone is insufficient |
| Why the problem persists | Relevant prior work and its specific insufficiencies |
| Importance | The practical or theoretical consequences and value of addressing the problem |
| Objective | A concrete outcome: design, develop, evaluate, compare, or establish something |
| Research questions | Specific, answerable questions that organize the investigation |
| Contributions | What new knowledge, method, system, framework, or insight the work offers |
| Scope and delimitations | What is included, excluded, and intentionally bounded, with reasons |
| Method overview | The research design and a short account of the approach |
| Validation overview | How success, correctness, or usefulness was assessed |
| Commissioning context | A short organization description when relevant |
| Thesis structure | A closing paragraph explaining each chapter’s role |

State the contribution without reporting detailed findings. Keep detailed theory, procedures, results, and the later assessment of research weaknesses in their respective chapters. Use formal, impersonal language and describe the completed study rather than leaving a proposal’s future-tense promises in the final Introduction.

### Research questions: formulation and follow-through

Formulate at least one specific, answerable research question. A small set of roughly 1–3 questions is often easier to address coherently; add questions only when they serve the study and can be answered with the available evidence.

A useful question identifies the investigated relationship, outcome, process, or design issue, with enough context to determine what evidence could answer it. Each question must be feasible within the available scope, resources, access, and time.

Illustrative question patterns, to adapt to the actual study:

- **Requirements:** Which requirements follow from the documented problems and stakeholder needs in the selected setting?
- **Design:** How can the proposed approach address those requirements under the stated constraints?
- **Evaluation:** How does the approach compare with the selected baseline on defined criteria under specified conditions?

These patterns are optional drafting aids, not mandatory question types. Interview, interpretive, and other studies need questions appropriate to their own research designs.

Avoid questions such as “What is AI?” that invite background description, questions too broad for one study, or questions that assume success before evaluation. An objective states what the thesis aims to achieve; an RQ states what it investigates; a method states how it investigates it.

For every RQ, identify the method, data, analysis, results, interpretation, and final answer. Preserve numbering and meaning across chapters. Explain justified revisions from the approved proposal.

### Contributions: what to claim

A contribution may be a justified and evaluated method, an engineered artifact with evidence about its performance, a framework supported by case evidence, or new empirical insight. Explain what it adds relative to existing knowledge or practice and why that addition matters.

Separate the **deliverable** from the **contribution**. A prototype is a deliverable; evidence about what its design achieves, under which conditions, and with what tradeoffs establishes its research value.

State contributions in the Introduction, demonstrate them in Results, and assess their significance in Conclusions. Identify your own work and distinguish it from existing tools, reused components, and team contributions. Avoid claims such as “first,” “best,” or “general solution” without sufficient evidence.

### Delimitations versus research limitations

| Concept | Meaning | Main location | Illustration |
|---|---|---|---|
| Delimitation | An intentional boundary of the study | Introduction | Only one organization or selected operating conditions were included |
| Research limitation | A weakness or evidence constraint affecting what can be concluded | Discussion and Conclusions | One organization limits transferability; short testing gives no evidence of long-term performance |

One circumstance can be both a chosen boundary and a source of uncertainty. Explain its consequences later instead of merely repeating the original scope statement.

## 5. Chapter 2: Method and Material

Describe the study in enough detail for another researcher to understand, assess, and reproduce its procedures. Name the research design and justify its fit to the research questions; a list of tools or activities is insufficient.

Include clearly identified subsections for:

- **2.1 Research Design**
- **2.2 Reliability and Validity**

Additional material may be organized within these or in further subsections.

### Research Design

Include:

- The named approach, such as design science, case study, action research, or experiment, with justification and relevant methodological sources.
- The study setting, sequence of activities, and connection between each RQ and its method.
- Data sources, sampling or selection, participants or materials, collection procedures, and timing.
- Tools, instruments, platforms, and configurations needed to understand or reproduce the work.
- The analysis procedure: how measurements, documents, observations, or interview data became findings.
- The evaluation design, including criteria and suitable comparators or baselines where relevant.
- Reasons for major methodological choices and the relevant alternatives.

Address ethics, privacy, consent and handling of sensitive data where applicable. Explain permissions and safeguards relevant to your material. Include a research timeline if it helps explain the sequence of work.

### Reliability and Validity

Explain why your methods can produce trustworthy answers. Consider safeguards appropriate to your study:

- **Reliability:** stable procedures, documented configurations, consistent coding, repeat measurements, or audit records as appropriate.
- **Validity:** whether the evidence actually supports the intended claim and whether relevant alternative explanations were considered.
- **Bias and objectivity:** researcher influence, participant selection, evaluator subjectivity, and measures taken to reduce their effects.
- **Transferability / generalizability:** the settings and populations to which findings may reasonably apply.

Choose safeguards appropriate to the research design; not every study needs statistical testing or identical replication. Acknowledge unavoidable subjectivity and explain how it was managed. Do not assert that reliability is guaranteed merely because established tools were used.

Keep findings and detailed subject theory out of this chapter. Report what was actually done rather than retaining a proposal’s future-tense plan.

## 6. Chapter 3: Current State Analysis / Project Specifications

Explain which approach is used and why. Investigate the actual problem systematically using evidence, rather than providing a general company profile.

For **Current State Analysis**, document the relevant existing process or system, structured stakeholder input, weaknesses, root causes, and prioritized improvement needs. Support the analysis with identifiable data or case documents.

For **Project Specifications**, derive and justify requirements, constraints, and technical specifications. Explain selection criteria and the reasoning behind relevant tool or system choices.

In either case:

- Connect findings to the research questions.
- Show how evidence leads to requirements or priorities.
- Explain which findings motivate the theory explored next.
- Use relevant diagrams, comparison tables, or a requirements matrix where useful.

Keep this chapter focused on evidence about the case and its requirements. Identify relevant case or internal documents, respecting confidentiality. Develop the external theoretical discussion in the next chapter and present the developed solution in Results. Record requirements and their rationale here without prematurely presenting the solution.

## 7. Chapter 4: Theoretical Background

Develop a critical, relevant account of the state of the art. Explain the concepts needed for the study, compare competing approaches, assess their strengths and weaknesses, and synthesize the knowledge that informs the solution or investigation.

Every topic must connect to an RQ or a finding from the current-state analysis/specifications. Show why existing work is insufficient for the particular problem and how the selected theoretical framework informs later decisions.

Use credible academic and professional sources, with citations in every paragraph presenting external knowledge. Paraphrase in your own words and make clear which ideas come from which sources. Reserve direct quotations for laws, standards or other official texts whose exact wording is needed, and identify them clearly. See [References and Citations](REFERENCES.md) for the supported citation format.

Use topic-specific headings. Avoid disconnected source summaries, irrelevant textbook material, unsupported opinions, and reliance on Wikipedia or unreliable web sources as primary references. Keep implementation details and original results out of this chapter.

## 8. Chapter 5: Results and Analysis

Present your original work and the evidence used to evaluate it. Explain the developed artifact, method, framework, or empirical findings in a logical sequence suited to the study.

Required content includes:

- The original contribution and its connection to the research questions.
- How results address the documented requirements.
- How theory informed the design or analysis.
- Justification of significant architectural, methodological, or tool choices.
- Systematic testing, measurement, or evaluation against defined criteria.
- Analysis of the findings, including relevant failures and tradeoffs.
- Application of the reliability and validity considerations established in Chapter 2.

As appropriate, report test conditions, sample or dataset details, baseline comparisons, expected versus actual outcomes, and uncertainty. These details operationalize reproducibility; the exact form depends on the method.

A useful optional matrix is:

| Requirement / RQ | Design feature or investigation | Evaluation method | Evidence location | Outcome |
|---|---|---|---|---|
| Identifier | What addressed it | How it was assessed | Table, figure, result, or appendix | Met, partly met, unmet, or unresolved |

Distinguish measured results, participant reports, researcher interpretation, and untested proposals. Do not invent evidence to complete a matrix. A demonstration supports only the conditions demonstrated; stronger claims require stronger evidence.

Introduce necessary theory earlier. Put long code listings and raw data in appendices while retaining enough explanation and evidence in the main text for the argument to stand on its own.

## 9. Chapter 6: Discussions and Conclusions

Cover both interpretation and final answers, with clear subsections if helpful.

### Discussion

- Briefly recall the problem, objectives, and scope.
- Explain what the findings mean for the RQs.
- Compare findings with the theory and prior work already introduced.
- Assess what succeeded, what failed, why, and to what extent the problem was addressed.
- Explain practical and broader research implications in proportion to the evidence.
- Analyze actual research limitations and their effect on credibility, completeness, and transferability.
- Give evidence-based recommendations and specific future research directions.

For each important limitation, explain **the constraint, the affected finding or claim, its consequence, and any mitigation or remaining uncertainty**. Relevant issues may include small or selective samples, a single setting, subjective judgments, researcher involvement, imperfect instruments, absent comparators, short observation periods, and unavailable longitudinal evidence. Include only limitations that apply to the actual study.

Future work should follow from unresolved questions and limitations. A technical feature wishlist alone does not explain what further research would establish.

### Conclusions

- Answer **every RQ explicitly**, using evidence already presented.
- State how far each objective was achieved, including partial achievement.
- Assess each claimed contribution and its significance relative to prior work.
- Explain what the study established that would otherwise remain unknown.
- State how trustworthy the findings are and where the final claims stop.
- Give the principal recommendations and future directions.

An answer can be partial or inconclusive when evidence is limited; say what was established and what remains unresolved. Do not force a successful answer unsupported by the study.

Do not introduce new data, results, theory, or analysis. Discussion interprets existing findings; conclusions give the resulting final positions. Avoid repeating Results verbatim.

## 10. Chapter 7: Summary

Provide a factual recap of approximately **1–2 pages**:

1. Research objective or question.
2. Method in one or two sentences.
3. Main findings.
4. Main conclusions.

Add no new evidence, interpretation, analysis, or recommendations. The Summary condenses the work; it does not replace the evaluative Discussion and Conclusions.

## 11. References and appendices

### References

Use the repository’s keyed bibliography format, which produces numbered citations and references. Write complete reference details consistently in the required Vancouver style. Cite external claims, paraphrases and reused material properly, and verify bibliographic details against the source. Define each source once in `input/80-references.md` and cite its key in the text; see [References and Citations](REFERENCES.md) for examples.

Keep References unnumbered in the chapter structure. The number of preliminary sources in a proposal is not a sufficient-source quota for the completed thesis; coverage and quality must support your actual argument.

### Appendices

Include supporting material such as instruments, detailed specifications, test protocols, supplementary results, and long code listings when applicable. Refer to each relevant appendix from the main text and keep essential reasoning in the chapters.

Use the appendix files and headings shown in the sample. The pipeline creates page breaks, appendix labels, headers and figure/table numbering. Supply descriptive captions without manually typing their generated numbers. Check the final PDF after adding or reordering appendices.

## 12. Writing, presentation, and integrity rules

Use these checks to keep your manuscript clear and consistent:

- Start each main chapter on a new page.
- Put explanatory text after every heading; avoid heading-to-heading sequences.
- If a subsection exists, provide at least one sibling subsection at the same level.
- Avoid third-level headings unless justified; do not use fourth-level headings.
- Use descriptive headings rather than questions or full sentences.
- Use at least two sentences per paragraph.
- Introduce every figure/table before it appears and explain it afterward.
- Caption tables above and figures below; number and reference visual material and listings.
- Use dedicated styles for code, quotations, and lists; number formulas and explain variables.
- Use formal academic language without personal pronouns or colloquialisms, except the permitted informal Preface.
- Use past tense for completed research activities and present tense for established facts or statements about the document. Keep the final abstract and introduction consistent with the work actually completed.
- Follow your programme’s current rules for AI assistance, originality checks and disclosure. You remain responsible for the text, sources, analysis and accuracy of every claim. Never invent data, references, results or work that was not performed.

## 13. Cross-section traceability check

Use this table during planning and final review:

| Thread | Introduction | Method | CSA / Theory | Results | Discussion / Conclusions |
|---|---|---|---|---|---|
| Each RQ | Formulated | Means of answering specified | Relevant foundation | Evidence reported | Meaning discussed; answer explicit |
| Each contribution | Identified | Means of establishing it | Gap and rationale | Demonstrated | Significance assessed |
| Requirements | Scope introduced | Derivation/evaluation procedure | Derived and justified | Addressed and tested | Achievement assessed |
| Limitations | Boundaries stated | Threats and safeguards explained | Context constraints identified | Evidence constraints reported | Actual consequences analyzed |
| Validation | Strategy outlined | Criteria and procedure specified | Rationale supported | Evidence and analysis | Credibility and claim boundaries assessed |

Also check that terminology, scope, tools, datasets, and reported procedures remain consistent. Changes from the approved proposal should be explained. Claims in the abstract must match the final Results and Conclusions.

## 14. Self-review checklist

Use this checklist to review your draft and prepare questions for supervision. It is not a grading scale; consult your programme’s assessment criteria for the formal requirements.

| Review area | Evidence of strong master’s-level work | Warning signs |
|---|---|---|
| Problem and significance | Precise, bounded, literature-supported problem | Broad topic or company task without research framing |
| Research gap | Critical account of prior work and its insufficiency | Unsupported assertion that little research exists |
| RQs and objectives | Feasible questions, concrete outcomes, consistent follow-through | Questions omitted, overly broad, or dropped later |
| Contribution | Identifiable original work with evidenced significance | Deliverable presented without established research value |
| Literature | Relevant comparison, evaluation, and synthesis | Descriptive summaries, weak sources, unsupported claims |
| Method | Named and justified design; clear data and analysis procedures | Activities listed without research logic |
| Reliability and validity | Specific threats, safeguards, and remaining uncertainty | Generic assurances or missing required subsection |
| Current-state / specifications | Evidence-based findings and justified requirements | General company description or assumed requirements |
| Results and validation | Systematic evidence tied to criteria and RQs | “It works” claims or unsupported interpretation |
| Discussion | Critical interpretation and comparison with prior work | Repetition of results or unexplained success claims |
| Conclusions | Explicit answers and proportionate contribution assessment | Unanswered RQs or claims beyond the evidence |
| Limitations | Actual weaknesses and their consequences explained | Only out-of-scope features listed |
| Coherence and integrity | Traceable argument, accurate sourcing, consistent account | Contradictions, uncited material, invented evidence |

When checking your draft, record the relevant section, the problem and the revision needed. Address missing evidence, unanswered questions and contradictions before polishing the wording. A polished document or a large page count is not a substitute for research quality.

### Evidence appropriate to your topic

Choose evidence and evaluation criteria that fit your research questions and technical subject. A performance study may need workload definitions, measurements and baselines; an interview study may need a justified participant selection and a transparent analysis process. A security or reliability claim needs checks that actually address the claimed property.

Explain why your chosen checks are appropriate and what they cannot establish. Discuss unfamiliar methodological or technical requirements with your supervisor.

## 15. Planning the proposal and completing the thesis

Prepare a proposal with a working title, background and problem, objective and scope, research questions, approach and methods, validation plan, preliminary structure, schedule and preliminary sources. Include sources that establish the problem and research gap, not just general background. Agree the scope, access to material and feasibility of the plan with your supervisor before starting the main study.

Plan time for supervisor feedback, revisions, language checking, the required originality check and final PDF review. Confirm your programme’s current instructions for topic approval, the maturity demonstration, presentation, submission and publication. These are process steps rather than additional thesis chapters; keep administrative documents outside `input/`.
