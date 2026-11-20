# Your first hour

You need: a Claude account, your CV (one file is enough to start), your enrolment certificate, and your residence permit in front of you if you are from a non-EU country.

Menu names in Claude change over time. If a name below does not match what you see, use the linked help article.

## Minute 0–10: create the project
1. Create a new Project in Claude and name it, for example, "Job Search".
   Help: [How can I create and manage projects?](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)
2. Open `project/project-instructions.template.md` from this kit. Copy all of it into the project's instructions field.

**Checkpoint:** the project page shows your instructions, still with `{{PLACEHOLDERS}}`.

## Minute 10–25: fill the placeholders
Replace every `{{...}}` in the instructions. The important ones:

| Placeholder | What to write | Example |
|---|---|---|
| `{{CITY}}`, `{{REGION_CITIES}}` | Where you live and which towns you would commute to | "Musterstadt; also A-Stadt, B-Stadt" |
| `{{MAX_COMMUTE}}` | Longest door-to-door commute, one way | "90 minutes" |
| `{{STUDY_PROGRAMME}}`, `{{UNIVERSITY}}` | As on your enrolment certificate | "Mechanical Engineering B.Eng." |
| `{{PERMIT_HOURS}}` | Your weekly limit in the lecture period, all jobs together | "20" |
| `{{GERMAN_LEVEL}}` | The level on your certificate, not the level you hope for | "B1" |
| `{{CV_VARIANTS}}` | One line per CV version and when to use it | "Technical: engineering roles" |
| `{{REAL_SCOPE}}` | The honest size of each skill | "Python: two university projects" |

For `{{PERMIT_HOURS}}`, read [countries/de.md](../countries/de.md) first and compare it with the text on your residence permit and its supplementary sheet (Zusatzblatt). If the two differ, your permit and your Ausländerbehörde decide.

**Checkpoint:** search the instructions for `{{`. There must be no result.

## Minute 25–35: add your files
Add to the project files:
- your CV or CVs (the current versions only),
- your certificates (enrolment, language certificate, references),
- `project/watchlist.template.md`, renamed to `watchlist.md`, with at least five company career pages and your university's job page,
- `project/language-level.template.md`, renamed to `language-level.md`, filled in.

**Checkpoint:** in a new chat in the project, ask: "Which CV variants do I have and what is my weekly hour limit?" The answer must match what you wrote.

## Minute 35–45: add the skills
For each folder in `skills/`: make a ZIP file of the folder (the folder itself must be the root of the ZIP) and upload it as a skill in Claude.
Help: [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) and [How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)

If you cannot upload skills on your plan, keep the four `SKILL.md` files in the project files instead and say "follow job-scan" and so on. It works the same way, a little slower.

**Checkpoint:** your skill list shows `job-scan`, `application-pack`, `job-followup` and `interview-prep`, all switched on.

## Minute 45–52: set up the tracker
Choose one:
- **Simple (works everywhere):** add `tracker/jobs.csv`, `tracker/tasks.csv` and `tracker/contacts.csv` to the project files. Delete the example rows later. Claude returns updated files after each change, and you replace the old ones.
- **Page (experimental):** paste `tracker/build-prompt.md` into a chat in the project. Claude builds a tracker page. Put its link into the instructions at `{{TRACKER_LOCATION}}`.

**Checkpoint:** ask "Read the tracker and tell me how many jobs it holds." You should get "1" (the example row).

## Minute 52–60: first scan
1. On the job sites you use (for example LinkedIn, your university job portal, the Bundesagentur für Arbeit Jobbörse), create job alerts yourself for your search terms and towns. The emails come to you. Claude never signs in to these sites.
2. In the project, say: **"scan jobs"**.
3. If an alert email has arrived, paste its text into the chat and say: "add these to the scan".

**Checkpoint:** the report lists each job with a score, a liveness level, a link and a posting date, and the new jobs are in the tracker with status `open`.

## After the first hour
- "make the pack for <job id>" builds one application.
- "what's due?" lists follow-ups.
- "prep me for <company>" starts interview practice.
- Optional: set up the two scheduled tasks in [project/scheduled-tasks.md](../project/scheduled-tasks.md).
- Once a week, read the numbers in the weekly review and change one thing.
