# Abstracts and metadata

The first file, [input/00-abstract.md](../input/00-abstract.md), contains the thesis metadata and English abstract. Metadata supplies the cover, student details and abstract header. The chapters remain regular Markdown.

## Fill in the first file

Keep metadata between the two `---` lines at the beginning of the file. Replace the example values:

```markdown
---
title: Your Thesis Title
subtitle: An Optional Subtitle
author: Your Full Name
degree_programme: Information Technology
professional_major: Your Specialisation
submission_date: May 2027
language: en
degree: master
tiivistelma: false
sammanfattning: false
keywords: first keyword, second keyword, third keyword
advisors:
- Supervisor Name (Title)
---

# Abstract

Explain the objective and context of the work.

Describe the methods and material actually used.

Report the principal results.

State the conclusions and the limits of what the results establish.
```

Use `degree: bachelor` for bachelor work or `degree: master` for master work. This selects the corresponding PDF template. `degree_programme` is the programme name, not the degree level. The sample uses `master`.

| Field | What to supply |
|---|---|
| `title` | The full thesis title. Quote the whole value if it contains a colon, for example `title: "Event Processing: A Case Study"`. |
| `subtitle` | Optional subtitle; remove the field if it is not needed. |
| `author` | Your full name. |
| `degree_programme` | Your official programme name. |
| `professional_major` | Your specialisation, where applicable. |
| `submission_date` | The submission date or month/year required for your thesis. |
| `language` | Keep `en` for the English manuscript illustrated here. |
| `degree` | Exactly `bachelor` or `master`. |
| `keywords` | Relevant keywords separated by commas. |
| `advisors` | Supervisor names and titles, with one `- ` list item per person. |
| `tiivistelma` | Whether to include the Finnish abstract. |
| `sammanfattning` | Whether to include the Swedish abstract. |

Keep metadata only in this first file. Use one field per line, simple text values, comma-separated keywords and the shown supervisor list format. Write `true` and `false` without quotes. Do not use YAML anchors, inline arrays, multiline block values or inline comments. Keep references in their separate [References file](REFERENCES.md).

## Choose the abstract languages

The English abstract remains included. Choose at most one alternative abstract:

| Required output | `tiivistelma` | `sammanfattning` | Additional text file |
|---|---|---|---|
| English only | false | false | None |
| English and Finnish | true | false | `00a-tiivistelma.md` |
| English and Swedish | false | true | `00b-sammanfattning.md` |

Both flags default to false if omitted. **The supplied sample explicitly enables Finnish and disables Swedish.** Change these existing fields rather than adding duplicate settings. The sample also contains `allow_multiple_alternative_abstracts: false`; leave it false or omit it. The current submission pipeline permits only one alternative abstract.

Follow your programme's language requirements when choosing. Keeping a translation file does not enable it: the corresponding flag must be true. A disabled translation is omitted from the PDF. An enabled translation requires nonempty text.

## Finnish abstract

In the first file's metadata, set:

```yaml
tiivistelma: true
sammanfattning: false
title_fi: Opinnäytetyön suomenkielinen nimi
degree_programme_fi: Tieto- ja viestintätekniikka
professional_major_fi: Suuntautumisvaihtoehto
keywords_fi: ensimmäinen avainsana, toinen avainsana, kolmas avainsana
```

Replace the content of `input/00a-tiivistelma.md`:

```markdown
# Tiivistelmä

Kirjoita tähän suomenkielinen tiivistelmäsi.
```

Supply your own translation of the thesis objective, methods, results and conclusions. Keep metadata in `00-abstract.md`; this translation file contains only its heading and prose.

## Swedish abstract

In the first file's metadata, set:

```yaml
tiivistelma: false
sammanfattning: true
title_sv: Svensk titel på examensarbetet
degree_programme_sv: Informationsteknik
professional_major_sv: Inriktning
keywords_sv: första nyckelordet, andra nyckelordet, tredje nyckelordet
```

Replace the content of `input/00b-sammanfattning.md`:

```markdown
# Sammanfattning

Skriv din svenska sammanfattning här.
```

The PDF uses Swedish field labels and `Nyckelord`. It does not translate the abstract or metadata. Supply the same objective, methods, findings and conclusions as in English. The bachelor/master selection still comes from the same `degree` field.

## Check the abstracts in the PDF

Each complete abstract page, including the header and keywords, must fit on one page. Use plain paragraphs and keep citations, figures, tables and code out of the abstract. Shorten overly long text rather than adding manual page breaks or changing fonts.

Check names, programme, supervisor titles, translated fields and keywords in the generated PDF. The current layout places the English abstract before the selected alternative. If a translated metadata value is omitted, some fields fall back to English; provide the translated values to avoid mixed-language headers.
