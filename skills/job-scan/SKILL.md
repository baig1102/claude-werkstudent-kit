---
name: job-scan
description: Scan for new student jobs (Werkstudent, HiWi, small jobs) for the user of this job-search project, check that each posting is live, remove duplicates against the tracker, score, and add new jobs to the tracker. Use for "scan jobs", "any new jobs?", a scheduled scan, when the user pastes job-alert emails, or before any job suggestion.
---

# job-scan

Finds new jobs, checks they are real, scores them, and adds them to the tracker. It never applies, never writes a cover letter, and never messages anyone.

All personal values (towns, hours, language level, role families, cooldown list) come from the project instructions. Sources and commute times come from the project file `watchlist.md`. If either is missing or still contains placeholders in double braces, stop and say which values are missing.

## 0. Before you start
1. Confirm today's date with the user. In an unattended scheduled run, use the system date and state it in the first line of the report.
2. Read the tracker named in the project instructions: tables `jobs`, `tasks`, `contacts`. If the tracker tool uses versions, pass the version on every write.
3. Read the project instructions (hard gates, truth rules, verification rule). If they disagree with this skill, they win.
4. Time box: 25 minutes. At most **5** new jobs per run. An empty run is a normal result: say so, never pad.

## 1. Sources
Search window: last 24 hours first, then 7 days, then 30 days only if fewer than 2 results.
- **Every run:** job-alert emails or posting text the user pasted into this chat, and any posting page the user opened and asked you to read.
- **Rotation over the week**, by the weekday of the run (manual and scheduled runs alike; the user may name another group):
  - Monday or Tuesday: watchlist company pages, Group A;
  - Wednesday or Thursday: university and research job pages, and small-job employers while no contract is signed;
  - Friday to Sunday: watchlist company pages, Group B, and public job boards for discovery only (then look for the same job on the company's own portal).
- Any company with a tracker job in status `open` or `applied` may be checked on any day.

**Sign-in sites (LinkedIn, XING, and any site that shows a login wall):** never search, scroll or collect postings there, never sign in, never use a scraper or an API. Use only what the user pasted or the single page the user opened. If a page shows a sign-in wall or a CAPTCHA, stop that source and say so.

**Pages you cannot read.** Many career portals load their job list with JavaScript, so the page text shows no postings, and some block automated reading. In both cases do not work around it (no other tools, no mirrors, no caches). List the source under "not readable" in the report and ask the user to open it and paste either the posting text or the link to one single posting page; single posting pages are often readable even when the list is not. A job you only know from such a list is `unverified`.

## 2. Hard gates: skip the job (do not add it) if any is true
Apply every gate in the project instructions: weekly hours, German level phrases, commute and on-site days, missing requirements, cooldown companies, internship rules. Also skip:
- jobs already in the tracker (match on link, job ID, or company plus normalised role title). If an existing job was relisted, update that row's `posted` and `notes`; do not add a new one;
- mass advertisements without a named employer.

## 3. Liveness (state it for every job)
- `verified`: seen today on the company's own portal with a live posting or a working apply button. Record the link, the posting date (or "undated") and what you saw.
- `live-recent`: posted by the company itself within the last 14 days, seen in a pasted job alert or on a page the user opened, not found on the company's own portal.
- `unverified`: aggregator only, a PDF on a server, a university PDF older than about six weeks, or any page saying the posting is closed (in Germany for example "bereits besetzt", "nicht mehr verfügbar", "inaktiv"). Unverified jobs get tier 3, no letter, and `next: "verify first"`.

## 4. Commute
1. If the tracker already has a job at the same site with a commute, reuse it.
2. Otherwise use the commute table in `watchlist.md`.
3. If the town is not in the table, write "unknown" and score commute 0.5. Do not guess minutes.

## 5. Score (0–100), show the parts
`score = 30·fit + 25·odds + 15·speed + 10·commute + 10·pay + 10·language` (each part 0–1)
- **fit**: 1.0 near-exact match to the user's proven work; 0.7 good; 0.4 stretch; 0.2 weak. Judge only against the "Real scope" lines in the truth rules.
- **odds**: base 0.6. +0.2 if the role is in a strong family, −0.2 if in a weak family (project instructions). Multiply by posting age: ×1.0 if 3 days or less, ×0.8 at 4–7, ×0.5 at 8–14, ×0.3 at 15–30, ×0.1 older or undated and clearly old. +0.1 if the user's degree subject is named; +0.1 if there is a named contact or the company is small. −0.2 if the posting shows more than 100 applicants or asks for a different degree only. Clamp to 0–1.
- **speed**: 1.0 start now or within 2 weeks; 0.6 within 6 weeks; 0.3 later; 0.5 unknown.
- **commute** (one way): 30 minutes or less 1.0; up to 60 0.8; up to 90 0.5; up to 120 0.3; remote 1.0; hybrid: the better of the commute score and 0.7.
- **pay**: €18/h or more 1.0; €15–18 0.8; legal minimum wage to €15 0.6; unknown 0.5. Below the user's minimum pay: skip.
- **language**: no level stated, English accepted, or a level at or below the user's certified level 1.0; one step above ("gut", "sicher" for a B1 user) 0.6.
Tier: 70 or more → 1; 50–69 → 2; under 50 → 3. Small jobs: fit 0.6 and odds 0.8 if the language gate passes.

These weights are starting values. After about 20 applications the weekly review may suggest changes.

## 6. Write to the tracker
One row per new job in `jobs`, id = short kebab-case (`company-topic`). Fields: `company, role, location` (with commute and its source), `link, posted, posted_date` (ISO or empty), `lang, fit` (2–3 factual sentences, real scope only), `cv` (a variant name from the project instructions), `category` (student-job | small-job), `family`, `channel` (portal | alert | agency | university | speculative | direct), `status: "open"`, `tier, added` (today, ISO), `score, score_parts, live_status, live_checked`, `next: "NEW from scan - review"`.
If a tracked `open` job has disappeared from its portal, do not change its status: list it under "possibly closed".

## 7. Report
Scheduled runs: at most 6 lines. Manual runs: a short table.
Date and sources covered; sources not readable; new jobs (score, company and role, liveness, link, posting date, recommended CV, letter worth it? yes only if compulsory, or score 70 or more and posted within 14 days and a person will read it); possibly closed postings; tasks due today; sources not covered and why. In manual runs end with: "Tell me which ones to build an application pack for."

## Guardrails
- Read-only everywhere outside the tracker. Never click apply, save, follow, message or sign up. Never enter the user's data into a form. Never sign in anywhere.
- Never write a cover letter in this skill, and never for an unverified job.
- Numbers (applicants, dates, pay, commute) only as observed or from the commute table; write "not stated" otherwise.

## Failure modes
Portal blocks reading or shows no postings as text → list it as "not readable", ask the user to open it and paste a posting or a single posting link. Sign-in wall or CAPTCHA → stop that source and say so. Version conflict on write → re-read the row and retry once. Tracker unreachable → stop and report; do not work from memory.
