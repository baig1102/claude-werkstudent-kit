# What was tested

"Tested November 2026" means the following, and nothing more.

| Part | Used in a real job search (Oct–Nov 2026, personal version) | Generalised file from this repo smoke-tested | Date | Notes |
|---|---|---|---|---|
| Project instructions | yes | yes | 2026-11-20 | Filled with an invented student ("Musterstadt") and used for the two skill tests below. |
| Tracker with jobs / tasks / contacts | yes (page with storage) | yes | 2026-11-20 | CSV variant: all three files were read correctly by job-followup. |
| Tracker build prompt | no | not tested | | experimental |
| job-scan | yes | partly | 2026-11-20 | Did not open LinkedIn and reported an empty run honestly. The real career pages tried showed no readable postings (JavaScript-loaded or blocked), so the liveness check on a real job was not exercised. |
| application-pack | yes | not tested | | |
| job-followup | yes | yes | 2026-11-20 | Weekly review read the CSV rows, applied the day-21 rule to the example job (it is dated January 2026, so it shows as ghosted rather than due), proposed the task clean-up, sent nothing. |
| interview-prep | yes | not tested | | |
| Scheduled tasks | not tested | not tested | | |
| Links in countries/de.md | n/a | yes | 2026-11-20 | All 7 source links and the 4 help-centre links in docs/first-hour.md and project/scheduled-tasks.md loaded. |

Tested with Claude (Projects, skills, scheduled tasks) as available in November 2026. Features and menu names change. If something does not work, open an issue and say which step failed.
