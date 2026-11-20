# claude-werkstudent-kit

A ready-to-use Claude Project setup for international students who are looking for a Werkstudent or HiWi job in Germany.

You copy one instruction template, four skills and a tracker template into your own Claude Project. After about one hour you have an assistant that finds real postings, prepares each application, reminds you of follow-ups and drills you for interviews, and that never sends anything in your name.

Unofficial. Not affiliated with Anthropic. Not legal advice.
Maintained by Mirza Muhted Baig (github.com/baig1102).

**Status:** v0.1, tested November 2026, Germany only. What exactly was tested is listed in [docs/tested.md](docs/tested.md).

## What is in the kit

| Part | File | What it does |
|---|---|---|
| Project instructions | [project/project-instructions.template.md](project/project-instructions.template.md) | Your goal, limits, truth rules and document rules. You fill in the placeholders. |
| Watchlist | [project/watchlist.template.md](project/watchlist.template.md) | The company portals, university pages and commute times the scan uses. |
| Language wording | [project/language-level.template.md](project/language-level.template.md) | One honest standard sentence about your German, reused everywhere. |
| Skill: job-scan | [skills/job-scan](skills/job-scan/SKILL.md) | Finds new postings, checks that they are live, scores them, adds them to the tracker. |
| Skill: application-pack | [skills/application-pack](skills/application-pack/SKILL.md) | Builds the folder for one application: CV variant, certificates, a letter only when it is worth it, form answers, a claim-by-claim truth check. |
| Skill: job-followup | [skills/job-followup](skills/job-followup/SKILL.md) | Lists what is due, drafts follow-ups, closes silent applications, reports weekly numbers. |
| Skill: interview-prep | [skills/interview-prep](skills/interview-prep/SKILL.md) | One brief and one spoken drill per interview, at your language level. |
| Tracker | [tracker/](tracker/schema.md) | Three tables: jobs, tasks, contacts. As CSV files, or as a page Claude builds for you. |
| Scheduled tasks | [project/scheduled-tasks.md](project/scheduled-tasks.md) | Optional: a scan three times a week and a Saturday review. |
| Germany rules | [countries/de.md](countries/de.md) | Work limits for students, with official sources. |

## Quick start

The four skills are also attached as ready-to-upload ZIP files to each [release](https://github.com/baig1102/claude-werkstudent-kit/releases/latest).


Follow [docs/first-hour.md](docs/first-hour.md). Short version:

1. Create a Claude Project and paste the filled instruction template into its instructions.
2. Add your CVs, your certificates, the watchlist and the language wording to the project files.
3. Add the four skills.
4. Set up the tracker.
5. Turn on job alerts on the job sites you use, then say "scan jobs".

## Rules built into every file

- **You send, Claude drafts.** No skill applies, submits a form, sends an email, or signs in anywhere.
- **Only true claims.** Every sentence about you must come from your CV, a certificate, or something you said. Separate facts are never combined into a new claim.
- **Only live jobs.** Each posting gets a liveness level (`verified`, `live-recent`, `unverified`). No cover letter for an unverified job.
- **No scraping.** Claude does not search or browse LinkedIn or other sign-in sites. It reads job-alert emails you paste and single pages you open yourself. See [docs/privacy-and-safety.md](docs/privacy-and-safety.md).
- **Your work limit is a hard gate.** Postings above your weekly hours are skipped. Check your own limit in [countries/de.md](countries/de.md) and with your Ausländerbehörde.

## What it does not do

It does not find hidden jobs, guarantee interviews, or replace your International Office, your Ausländerbehörde or a lawyer. The default timings and scores come from one real search in autumn 2026. Change them when your own numbers say something else.

## Kurz auf Deutsch

Dieses Repository enthält eine fertige Vorlage für ein Claude-Projekt. Sie hilft internationalen Studierenden bei der Suche nach einer Werkstudenten- oder HiWi-Stelle in Deutschland.

- **Inhalt:** eine Vorlage für die Projektanweisungen, vier Skills (Stellensuche, Bewerbungsmappe, Nachfassen, Vorbereitung auf Vorstellungsgespräche) und eine Vorlage für die Bewerbungsübersicht.
- **Grundsätze:** Claude schreibt nur Entwürfe und verschickt nichts. Alle Angaben über Sie müssen stimmen und belegbar sein. Es werden nur Stellen vorgeschlagen, die aktuell ausgeschrieben sind.
- **Arbeitsrecht:** Die Regeln für Studierende aus Nicht-EU-Staaten stehen mit offiziellen Quellen in [countries/de.md](countries/de.md). Das ist keine Rechtsberatung. Verbindlich sind Ihr Aufenthaltstitel und die Auskunft Ihrer Ausländerbehörde.
- **Start:** [docs/first-hour.md](docs/first-hour.md) (auf Englisch).
- **Stand:** getestet im November 2026.

## Checking the kit

`python3 scripts/check_kit.py` checks the skill frontmatter, the tracker CSV columns against the schema, stray placeholders and relative links. It runs on every push. `python3 scripts/build_skill_zips.py` builds the skill ZIPs into `dist/`.

## Other countries

Version 0.1 covers Germany. The plan for one file per country is in [ROADMAP.md](ROADMAP.md). To add a country, read [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

MIT. See [LICENSE](LICENSE).
