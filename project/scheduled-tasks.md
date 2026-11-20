# Optional: scheduled tasks

Scheduled tasks need a Claude plan that offers them. Help: [Schedule recurring tasks](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork)

Nobody answers questions during a scheduled run, so both prompts are strict about what may be written. Replace the placeholders, and pick your own times.

## Task A: job scan, three times a week
Suggested schedule: Monday, Wednesday, Friday, early morning.

```
Run the job-scan skill as a scheduled run for my project "{{PROJECT_NAME}}". Nobody will answer questions. Use today's system date and state it in the first line. Tracker: {{TRACKER_LOCATION}}. Follow the skill exactly: today's source rotation, the 25-minute time box, at most 5 new jobs. Use only public career pages and university pages from watchlist.md. Do not open LinkedIn or any site that needs a sign-in. Write only new jobs with status open, or posted/notes on relisted jobs. Do not apply, sign in, message, save, follow or write letters. If the job-scan skill or the tracker is not available, stop and report that; do not improvise. End with at most 6 lines: date and sources covered; new jobs (score, company and role, liveness, link); possibly closed postings; tasks due today; sources not covered.
```

## Task B: weekly review
Suggested schedule: Saturday morning.

```
Run the job-followup skill as the weekly review for my project "{{PROJECT_NAME}}". Nobody will answer questions. Use today's system date and state it in the first line. Tracker: {{TRACKER_LOCATION}}. Draft only: no emails, calls or messages. Allowed tracker writes: closed "ghosted" under the day-21 rule, and new follow-up tasks. List every other clean-up as a proposal. If the job-followup skill or the tracker is not available, stop and report that. Output: the skill's report layout plus the weekly numbers against my weekly target.
```

## First run
Start Task A once by hand and read the result. Pass: it read the tracker, named the sources it covered, and wrote nothing except new `open` jobs. If it could not see the skill or the tracker, switch both tasks off and fix that first.

Job-alert emails are not part of scheduled runs. Paste them into a chat yourself and say "add these to the scan".
