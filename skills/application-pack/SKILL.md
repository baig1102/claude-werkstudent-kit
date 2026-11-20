---
name: application-pack
description: Build a ready-to-send application folder for one tracker job in this job-search project - the right CV variant, certificates, a cover letter (.docx plus PDF copy) only when it is worth it, form answers, a claim-by-claim truth check and a "change before sending" list. Use for "make the pack for a job", "prepare the application for this id".
---

# application-pack

Prepares everything for one application. The user submits it. This skill never sends, uploads, submits or applies.

Personal values come from the project instructions (CV variants, certificates, truth rules, hours, working folder) and from the project file `language-level.md`.

## 0. Before you start
1. Confirm today's date with the user. The letter date is the day the user will send it; ask if unsure.
2. Read the tracker row for the job (`jobs`) and its contact (`contacts`).
3. Re-check liveness now on the company's own page. If the posting is gone or closed: stop, tell the user, set `next: "posting gone <date>"`. If it is `unverified`: build CV and certificates only, no letter.
4. Read the full posting text. Note: compulsory documents, form fields, language of the posting, language level asked, hours, contact name. If the posting is behind a sign-in, ask the user to paste the text.
5. Working folder: use the folder named in the project instructions (`<folder>/<tracker-id>/`). If no folder is reachable, build the files here, deliver them in the chat, and say so.

## 1. Choose the CV (copy, never edit the master)
Pick the variant from the "CV variants" list in the project instructions that matches the role, and say why. Copy it into the job folder. If the role needs a CV change, propose it as text first; after approval make a new versioned copy and never overwrite. Posting in English → an English CV if one exists; otherwise say so at the top.

## 2. Certificates
Attach the "always attached" certificates. Add "only when asked" certificates only if the posting asks. Keep every certificate as a separate file unless the user asks for one file or the portal allows only one upload. List each file and why it is included.

## 3. Cover letter: decide first, and say why
Write a letter only if at least one is true:
- the posting or the form makes it compulsory;
- the tracker `score` is 70 or more AND the posting is 14 days old or less AND there is an upload slot or a named person who will read it;
- it is an email application: then the email body is the letter, at most 120 words, CV attached.
Otherwise write no letter. Write a 3–4 line form message instead (why this role, the one matching project, availability). Time box for a letter: 20 minutes.

Format: one page, a common font at 10.5 pt or larger, name header, contact line, recipient block, date right-aligned, bold subject line with the job title and job ID. Language of the posting. Save a .docx and a PDF copy with the same name: `CoverLetter_<LastName>_<Company>_<Topic>` (German postings: `Anschreiben_...`).

Content, three short paragraphs:
1. the role, and one sentence on why this company;
2. two proofs from the user's real work or studies that match the top tasks in the posting, with a number or result where the CV has one;
3. availability (hours per week, days, start date) and the standard sentence from `language-level.md`.
Plain language. No filler, no list of gaps, no apology for missing requirements.

## 4. Truth check (in writing, in the reply)
Make a table: every factual claim in the letter or form message → its source (CV line, certificate, tracker note, or the user's statement). Delete any claim without a source, or ask. Never combine two facts into a new one. Apply the "Real scope", "Not true, never claim" and "Confidentiality" lines of the project instructions to every sentence. No frequency words unless confirmed. Language level exactly as in `language-level.md`.

## 5. Form answers (`form-answers.md` in the folder)
Availability and start date; weekly hours (all jobs together must stay within the user's limit; name the free days from the timetable); salary expectation (use the range in the posting; if none, ask, do not invent); "how did you find us"; profile links the user listed; the short language sentence. Mark every answer the user must confirm with **CONFIRM**.

## 6. Reply layout
1. **CHANGE BEFORE SENDING**, at the very top: each thing the user must check or edit (date, recipient name, salary, hours, every CONFIRM item, anything you could not verify).
2. What is in the folder (file list) and which CV, and why.
3. Letter decision (written or not, and the rule that decided it).
4. Truth-check table.
5. Where and how to submit (portal link, upload slots, which file goes where). The user submits.

## 7. Tracker
Set `next: "Pack ready - apply by <date>"`, `cv`, `letter: true|false`, `live_checked`. Do NOT set `status: "applied"` or `applied` until the user says it was sent; then set both, and add a follow-up task due 8 days later if a contact is known.

## Guardrails
Never open an application form to type the user's data, never upload, never send email, never use one-click apply. Never overwrite a master CV or an existing letter; add `_v2`. Never delete the user's files. If the facts are too thin for a strong sentence, ask one question; do not guess.

## Failure modes
Posting unreadable → ask the user to paste the text. Folder not reachable → deliver in chat and say so. PDF conversion fails → deliver the .docx and say the PDF is missing. Letter runs over one page → cut content, do not shrink the font below 10.5 pt. Version conflict → re-read and retry once.
