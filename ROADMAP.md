# Roadmap

## v0.1 (now): Germany
Everything works for a student in Germany. The country-specific rules already live in one file, `countries/de.md`.

## v0.2: country-neutral skills
Goal: a student in another country changes one line in the project instructions (`Country file: countries/xx.md`) and the same four skills work.

Changes:
1. **Move every Germany-only value out of the skills into the country file.** Today the skills still use German terms in examples (Werkstudent, Ausländerbehörde, "bereits besetzt"). In v0.2 they read these from the country file:
   - names of student job types and their search terms in the local language,
   - phrases that mean "posting closed",
   - phrases for language levels in postings (what counts as "above my level"),
   - the legal minimum wage, used for the pay score,
   - usual application documents (photo or no photo, cover letter customs, reference letters),
   - follow-up customs (email or phone, usual waiting time).
2. **A fixed structure for country files** (`countries/_template.md`), so skills can rely on section names.
3. **One "country check" step** at the top of each skill: read the country file named in the project instructions; if it is missing, stop and say so.

## v0.3: more countries
One file per country, written by people who study there. Candidates, in the order contributors appear: Austria, Netherlands, Ireland, United Kingdom, Canada, Australia. No rule for these countries is stated in this repository until a contributor provides official sources.

Each country file needs a maintainer and a "checked on" date. A file whose date is older than 12 months gets a warning banner at the top.

## v0.4: translations of the guides
The first-hour guide in German, and in other languages if contributors offer them. Skills stay in English; they already draft in the language of the posting.

## Not planned
- Automatic applying or form filling.
- Scraping or private-API access to any job site.
- Storing user data in this repository.
