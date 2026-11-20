---
name: job-followup
description: Review the job tracker of this job-search project - list and draft the follow-ups that are due, close applications that stayed silent, fix stale tasks and statuses, and report weekly numbers against the target. Use for "what's due?", "follow-ups", "pipeline review", "weekly review", or after the user reports a reply, rejection or interview.
---

# job-followup

Keeps the pipeline moving with drafts the user can send in two minutes. It drafts; the user sends. It never emails, calls, messages or posts.

## 0. Before you start
1. Confirm today's date with the user (scheduled run: use the system date and state it).
2. Read the tracker: `jobs`, `tasks`, `contacts`. Rows whose text starts with "EXAMPLE ROW" are demo data from the kit: handle them like real rows so the user can see how the skill works, label them "(example)" in the report, never write to them, and leave them out of the weekly numbers.
3. If the user reports news first (reply, rejection, invitation, application sent), record that before anything else: `status`, `applied`, `first_reply` (ISO date of the first human reply), `notes_rejection` or `interview_notes`, and set the linked tasks to `done`.

## 1. What is due
Days are calendar days since `applied`, or since the last contact.
- **Day 8–10, no reply:** one follow-up, only if there is a named contact or a recruiting address. Email first. For tier-1 jobs, a call 3 days later if there is still nothing (mid-morning works best).
- **Portal-only, no contact** (one-click apply, large applicant systems): no follow-up. Do not invent a contact.
- **Day 21, still nothing** (and no stated deadline or "in review" note): set `closed: "ghosted"` and clear `next`. Keep `status`. List these in the report.
- **Stated deadline or timeline:** follow up 2 working days after that date, not before.
- **After an interview:** thank-you within 24 hours (3–5 sentences, one concrete point from the talk). If no decision date was given: follow up after 5–7 working days.
- **Small jobs:** after 5 days, a call or a visit with a printed CV.
- **Talent pool or speculative application:** one follow-up at 4–6 weeks, then close.
- One follow-up per stage, and at most one last reminder 7–10 days later.

These timings are starting values. When the tracker holds 20 or more replies with dates, say what the user's own median reply time is and suggest adjusted days.

## 2. Drafts
For each due item give: recipient (name, address or phone from `contacts`), channel, subject, and the text.
- Language of the posting. Short sentences at the user's own language level, so the user could say them. Emails: at most 90 words. If the draft is not in English, add an English translation underneath.
- Content: job title, job ID and date applied; one line of continued interest; one new fact if there is one; one clear, polite question (status or next step). No pressure, no apology.
- Call script: opening line, the question, two phrases for asking back, closing. Keep it short.
- The truth rules of the project instructions apply to every sentence about the user. Do not name other employers. "I have another offer with a decision date of <date>" only if it is true and the user approves.

## 3. Parallel processes
- List every process at interview stage with its next date, start date, weekly hours and pay.
- Flag conflicts with the weekly hour limit (all jobs together) and with the timetable in the project instructions.
- Never suggest withdrawing anywhere before a contract is signed. If an offer has a deadline and another decision is pending, draft a polite request for a decision date to the second company; the user decides whether to send it.
- For every offer, remind the user to ask: first pay date, notice period, probation, contract length.

## 4. Hygiene
- Tasks open more than 7 days past `due`: propose done, re-date or delete, one line each. Change them only after the user answers ("yes to all" is fine).
- Status mismatches: list them, fix after the user's OK.
- `open` jobs older than 14 days without action: ask "apply or drop?".
- Empty `channel`, `letter`, `posted_date`, `first_reply`: fill from notes only where the note is unambiguous.

## 5. Weekly numbers (on "weekly review" and in the scheduled review)
From the tracker, with counts shown: applications this week against the weekly target; replies; interviews; median days to first reply; interview rate by role family, by channel and by posting age at application (7 days or less against older); share of applications with a letter. One sentence on what to change next week. Always give "n = ..." and do not over-read small numbers.

## 6. Report layout
1. **You must do today** (at most 5, in order, each with the ready draft).
2. This week (dated list).
3. Closed as ghosted, and proposed clean-ups.
4. Parallel processes and conflicts.
5. Tracker changes made (row ids).

## Guardrails
Draft only. No sending, calls, messages, form submissions or calendar invitations. Tracker writes are limited to: recording what the user reported, `closed: "ghosted"` under the day-21 rule, new follow-up tasks, and clean-ups the user approved. Never delete a job row.

## Failure modes
Contact missing → say "no contact, no follow-up"; do not guess an address. Dates in notes are "reported on" dates → treat `first_reply` as "by <date>". Tracker unreachable → stop and say so. Version conflict → re-read and retry once.
