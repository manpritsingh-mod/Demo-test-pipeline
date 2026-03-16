# Director-Level Speaking Guide — 12 Minutes Target

## ⏱️ Time Budget

| Slide | Title                    | Time        |
| ----- | ------------------------ | ----------- |
| 1     | Title / Intro            | 0:45        |
| 2     | About Me                 | 0:20        |
| 3     | Roadmap                  | 1:30        |
| 4     | Q1 — Foundation & POC 1  | 1:30        |
| 5     | Q1 — Architecture & Demo | 1:00        |
| 6     | Q2 — UnifiedCI Core      | 1:30        |
| 7     | Q2 — Architecture & Demo | 1:00        |
| 8     | Q3 — React + AI/ML       | 1:15        |
| 9     | Q3 — Architecture & Demo | 0:45        |
| 10    | Q4 — Mobile CI/CD + ML   | 1:30        |
| 11    | Q4 — Architecture & Docs | 1:00        |
| 12    | Thank You                | 0:45        |
|       | **Total**                | **~13 min** |

> [!TIP]
> This gives you ~2 min buffer for Q&A or pauses. If running long, cut slides 5 and 7 to 30 seconds each — just say _"Here's the architecture and live demo — I'll let you glance at it"_ and move on.

---

## Slide 1 — Title _(45 sec)_

> Good morning, everyone. Thank you for being here.
>
> I'm Manprit Singh — intern since May 2025 under Gautom-san, with Sunil-san as architect and Viresh-san as my mentor.
>
> Today I want to tell you the story of my year — how I went from learning the basics to building solutions that save time, bring standardization, and now use AI for smarter decisions.

**→** _"Quick bit about me..."_

---

## Slide 2 — About Me _(20 sec)_

> Quick intro — I'm from Jamshedpur, B.Tech in CS from Arka Jain University. My core interest is CI/CD automation and backend development. Outside work — drawing, travel, badminton.
>
> Let's get into the work.

**→** _"Here's the map of my year..."_

---

## Slide 3 — Roadmap _(1 min 30 sec)_

> Four chapters.
>
> **Q1** — Foundations. I learned Jenkins, Docker, Groovy, and delivered my first automation — a tool that cleans up old, forgotten pull requests.
>
> **Q2** — I saw a bigger problem. Every team was building their pipeline from scratch — same work, done differently. So I built **UnifiedCI** — one standard system for Java and Python.
>
> **Q3** — Extended UnifiedCI to React. And I started exploring: _what if CI could not just execute, but actually understand failures using AI?_
>
> **Q4** — Two things. An ML system that picks the right AWS machine size for builds. And Android CI/CD for mobile apps.
>
> The arc: **Learn. Build. Extend. Innovate.**

**→** _"Let me start with Q1..."_

---

## Slide 4 — Q1: Foundation & POC 1 _(1 min 30 sec)_

> When I joined, my mentor gave me a real problem.
>
> We had pull requests sitting idle across repositories. Old code. Dead branches. Nobody cleaning them up — because it's the kind of thing you always mean to do _next week_, and next week never comes.
>
> Small problem? Individually, yes. But repeated across dozens of repos, week after week — it adds up.
>
> So I built an automation. Every day, a Jenkins job wakes up, finds PRs inactive for over 30 days, labels them stale, closes them, and deletes the dead branches. Zero human involvement.
>
> But honestly, the biggest challenge wasn't the code. It was getting access — Linux desktop, GitHub, Docker, network approvals. Everything needed a process.
>
> That's where I learned — **technical skill is half the job. Communication, follow-ups, and patience are the other half.** That foundation helped me move much faster later.

**→** _"Let me show you how this works..."_

---

## Slide 5 — Q1: Architecture & Demo _(1 min)_

> Here's the system.
>
> Four steps — all automatic. **Daily trigger → Scan for inactive PRs → Label them stale → Close and delete.**
>
> On the right — the actual Jenkins pipeline running. Real runs. Each stage finishes in seconds. Entire cleanup takes under a minute per repo.
>
> Documentation and code are all on GitHub — linked at the bottom.
>
> Something that was manual and easily forgotten — now runs like clockwork, every day.

**→** _"That was a good start. But Q2 is where things got much bigger..."_

---

## Slide 6 — Q2: UnifiedCI Core _(1 min 30 sec)_

> After a few months, I noticed a pattern. Every team was building their CI/CD pipeline from scratch. Same goal — build, test, report — but everyone doing it differently.
>
> Imagine ten teams drawing their own maps to the same destination. Different routes. Different quality. And every new project — someone draws another map from scratch.
>
> So I built **UnifiedCI** — a shared library. One common template. A team just says _"I'm Java"_ or _"I'm Python"_ in one config file, and everything is ready — testing, building, code quality, reporting.
>
> **Result?** Setup went from days to hours. Pipeline code dropped. And every team now follows the same standard.
>
> This was also where I learned to **listen before building** — because if the solution doesn't match how teams actually work, the technical quality doesn't matter.
>
> Challenge-wise — Docker images piled up and killed our disk space. We had to optimize and eventually get a separate machine.

