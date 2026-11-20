# Contributing

Thank you for helping. Three kinds of contribution are welcome.

## 1. Corrections to a country file
Rules change. If a number or a link in `countries/` is out of date, open an issue or a pull request with:
- the sentence that is wrong,
- the official source that shows the current rule (law text, government or public-agency page),
- the date you checked it.

Blogs, relocation companies and forum posts are not accepted as sources for rules.

## 2. A new country file
Copy `countries/_template.md` to `countries/<two-letter-code>.md` and fill every section. Requirements:
- You study or have studied in that country, or you work in student advising there.
- Every rule has an official source and a "checked on" date.
- The file says "not legal advice" at the top.
- No personal stories that identify a person or an employer.

## 3. Improvements to skills and templates
Keep them general. A skill must not contain a city, a company list, a language level or any other personal value. Those belong in the user's project instructions or watchlist.

## Before you open a pull request
Run `python3 scripts/check_kit.py` from the repository root. It must print PASS. The same check runs automatically on every push and pull request.

## Never include
Personal data, real application documents, real tracker rows, employer-internal information, or code that scrapes job sites or calls their private APIs.
