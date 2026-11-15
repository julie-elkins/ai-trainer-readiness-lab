"""Check the public course contract.

Design rules:
1. Keep the required course path readable from a clean checkout.
2. Require explicit learner evidence and claim boundaries.
3. Keep the public package synthetic and provider-neutral.
"""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    Path("README.md"),
    Path("GUIDE.md"),
    Path("course/VISUAL-SYSTEM.md"),
    Path("course/COURSE_GUIDE.md"),
    Path("templates/learner-worksheet.md"),
    Path("templates/learner-feedback.md"),
    Path("templates/facilitator-scorecard.md"),
    Path("templates/workshop-revision-record.md"),
)

REQUIRED_PHRASES = {
    Path("README.md"): (
        "provider-neutral",
        "AI Teaching Strategies",
        "GUIDE.md",
        "python3 scripts/check_course.py",
    ),
    Path("GUIDE.md"): (
        "```mermaid",
        "## 🎯 Purpose",
        "Learning objectives",
        "Synthetic scenario",
        "Assessment rule",
        "Accessibility and responsible use",
        "learner feedback",
        "What this proves and does not prove",
    ),
    Path("course/VISUAL-SYSTEM.md"): (
        "Palette",
        "Diagram conventions",
        "Emoji legend",
    ),
    Path("course/COURSE_GUIDE.md"): (
        "complete course is maintained",
        "GUIDE.md",
    ),
    Path("templates/facilitator-scorecard.md"): (
        "Evidence note",
        "Prototype threshold",
        "not a certification decision",
    ),
    Path("templates/learner-feedback.md"): (
        "Confidence before and after",
        "It is not a grade",
        "Feedback describes learner experience",
        "Do not include your name",
    ),
}

FORBIDDEN_MARKERS = (
    "OPENAI_API_KEY",
    "ANTHROPIC_API_KEY",
    "sk-",
)


def main() -> int:
    failures = []

    for relative_path in REQUIRED_FILES:
        path = ROOT / relative_path
        if not path.is_file():
            failures.append(f"missing file: {relative_path}")
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in REQUIRED_PHRASES.get(relative_path, ()):
            if phrase not in text:
                failures.append(f"{relative_path}: missing phrase: {phrase}")
        for marker in FORBIDDEN_MARKERS:
            if marker in text:
                failures.append(f"{relative_path}: forbidden marker: {marker}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print(f"PASS: checked {len(REQUIRED_FILES)} course files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
