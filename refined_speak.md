# Final Speaking Script — Short + Storytelling (10 min)

---

### Slide 1 ⏱️ 30s

> Good morning, I'm Manprit Singh, intern since May 2025 under Gautom-san, working with Sunil-san and Viresh as my mentor. This year I went from learning the basics to building real solutions — let me take you through that journey.

---

### Slide 2 ⏱️ 30s

> Quick about me — from Jamshedpur, B.Tech in CS. Into CI/CD and backend work. Outside work — sketching, travel, badminton. Now let me show you where this year took me...

---

### Slide 3 ⏱️ 40s

> I've split my year into four quarters, each building on the last. Started with basics in Q1, then built a shared library in Q2, extended it and explored AI in Q3, and now in Q4 — mobile CI/CD, ML, and a hackathon. So it's been — learn, build, extend, innovate. Let me start from Q1...

---

### Slide 4 — Q1 ⏱️ 1m 20s

> So when I joined, there were lots of stale PRs piling up across repos — old code sitting there for months, nobody cleaning them up. Going through each repo manually was a real headache. So I built an automation that goes through every repo daily, figures out which ones have been sitting too long, and cleans them out — no human effort.
>
> Along the way I picked up Jenkins, Docker, Groovy, Python. But honestly, the bigger learning was how corporate environments work.
>
> Challenges were mostly around access — Linux desktop, GitHub, Docker, SWAN2 network, Slack tokens. Five different approvals at once. So instead of waiting one by one, I raised them all together and followed up on each regularly. By the time one came through, the others were already moving. That approach saved me weeks. Let me show you how it looks...

---

### Slide 5 — Q1 Demo ⏱️ 40s

> So here it is — four steps, all automatic. Triggers daily, scans PRs, labels the stale ones, closes and cleans up. This is a real Jenkins run — each stage takes seconds. What used to be manual and forgotten now runs on its own every day. That was a good start — but in Q2, I noticed something bigger...

---

### Slide 6 — Q2 ⏱️ 1m 20s

> So every team was setting up their CI/CD pipeline from scratch — same thing over and over, but each one doing it differently. I wanted to fix that once and for all.
>
> So I built UnifiedCI — a shared library that works across Java and Python. Now a team just puts their project type in a small config, and everything runs — build, test, quality checks. Setup that took days now takes hours, and pipeline code dropped by 95%.
>
> This quarter taught me something important — listen before you build. I initially designed it based on my assumptions, and when teams gave feedback, I had to rework parts. After that, I always talked to users first. Technically — shared library design, testing tools, Nexus integration.
>
> Challenges — GitHub access, tool installations, Linux setup. But the big one was disk space. Docker images were piling up quietly after every build, and one morning the disk was completely full — builds just stopped. So I wrote cleanup scripts that run after every build and set up a weekly deep cleanup. Eventually got a dedicated machine, and the problem was gone for good. Let me show you the architecture...

---

### Slide 7 — Q2 Demo ⏱️ 40s

> Simple design — developer writes a small config, it connects to our shared library, library picks the right template and handles everything. Here's a real Java build — done in under two minutes. Few lines of config, and it just works. Now Q3 is where things got interesting...

---

### Slide 8 — Q3 ⏱️ 1m 20s

> So I extended UnifiedCI to React — three languages, one system now. But the bigger question I started asking was — what if our CI system could actually understand what went wrong when a build fails? Instead of someone reading thousands of log lines manually?
>
> That's when I connected Copilot to Jenkins through MCP — think of it as a bridge that lets AI read build logs and give smart feedback. So now it's not just automation — it's intelligent automation.
>
> Technically, I learned the React tooling and how AI models plug into CI/CD. But the real shift was in my thinking — I went from just doing tasks to asking "how can this be better?"
>
> Challenges — Copilot access, AI tool permissions. But the painful one was my desktop ran out of space completely — Node modules from React are huge, plus Docker on top of that. While the new desktop provisioning was in process, I did aggressive cleanups and kept working with what I had. Sometimes you just have to make it work with limited resources. Let me show you the setup...

---

### Slide 9 — Q3 Demo ⏱️ 40s

> Left side — React pipeline, same pattern as Java and Python, all standardized. Right side — AI model connecting to Jenkins through MCP, analyzing build logs. Here's the live React build. By end of Q3 — three tech stacks done, and AI entering our CI/CD. Now the current quarter...

---

### Slide 10 — Q4 ⏱️ 1m 20s

> This quarter I took on two projects and a hackathon. First — teams pick AWS machines by guessing. Too big, money wasted. Too small, builds slow down. So I'm building an ML model that looks at past build data and predicts the right machine. Right resource, right time, no waste.
>
> Second — mobile CI/CD for Android. Push code, everything runs automatically.
>
> And I also joined an internal hackathon — Self-Healing CI/CD with Agentic AI. The idea — when a build fails, the system tries to fix it on its own. Submitted on time.
>
> Running three things at once taught me how to prioritize — that was the biggest growth this quarter.
>
> Challenges — AWS access, Play Store credentials, physical devices for testing. But the interesting one was the ML data problem. I needed real AWS usage data to train the model, but that access takes time. So instead of waiting, I generated a synthetic dataset and built the entire pipeline end-to-end — training, prediction, API serving — everything works. Once real data comes in, I just swap it in. The systems are built and ready, the access is coming through. Let me show you both...

---

### Slide 11 — Q4 Demo ⏱️ 40s

> Mobile side — code push, Docker builds it in a clean environment, tests, deploys to emulator. ML side — build starts, system checks history, picks the right machine from 2GB to 32GB. Smart and automatic. So let me wrap up...

---

### Slide 12 — Thank You ⏱️ 30s

> When I started — I was learning tools. Now — I'm solving problems. Cleanup automation, then a shared library, then AI-assisted CI/CD, now intelligent infrastructure and mobile. From learning tools to solving problems. Thank you — happy to take your questions.

---

## ⏱️ ~10 min total
