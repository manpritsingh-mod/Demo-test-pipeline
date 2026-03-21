# Final Speaking Content Review

## Verdict: ⚠️ ~85% There — NOT 100% Yet

The story and structure are strong. But there are **grammar mistakes, typos, incomplete sentences, and a few places where storytelling breaks**. A director will notice if you stumble on these. Here's everything, slide by slide.

---

## ❌ Issues Found (Must Fix)

### Slide 1
| Your Text | Problem | Fix |
|---|---|---|
| *"will saves time"* | Grammar | **"save time"** |
| *"AI/ML for smarter decisions-making"* | Wrong word | **"decision-making"** |

### Slide 3
| Your Text | Problem | Fix |
|---|---|---|
| *"focused on learning"* | Missing "I" | **"I focused on learning"** |
| *"AI/ML solution can help"* | Awkward | **"AI/ML can help"** |

### Slide 4
| Your Text | Problem | Fix |
|---|---|---|
| *"had assign ne the work"* | Typo + grammar | **"assigned me a problem to work on"** |
| *"So built an automation"* | Missing "I" | **"So I built an automation"** |
| *"helped me nove faster"* | Typo | **"helped me move faster"** |

### Slide 6
| Your Text | Problem | Fix |
|---|---|---|
| *"Imagine ten teams scratch. drawing their own maps"* | Broken sentence | **"Imagine ten teams drawing their own maps to the same destination from scratch"** |
| *"in ane config file"* | Typo | **"in one config file"** |

### Slide 7
| Your Text | Problem | Fix |
|---|---|---|
| *"the deno video"* | Typo | **"the demo video"** |
| *"in under a minutes"* | Grammar | **"in under two minutes"** |

### Slide 8
| Your Text | Problem | Fix |
|---|---|---|
| *"extended UnifiedCI"* | Missing "I" | **"I extended UnifiedCI"** |
| *"the systes could"* | Typo | **"the system could"** |
| *"intelligerit feedback"* | Typo | **"intelligent feedback"** |

### Slide 10
| Your Text | Problem | Fix |
|---|---|---|
| *"I'm worked on two things"* | Grammar | **"I'm working on two things"** |
| *"the process Mwork"* | Typo | **"the ML work"** |
| *"real AMS usage data"* | Typo | **"real AWS usage data"** |
| *"has been a"* | Incomplete sentence | **"has been a process"** or **"has been challenging"** |

---

## ⚠️ Storytelling Breaks (Should Fix)

### Problem 1: Slides 5, 7, 9, 11 sound like bullet points, not a story

Your content slides (4, 6, 8, 10) tell a great story. But the architecture slides (5, 7, 9, 11) suddenly switch to a list-reading tone. Directors will feel the energy drop.

**Example — Slide 5 (current):**
> "Four steps all automatic. Daily trigger Scan for inactive PRs Label them stale Close and delete."

This reads like notes, not speech. **Fix:**
> "It works in four simple steps — every day, a Jenkins job wakes up automatically. It scans all open pull requests, finds the ones inactive for over 30 days, labels them as stale, and then closes them and deletes the dead branches."

**Example — Slide 9 (current):**
> "React pipeline. Same pattern. Jenkinsfile shared library React template. Standardized."

Too choppy. **Fix:**
> "On the left, the React pipeline — it follows the same pattern we built before. Jenkinsfile connects to the shared library, and now there's a React template alongside Java and Python. Standardized."

### Problem 2: Some transitions are missing

Between slides 1→2, 2→3, you don't have transition lines. The story needs connectors.

| After Slide | Add This Transition |
|---|---|
| 1 → 2 | *"But first, a quick bit about me..."* |
| 2 → 3 | *"Now, let me show you where this year has taken me..."* |
| 7 → 8 | *"Q2 was about standardization. Q3 is where things got more interesting..."* |
| 9 → 10 | *"And that brings us to the current quarter..."* |
| 11 → 12 | *"So, let me bring it all together..."* |

---

## ⚠️ Grandmother Test — Technical Words to Explain Better

Your manager said "explain like to your grandmother." These terms need one extra line of explanation:

| Term You Used | A Director Might Think... | Add This Explanation |
|---|---|---|
| **MCP** | "What is that?" | You already say "Model Context Protocol" ✅ but add: *"It's basically a bridge that lets AI talk to Jenkins"* |
| **Docker container** (Slide 11) | "Container?" | Add: *"a clean, isolated environment — like a fresh computer every time"* |
| **Nexus repository** | Not mentioned in speech ✅ | Good — you skipped this. Keep it that way |
| **Jenkinsfile** (Slides 7, 9) | "What file?" | Add once: *"a small configuration file that tells Jenkins what to do"* |
| **PR / Pull Request** (Slide 4) | May not know | First mention, add: *"pull requests — which are basically proposed code changes waiting for review"* |