**→** _"Here's the architecture..."_

---

## Slide 7 — Q2: Architecture & Demo _(1 min)_

> Simple by design. A developer writes a small Jenkinsfile → it connects to the shared library → the library picks the right template — Java or Python — and handles everything automatically.
>
> On the right — a real build. Maven-based Java project, **build 27**, completed successfully in under two minutes.
>
> The key point — **teams don't need to understand the complexity underneath.** A few lines of config, and it just works. That's what a good platform does.

**→** _"Q2 was about standardization. Q3 is where things get more interesting..."_

---

## Slide 8 — Q3: React + AI/ML _(1 min 15 sec)_

> In Q3, I extended UnifiedCI to React. Java, Python, React — three technologies, one system.
>
> But the bigger story of Q3 is a question I started asking: **Can our CI system not just run things, but actually understand what went wrong?**
>
> Today, when a build fails, someone reads through hundreds of lines of logs. Time-consuming. Easy to miss things.
>
> What if the system could summarize the failure, suggest the cause, and recommend a fix?
>
> That's where I connected **GitHub Copilot to Jenkins** through **MCP — Model Context Protocol** — letting an AI model read build logs and provide intelligent feedback.
>
> It's not just automation anymore. It's **intelligent automation.**
>
> Challenges were different — getting Copilot access, AI tool approvals, environment setup.

**→** _"Let me show you the architecture..."_

---

## Slide 9 — Q3: Architecture & Demo _(45 sec)_

> Two things here.
>
> **Left** — React pipeline. Same pattern. Jenkinsfile → shared library → React template. Standardized.
>
> **Right** — the AI piece. LLM talks to MCP, MCP connects to Jenkins. AI can pull build data and analyze logs. Still in exploration, but early results are promising.
>
> Bottom — React pipeline running live in Jenkins. All stages visible.
>
> By end of Q3 — **three tech stacks covered, and AI entering our CI/CD process.**

**→** _"Now, Q4 — the current quarter..."_

---

## Slide 10 — Q4: Mobile CI/CD + ML _(1 min 30 sec)_

> Two things I'm building now.
>
> **First — ML-powered AWS node selection.**
>
> Simple problem: teams pick AWS machines by guessing. Too big = wasted money. Too small = slow builds. What if we looked at past build data — actual CPU, actual memory usage — and recommended the right machine?
>
> **Right resource. Right time. No waste.**
>
> A small saving per build × thousands of builds = real money saved. The training dataset is ready and the prediction model is in progress.
>
> **Second — Android CI/CD.**
>
> Developer pushes code → everything happens automatically. Build, test, package, deploy. Docker environment is ready, pipeline is working, Nexus deployment is in progress.
>
> This quarter required the most independent decision-making. No fixed playbook. I had to define the approach, experiment, and manage timelines myself.

**→** _"Let me show you both architectures..."_

---

## Slide 11 — Q4: Architecture & Docs _(1 min)_

> **Left — Mobile CI/CD.** Developer pushes code → Jenkins spins up a Docker container → builds the app, runs tests, deploys to an Android emulator. Everything containerized — same environment every time. Consistent and reliable.
>
> **Right — ML Node Selection.** Build starts → system checks the project's history → recommends the right machine — from 2 GB small to 32 GB extra-large. Right fit, automatically chosen.
>
> Both repos and documentation linked at the bottom.
>
> What excites me — **one expands into mobile, the other brings intelligence into infrastructure.**

**→** _"So let me bring it all together..."_

---

## Slide 12 — Thank You _(45 sec)_

> When I started, my focus was learning tools — _How does Jenkins work? What is Docker?_
>
> Now, my focus is solving problems — _How do we stop repeated work? How do we spend less on cloud machines?_
>
> Four quarters: cleanup automation → shared library for the org → AI-assisted CI/CD → intelligent infrastructure and mobile deployment.
>
> **From learning tools to solving problems.**
>
> I want to keep building systems that are not just automated — but intelligent, scalable, and impactful.
>
> Thank you. Happy to take your questions.

---

## 🚨 Emergency Cuts (If Running Over 13 Min)

| Cut This                                                                                     | Saves  |
| -------------------------------------------------------------------------------------------- | ------ |
| Skip slide 2 entirely — just say _"Quick intro on the slide"_                                | 20 sec |
| On slides 5 & 7, just say _"Here's the architecture and live proof — take a moment to look"_ | 1 min  |
| Drop the challenges/disk-space story from slide 6                                            | 15 sec |
| Shorten slide 12 — just say the last 3 lines                                                 | 20 sec |
