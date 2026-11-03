# Writing thesis chapters in Markdown

Write the thesis as ordinary Markdown: headings, paragraphs, lists, emphasis and links. The example files in [input](../input) show these forms in context. The PDF pipeline supplies the university layout, contents, numbering and page styles.


## Files and reading order

Keep chapter files directly inside `input/`, and images and supporting files in `input/assets/`. Save text files as UTF-8. Filename prefixes determine reading order; the prefixes are not printed as chapter numbers.

| File | Purpose and suggested content |
|---|---|
| `00-abstract.md` | Metadata and the English abstract. Summarise the objective, methods, main results and conclusions. See [abstracts and metadata](ABSTRACT-METADATA.md). |
| `00a-tiivistelma.md` | Finnish abstract, included only when enabled in metadata. |
| `00b-sammanfattning.md` | Swedish abstract, included only when enabled in metadata. |
| `01-preface.md` | Optional acknowledgements and personal context. Keep research findings in the main chapters. |
| `02-abbreviations.md` | Abbreviations actually used in the thesis, with their meanings. |
| `10-introduction.md` | Problem, context, motivation, objective, research questions, intended contribution, scope and thesis structure. Explain deliberate exclusions in a Scope and Delimitations subsection. |
| `11-method.md` | Research design, material or data, selection, collection, tools, analysis and evaluation procedure. Explain reliability, validity and ethical considerations. Distinguish planned checks from checks actually performed. |
| `12-specifications.md` | Current situation and evidence of needs. Derive requirements, constraints and measurable acceptance criteria from that evidence. |
| `13-theory.md` | Relevant concepts, previous work and technical foundations. Compare sources and explain how they inform the design or analysis. |
| `14-results.md` | Developed solution or findings, design decisions, implementation where relevant, evaluation method and evidence. Explain figures/tables and distinguish measured results from assumptions. |
| `15-discussion.md` | Interpret findings, answer research questions, relate results to earlier work, assess limitations and give justified conclusions and recommendations. Distinguish study limitations from intentional scope exclusions. |
| `16-summary.md` | Concise factual recap of the problem, approach, main findings and contribution. Avoid introducing new results or arguments. |
| `20-references.md` | One keyed bibliography. See [references and citations](REFERENCES.md). |
| `30-appendix-a.md` and later appendix files | Supporting material mentioned in the body: detailed data, protocols, extended tables or code. Retain the main argument in the chapters. |

These are the sample's chapter functions, not a requirement to reproduce its fictional project. Adapt the structure with your supervisor. For bachelor work, explain the practical problem, engineering work and evidence of its outcome. For master work, make the research questions, methodological justification, evaluation and contribution especially clear. Use actual evidence and identify proposed or illustrative material honestly.

Remove unused optional sections. Keep notes, old drafts, README files and guides outside `input/`: every top-level `.md` file there is read as manuscript content. Put thesis metadata only in the first abstract file.

## Headings and paragraphs

Use `#` for a chapter, `##` for a section and `###` for a subsection. Leave a space after the hash characters and do not type chapter numbers.

```markdown
# Introduction

Describe the problem and why it matters. Explain the context of the work.

## Objective and Research Questions

State the objective and the questions the thesis will answer.

## Scope and Delimitations

Describe what is included, what is excluded and why.
```

Do not skip heading levels. Use descriptive headings and explain the subject under each one. Separate paragraphs with a blank line; do not insert a blank line in the middle of a sentence. Let the PDF wrap lines automatically.

Use the supplied special headings for front matter: `# Abstract`, `# Preface`, `# Abbreviations` and `# References`. The generated title page and contents do not need their own Markdown files.

## Emphasis, identifiers and lists

```markdown
Use **bold** for emphasis and *italic* when appropriate.
The field `event_id` identifies the event.

- Validate the input.
- Store the accepted record.
- Return the result.

1. Prepare the test data.
2. Run the defined checks.
3. Record and interpret the outcomes.
```

Use backticks for commands, filenames, paths and identifiers. Keep list items together without blank lines between them when they form a simple list. Use prose paragraphs to explain the significance of a list.

For a short quotation, use `>` and identify its source in the surrounding text with a citation. A web link such as `[project documentation](https://example.org/docs)` does not replace a bibliographic citation supporting a claim.

## Figures

Put the image in `input/assets/` and refer to it relative to the chapter file:

```markdown
The diagram summarises the service boundaries.

![Service components](assets/architecture.png "Service architecture and request boundary.")

Explain the components and the design decision illustrated by the figure.
```

The quoted text is the caption. Supply only its description: the PDF adds `Figure` and its number. Introduce and interpret figures in the prose, and acknowledge reused material with a citation. Check that labels remain readable at the rendered size.

An optional width is a fraction of text width:

```markdown
![Request sequence](assets/sequence.png "Request sequence.") {width="0.65"}
```

Use PNG or JPEG assets and simple filenames without spaces. Keep width values greater than zero and at most one. References to figure numbers in prose need checking after edits; the Markdown does not automatically update them.

## Tables

Place a `Table:` caption before a regular Markdown table:

```markdown
Table: Requirements and acceptance checks. {widths="1,3,3"}

| ID | Requirement | Acceptance check |
|---|---|---|
| R1 | Preserve event identity | Compare IDs with stored records |
| R2 | Reject changed content | Inspect the conflict response |
```

Use the same number of cells in every row. The first row is the header. Optional `widths` values are positive column proportions, with one value per column. Omit the attribute for equal widths. Avoid literal `|` characters within cells.

The PDF numbers the table and repeats its header if it spans pages. Keep a long table together instead of copying headers and captions into separate continued tables. Merged cells and nested tables are outside this simple format. Explain what the table shows in the surrounding text.

## Code, JSON, YAML and other listings

Use fenced code blocks with a language and a caption:

````markdown
```python caption="Check whether an event identifier is present."
def valid_event_id(event_id):
    return isinstance(event_id, str) and bool(event_id.strip())
```
````

Use `json`, `yaml`, `sql`, `bash` or another supported language for the corresponding content; use `text` for logs or unfamiliar formats. Preserve indentation. A listing is displayed, not executed. Supply only the caption description, without a manually typed listing number.

For an associated source file, the opening fence can also contain `source="assets/accept_event.py"`. That file must exist. The displayed code still comes from the fenced block, so keep both versions consistent. Explain short extracts in the body and put extensive supporting material in an appendix. Remove credentials and private data.

## Mathematics

Use `$...$` for inline mathematics and a separate `$$` block for a displayed equation:

```markdown
Let $n$ denote the number of accepted events.

$$
r = \frac{n}{N}
$$

Here, $N$ is the total number of submitted events.
```

Define symbols, units and assumptions in the prose. Use `\$` for a literal currency dollar sign. Mathematical notation is the specialised syntax inside otherwise regular Markdown.

## Appendices and final checks

Start an appendix with a heading such as `# Appendix A. Test Protocol`, following the included files. Refer to each appendix from the body. The pipeline supplies appendix labels and numbering.

Replace the sample's author, topic, synthetic findings and example assets with your own work. Before submission, check the generated PDF's headings, figures, tables, code, citations, contents and page breaks. Markdown previews show content, but the thesis PDF determines the final layout.
