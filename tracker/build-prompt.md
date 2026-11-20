# Build prompt for a tracker page (experimental)

Paste the text below into a chat in your project. It works only if your Claude plan can create pages that keep data between visits. If Claude says it cannot, use the CSV files.

```
Build me a job-search tracker as a page that keeps its data between visits.

Data: three collections named jobs, tasks and contacts, with exactly the fields in the project file tracker/schema.md (I paste it below if you cannot see it).

Views:
1. Jobs: a table grouped by status (open, applied, interview, offer, rejected, dropped), sorted by tier and then score. Each row shows company, role, location, score, liveness level, posted date, next action, and the link. Rows with closed = ghosted are greyed out.
2. Tasks: open tasks sorted by due date; overdue tasks marked.
3. Contacts: a simple list.
4. Numbers: applications per week, replies, interviews, median days to first reply.

Rules: I can edit status, next and notes on the page. Nothing can be deleted. No data leaves the page. Start with an empty tracker.

When it is built, tell me the link, and show me how you will read and write the three collections in later chats.
```

Then put the link into your project instructions at `{{TRACKER_LOCATION}}`.