---

## ✅ What's Working Great

| Aspect | Why It Works |
|---|---|
| **"Learn. Build. Extend. Innovate."** | Memorable. Directors will remember this |
| **Map analogy** (Slide 6) | Perfect for non-technical audience |
| **"Can our CI system... actually understand?"** (Slide 8) | Creates curiosity. Storytelling gold |
| **"Right resource. Right time. No waste."** (Slide 10) | Punchy. CFO-level language |
| **Access challenges honesty** (Slide 4) | Shows maturity. Directors love this |
| **"Listen before building"** (Slide 6) | Shows you understand real-world work |
| **"From learning tools to solving problems"** (Slide 12) | Perfect arc. Strong closing |

---

## 🔧 Corrected Final Script (with Transitions + Simple Explanations)

Below is your **complete, ready-to-speak script** with all three things baked in:
- ✅ Grammar/typo fixes
- ✅ **Transition lines** between every slide (marked with ↓)
- ✅ **Grandmother-test explanations** for technical terms (marked with 👵)

---

### Slide 1 — Title
> Good morning, I'm Manprit Singh, intern here since May 2025 under Gautom-san, working closely with Sunil-san and Viresh as my mentor.
>
> Over the past few months, my journey has been from learning the fundamentals to building solutions that **save** time, bring standardization, and even exploring AI/ML for smarter **decision-making**.
>
> Let me walk you through my journey.

**↓** *"But first, a quick bit about me..."*

---

### Slide 2 — About Me
> Quick intro — I come from Jamshedpur, Jharkhand and completed my B.Tech in Computer Science from Arka Jain University.
>
> My core interest is in CI/CD automation and backend development — Java, Spring Boot.
>
> Outside work, I enjoy sketching, travel, and playing badminton.

**↓** *"Now, let me show you where this year has taken me..."*

---

### Slide 3 — Roadmap
> Here's a high-level view of my one-year journey, structured across four quarters.
>
> In Q1, I focused on learning the fundamentals and delivered my first proof of concept.
>
> In Q2, I moved towards solving a larger problem — standardizing CI/CD through UnifiedCI.
>
> Q3 was about extending UnifiedCI to React projects and exploring how AI/ML can help in CI/CD.
>
> And in Q4, I focused on innovation — ML-based node selection and mobile CI/CD.
>
> So the journey has been — learn, build, extend, and now innovate.

**↓** *"Let me start from the beginning — Q1..."*

---

### Slide 4 — Q1: Foundation & POC 1
> When I joined, my mentor assigned me a problem to work on.
>
> We had pull requests — 👵 *which are basically proposed code changes waiting for review* — sitting idle across repositories. Old code. Dead branches. Nobody cleaning them up. Small problem? Individually, yes. But repeated across dozens of repos, week after week — it adds up.
>
> So I built an automation where every day, a Jenkins job wakes up, finds PRs inactive for over 30 days, labels them stale, closes them, and deletes the dead branches.
>
> Zero human involvement.
>
> But honestly, the biggest challenge wasn't technical. It was getting access — Linux desktop, GitHub, Docker, network approvals. Everything needed a process.
>
> This phase taught me something important — technical knowledge is only one part of the work. Communication, follow-ups, and patience matter equally. And that foundation helped me move faster.

**↓** *"Let me show you how this actually works..."*

---

### Slide 5 — Q1: Architecture & Demo
> Here's the system I just described.
>
> It works in four simple steps — all automatic. Every day, a Jenkins job triggers on its own, scans every open pull request, finds the ones inactive for over 30 days, labels them as stale, and then closes them and deletes the dead branches.
>
> And here is the video demo — the actual Jenkins pipeline running. These are real runs. Each stage finishes in seconds. The entire cleanup takes under a minute per repo.
>
> Documentation and code are all on GitHub.
>
> In short — something that was manual and easily forgotten now runs like clockwork, every single day.

**↓** *"That was a good start. But in Q2, I noticed a much bigger problem..."*

---

### Slide 6 — Q2: UnifiedCI Core
> After a few months, we noticed a pattern. Every team was building their CI/CD pipeline from scratch. Same goal — build, test, report — but everyone doing it differently.
>
> Imagine ten teams drawing their own maps to the same destination from scratch. Different routes. Different quality. And every new project — someone draws another map.
>
> So I built UnifiedCI — a shared library. 👵 *Think of it as a common template that any team can reuse.* A team just mentions the specification of their project — "Java" or "Python" — in one config file, and everything is ready — testing, building, code quality checks, reporting.
>
> Result? Setup went from days to hours. Pipeline code dropped. And every team now follows the same standard.
>
> This was also where I learned to listen before building — it taught me an important lesson: understanding user needs is as important as building the solution itself.
>
> Challenge-wise — Docker images piled up and killed our disk space. We had to optimize and eventually get a separate machine.

