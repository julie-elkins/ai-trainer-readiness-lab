# AI Trainer Readiness Lab

A public, provider-neutral course for designing, delivering, assessing, and
improving hands-on AI workshops.

The lab is built for learning and instruction leaders, technical enablement
practitioners, community trainers, and AI practitioners who need to teach more
than product features. Learners practice turning an AI capability into a
bounded workflow, checking the result, explaining the limitation, and teaching
the workflow to someone else.

This is an independent portfolio project. It is not an OpenAI product and is
not affiliated with or endorsed by OpenAI.

## Why this project

An AI workshop is not ready because the slides are finished. A trainer-ready
program needs:

- an audience and competency map;
- a hands-on task with a safe failure boundary;
- a positive and degraded demonstration;
- a visible assessment rubric;
- facilitator calibration;
- accessibility and responsible-use boundaries; and
- a revision loop based on learner evidence.

The lab makes those elements inspectable in one public package.

## Start here

Read the complete [GUIDE.md](GUIDE.md), then use the templates. The guide uses
the [course visual system](course/VISUAL-SYSTEM.md) so diagrams, emoji
signposts, and color cues carry consistent meanings.

1. [Learner worksheet](templates/learner-worksheet.md)
2. [Facilitator scorecard](templates/facilitator-scorecard.md)
3. [Workshop revision record](templates/workshop-revision-record.md)
4. [Learner feedback](templates/learner-feedback.md)
5. [Pilot protocol](docs/pilot-protocol.md)
6. [Pilot summary](templates/pilot-summary.md)
7. [Trainer subject-matter readiness checklist](templates/trainer-readiness-checklist.md)

Run the contract check from the repository root:

```bash
python3 scripts/check_course.py
```

The older [course guide path](course/COURSE_GUIDE.md) remains as a
compatibility link, but `GUIDE.md` is the single reading path and source for
the course text.

The required path is offline and synthetic. A live model, a product account,
network access, and provider credentials are not required.

## The capstone

Design and deliver a 60-minute workshop called **From AI output to verified
workflow**.

The capstone package must contain:

1. an audience and competency map;
2. a facilitator guide with timings and accessibility options;
3. a synthetic practice task;
4. a positive example and a degraded example;
5. a learner evidence worksheet;
6. a scoring rubric;
7. a five-minute teach-back;
8. a learner feedback form;
9. a revision record based on observed learner evidence and feedback themes;
10. a bounded pilot protocol and summary.

Another facilitator should be able to run the workshop without the author
present.

## Course boundaries

The course teaches transferable workflow judgment. ChatGPT, Codex, reusable
skills, and workspace agents can be used as optional product examples, but no
product feature is a hidden prerequisite.

The examples must remain synthetic. Do not add private learner records,
unpublished exam material, production traces, credentials, provider-private
prompts, or internal project identifiers.

## Pilot boundary

The [pilot protocol](docs/pilot-protocol.md) is a small first-delivery
procedure for finding course problems. It is not a validation study, a
credential trial, or evidence of learner transfer.

## Related public work

- [AI Teaching Strategies](https://github.com/julie-elkins/ai-teaching-strategies)
  provides reusable teaching and adoption strategies.
- [Agent Evaluation Learning Path](https://github.com/julie-elkins/agent-evaluation-learning-path)
  sequences the broader technical learning route.
- [Agent Assurance Harness](https://github.com/julie-elkins/agent-assurance-harness)
  provides metadata-only assurance controls for agent workflows.
- [Julie Elkins' portfolio](https://julie-elkins.github.io/)
  presents the projects and research narrative.

## Current first-party learning references

These are optional learning and product references for facilitators, not
prerequisites. The [complete learning map](GUIDE.md#-first-party-learning-map)
explains how to choose only the sources needed for a lesson.

- [OpenAI Academy](https://openai.com/academy)
- [Anthropic Academy](https://www.anthropic.com/learn)
- [Llama Learn](https://www.llama.com/learn/)
- [OpenAI prompting guide](https://platform.openai.com/docs/guides/prompting)
- [Anthropic prompt engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Llama documentation](https://www.llama.com/docs/)
- [OpenAI Academy workspace agents](https://openai.com/academy/workspace-agents/)
- [Codex changelog](https://developers.openai.com/codex/changelog?type=general)
- [Codex general availability announcement](https://openai.com/index/codex-now-generally-available)

Verify product documentation before each delivery because product capabilities
and names can change.

## Verification

The repository check verifies that the course guide, templates, safety
boundaries, and first-party reference links are present. It does not validate
learner outcomes, product quality, credential validity, or production safety.

## License

The course text and templates are licensed under the MIT License. See
[LICENSE](LICENSE).
