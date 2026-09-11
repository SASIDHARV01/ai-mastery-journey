# AI Mastery Journey

A sequential learning and GitHub proof-of-work repository based on the supplied **Complete AI Mastery Roadmap**. All nine phases remain in scope. The user's mentoring rules govern the journey; suggestions inside the PDF do not override them.

## Starting point

**Phase 0 → Math → Topic 1: Linear Algebra → Lesson 1: Vectors.**

Status: learning vectors. No lesson, quiz, or project has been completed. The learner knows basic Python and basic mathematics; Python data structures are not yet understood. Study time is 2 hours per day. The initial vectors answer is recorded; the lesson and runnable example are available, and five quiz answers are pending. The first 1–2 months are a study window, not a promise to master the entire roadmap.

## Repository layout

```text
ai-mastery-journey/
├── README.md
├── ROADMAP.md                    # Complete source inventory, in order
├── PROGRESS.md                   # Current lesson, review gates, next step
├── MENTORING.md                  # Agreed teaching and review protocol
├── daily-log.md                  # Dated work and actual push evidence
├── .gitignore
├── templates/
│   └── TOPIC.md                  # Copy when a lesson is unlocked
├── phase-00-foundations/
│   └── 01-linear-algebra/
│       └── 01-vectors/
│           ├── README.md        # Lesson and learning goals
│           ├── notes.md         # Explanation in the learner's own words
│           ├── quiz.md          # Questions, learner answers, review
│           ├── project/         # Learner-built code and run instructions
│           └── evidence/        # Outputs, observations, limitations
├── phase-01-classical-machine-learning/
├── phase-02-deep-learning-foundations/
├── phase-03-computer-vision/
├── phase-04-natural-language-processing/
├── phase-05-large-language-models-and-generative-ai/
├── phase-06-reinforcement-learning/
├── phase-07-mlops-and-production-ai/
└── phase-08-frontier-research-topics/
```

Later phase folders are placeholders. Their lessons are not unlocked. Add a lesson folder only when the preceding lesson passes its checks. Keep dependencies local to each project as they become necessary.

## GitHub proof of work

Account verified through the GitHub plugin: **SASIDHARV01**.

Repository: [SASIDHARV01/ai-mastery-journey](https://github.com/SASIDHARV01/ai-mastery-journey). Visibility: **public**, selected by the learner when creating it. Default branch: `main`.

The learner has authorized the mentor to commit and push the journey's proof of work. Each commit must describe actual work, and quiz/project completion still requires learner understanding and mentor review. Setup files are not a completed learning project.

To get a local copy, run this from the parent folder where you want the repository:

```bash
git clone https://github.com/SASIDHARV01/ai-mastery-journey.git
cd ai-mastery-journey
```

For an existing clone, run `git status` before `git pull --ff-only` and resolve any uncommitted changes deliberately. The mentor uses the GitHub plugin to publish reviewed work to this repository. `PROGRESS.md` and `daily-log.md` record verified setup and learning evidence.

## Every study day

Save meaningful progress: a prediction, corrected quiz answer, small implementation, observed output, or explanation. Update `daily-log.md`, inspect the changes, then commit and push. An unfinished project can have daily progress commits; it cannot be marked complete.

Example commit messages:

- Setup: `chore: scaffold AI mastery roadmap and progress tracking`
- First prediction: `docs(p00-vectors): record initial reasoning`
- Project work: `feat(p00-vectors): implement the agreed vector project`
- Correction: `fix(p00-vectors): correct the identified calculation error`
- Review: `docs(p00-vectors): record quiz corrections and project evidence`

Use a message that describes what actually changed. Record real commit links in the log after a successful push. The setup commit does not satisfy the vectors project requirement.

## Resume

At the beginning of a session, consult `PROGRESS.md`. Give a brief recap of the last completed lesson, or state that none is completed. If this conversation is unavailable, provide this repository and progress file in the next conversation. Do not assume completion from elapsed time or commit count.