**↓** *"Let me show you the architecture..."*

---

### Slide 7 — Q2: Architecture & Demo
> Here's the architecture — and I kept it simple by design.
>
> A developer writes a small Jenkinsfile — 👵 *which is just a small configuration file that tells Jenkins what to do* — it connects to our shared library, the library picks the right template — Java or Python — and handles everything automatically.
>
> On the other hand, here is the demo video — a real build. Java project, completed successfully in under two minutes.
>
> The key point — teams don't need to understand the complexity underneath. A few lines of configuration, and it just works.

**↓** *"Q2 was about standardization. Q3 is where things got more interesting..."*

---

### Slide 8 — Q3: React + AI/ML
> In Q3, I extended UnifiedCI to support React projects. Now we have React, Java, Python — three technologies, one system.
>
> But the bigger story of Q3 is a question I started asking: Can our CI system not just run things, but actually understand what went wrong?
>
> Today, when a build fails, someone reads through hundreds — sometimes thousands — of lines of logs. Time-consuming. Easy to miss things.
>
> What if the system could summarize the failure, suggest the cause, and recommend a fix?
>
> That's where I connected GitHub Copilot to Jenkins through MCP — Model Context Protocol. 👵 *Think of MCP as a bridge — it lets an AI model talk to Jenkins, read the build logs, and provide intelligent feedback to the developer.*
>
> It's not just automation anymore. It's intelligent automation.
>
> Challenges were different — getting Copilot access, AI tool approvals, environment setup.

**↓** *"Let me show you the architecture..."*

---

### Slide 9 — Q3: Architecture & Demo
> Two things here.
>
> On the left — the React pipeline. It follows the same pattern I built before. Jenkinsfile connects to the shared library, and now there's a React template alongside Java and Python. Standardized.
>
> On the right — the AI piece. 👵 *An AI model — called an LLM, a large language model — talks to MCP, and MCP connects to Jenkins.* This lets the AI pull build data and analyze logs. It's still in exploration, but early results are promising.
>
> And here is the demo — the React pipeline running live in Jenkins. All stages visible.
>
> By end of Q3 — three tech stacks covered, and AI entering our CI/CD process.

**↓** *"And that brings us to the current quarter..."*

---

### Slide 10 — Q4: Mobile CI/CD + ML
> In the current quarter, I'm working on two things.
>
> First — and something I'm personally very excited about.
>
> The problem: teams pick AWS machines — 👵 *these are computers in the cloud that run our builds* — by guessing. Too big — wasted money. Too small — slow builds or build failure. What if we looked at past build data — actual CPU, actual memory usage — and predicted the right machine automatically?
>
> The idea is simple: Right resource. Right time. No waste.
>
> Even a small optimization per build, repeated across thousands of builds, can create real savings.
>
> Second — mobile CI/CD. My goal is simple — a developer pushes code, and everything else happens automatically. Build. Test. Package. Deploy.
>
> Challenges — Play Store requires credentials and signing certificates, which need approvals. For the ML work, getting access to real AWS usage data has been challenging.

**↓** *"Let me show you both architectures..."*

---

### Slide 11 — Q4: Architecture & Docs
> On the left — Mobile CI/CD. A developer pushes code, Jenkins spins up a Docker container — 👵 *think of it as a clean, isolated environment, like a fresh computer every time* — builds the app, runs tests, and deploys to an Android emulator. Consistent and reliable.
>
> On the right — ML Node Selection. When a build starts, the system checks the project's past history, and predicts the right machine — from 2 GB small to 32 GB extra-large. The right fit, automatically chosen.
>
> What excites me — one expands into mobile, the other brings intelligence into infrastructure.

**↓** *"So, let me bring it all together..."*

---

### Slide 12 — Thank You
> When I started, my focus was learning different tools — how does Jenkins work? What is Docker?
>
> Now, my focus is solving problems — how do we stop repeated work? How do we spend less on cloud machines?
>
> From cleanup automation... to a shared library for the org... to AI-assisted CI/CD... to intelligent infrastructure and mobile deployment.
>
> From learning tools — to solving problems.
>
> I want to keep building systems that are not just automated — but intelligent, scalable, and impactful.
>
> Thank you. Happy to take your questions.
