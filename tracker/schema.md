# Tracker schema

Three tables. The skills depend on these names.

## jobs (one row per posting)
| Field | Type | Meaning |
|---|---|---|
| `id` | text | Short kebab-case, `company-topic`. Never changes. |
| `company`, `role` | text | As in the posting. |
| `location` | text | Town, on-site/hybrid/remote, commute and its source. |
| `link` | text | The company's own posting page when there is one. |
| `posted` | text | What the page says, or "undated". |
| `posted_date` | ISO date or empty | For age calculations. |
| `lang` | text | Language of the posting and the level it asks for. |
| `fit` | text | 2–3 factual sentences. Real scope only. |
| `cv` | text | Name of the CV variant to use. |
| `category` | `student-job` \| `small-job` | |
| `family` | text | Role family, for the weekly numbers. |
| `channel` | `portal` \| `alert` \| `agency` \| `university` \| `speculative` \| `direct` | How the application goes in. |
| `status` | `open` \| `applied` \| `interview` \| `offer` \| `rejected` \| `dropped` | |
| `closed` | empty \| `ghosted` | Set at day 21 without a reply. `status` stays. |
| `tier` | 1 \| 2 \| 3 | From the score. |
| `score`, `score_parts` | number, text | 0–100 and the six parts. |
| `live_status` | `verified` \| `live-recent` \| `unverified` | |
| `live_checked` | ISO date | Last liveness check. |
| `added`, `applied`, `first_reply` | ISO date or empty | |
| `letter` | true \| false \| empty | Was a cover letter sent. |
| `next` | text | The next action, or empty. |
| `notes`, `notes_rejection`, `interview_notes` | text | |

## tasks (one row per action with a date)
| Field | Type | Meaning |
|---|---|---|
| `id` | text | `t01`, `t02`, ... |
| `task` | text | What to do. |
| `due` | ISO date | |
| `status` | `open` \| `done` | |
| `refs` | text | Job ids, comma-separated. |
| `closed_note` | text | Why it was closed, if not obvious. |

## contacts (one row per person or office)
| Field | Type | Meaning |
|---|---|---|
| `id` | text | Short kebab-case. |
| `name`, `org` | text | |
| `email`, `phone` | text | Work contact details only. |
| `refs` | text | Job ids. |
| `notes` | text | |

## Rules
- The tracker is the single source of truth. Update it after every change.
- Nothing is deleted. Jobs end as `rejected`, `dropped`, or `closed: ghosted`.
- `applied` is set only after the user says the application was sent.
