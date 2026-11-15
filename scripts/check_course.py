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
    Path("docs/pilot-protocol.md"),
    Path("templates/learner-worksheet.md"),
    Path("templates/learner-feedback.md"),
    Path("templates/facilitator-scorecard.md"),
    Path("templates/workshop-revision-record.md"),
    Path("templates/pilot-summary.md"),
    Path("templates/trainer-readiness-checklist.md"),
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
        "bounded pilot",
        "subject-matter readiness",
        "Trainer note",
        "[!TIP]",
        "never stop learning",
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
    Path("docs/pilot-protocol.md"): (
        "one to three learners",
        "Performance evidence",
        "Experience evidence",
        "Delivery evidence",
        "Interpretation boundary",
    ),
    Path("templates/pilot-summary.md"): (
        "## Performance evidence",
        "## Experience evidence",
        "## Comparison",
        "## Boundary",
    ),
    Path("templates/trainer-readiness-checklist.md"): (
        "Define the teaching boundary",
        "Build a first-party source pack",
        "Map capability to evidence",
        "Make the readiness decision",
        "🔒 Internal course library (private, if approved)",
        "Trainer mindset and support",
        "[!TIP]",
        "Previously recorded classes (private, if approved)",
        "Office hours (private, if approved)",
        "Trainer dry runs (private or synthetic)",
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
