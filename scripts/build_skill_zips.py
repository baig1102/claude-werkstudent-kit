#!/usr/bin/env python3
"""Build one upload-ready ZIP per skill.

Run from the repository root:  python3 scripts/build_skill_zips.py
Output: dist/<skill-name>.zip, with the skill folder as the root of each ZIP
(the layout Claude expects when you upload a custom skill).
"""
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"


def main():
    DIST.mkdir(exist_ok=True)
    for skill in sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir()):
        out = DIST / f"{skill.name}.zip"
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(skill.rglob("*")):
                if f.is_file():
                    z.write(f, f.relative_to(skill.parent).as_posix())
        print(out.relative_to(ROOT))


if __name__ == "__main__":
    main()
