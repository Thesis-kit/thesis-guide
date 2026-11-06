# References and citations

Define all sources in [input/80-references.md](../input/80-references.md). Cite them in the chapters using stable keys. The pipeline automatically assigns numbers in order of first citation.
 
## Define a source once

Each reference starts with `- [@key]`, followed by its complete bibliographic details:

```markdown
# References

- [@http] Fielding R, Nottingham M, Reschke J. HTTP Semantics. RFC 9110. Internet Engineering Task Force; 2022. Available from: https://www.rfc-editor.org/rfc/rfc9110.html
- [@postgres] PostgreSQL Global Development Group. PostgreSQL 18 Documentation: Constraints, Section 5.5. Available from: https://www.postgresql.org/docs/18/ddl-constraints.html [accessed 27 October 2026].
```

These entries also appear in the sample. Verify the details and use the date you actually accessed a web source. Follow the required bibliographic style consistently; the pipeline orders and numbers references but does not verify authors, dates, titles or URLs for you.

Keys may contain letters, digits, hyphens and underscores. Choose a short, meaningful, unique key, such as `http`, `database-constraints` or `study2026`. Reuse that key whenever citing the same source. Keep each complete entry on one Markdown paragraph; the editor may wrap it visually.

Do not maintain a second bibliography in abstract metadata. In particular, do not add a `references:` metadata field or type numeric bibliography labels manually.

## Cite a source in a chapter

```markdown
The protocol defines the intended effect of repeated requests [@http].
```

The PDF replaces the key with a numbered citation and links it to the corresponding reference. In this renderer, citations in a paragraph are collected at the paragraph's end. Use separate paragraphs when different claims need separate source attribution.

For two sources, write separate citation tokens:

```markdown
The design combines protocol semantics and database constraints [@http] [@postgres].
```

Use `[@http] [@postgres]`, not `[@http, @postgres]`. Do not type `[1]` or `[2]` as substitutes for these citation keys.

## Automatic numbering example

Suppose the chapter first cites the database source:

```markdown
The storage design relies on a documented constraint [@postgres].

Request semantics are addressed separately [@http].

The same database source also explains the selected restriction [@postgres].
```

The PDF assigns the database source number **1**, the HTTP source number **2**, and reuses **1** for the third citation. This holds even if the HTTP definition comes first in the References file. Moving the first citation may change the numbering; the keys remain the same.

Citation order includes supported prose in appendices. An unused source is retained at the end with a warning; remove it if it does not belong in the thesis. Missing keys and duplicate definitions cause errors.

## Sources for figures, tables and quotations

Explain the origin of reused material in an adjacent prose paragraph and cite it there. Keep caption descriptions free of manually typed labels such as `Figure 3.`. For a direct quotation, make it clear which text is quoted and provide the source and any necessary locator in the surrounding prose.

## Check before submission

- Every citation key has exactly one definition in the References file.
- Each source supports the claim attributed to it.
- Repeated citations use the original key rather than a duplicate entry.
- Source details and access dates are accurate and consistently formatted.
- The generated PDF's numbering and reference links work as expected.
