# DT Fellowship Assignment – Design Write-up

## Project Overview

This project is a deterministic end-of-day employee reflection tool built as a structured decision tree. The goal of the system is to help users reflect on how they approached their day through three psychological dimensions:

1. **Ownership** – The degree of control they perceived over events
2. **Contribution** – Whether their mindset focused more on giving value or expecting value
3. **Perspective** – Whether their attention remained self-focused or expanded toward others

Instead of using a live LLM or free-text journaling, the system uses predefined questions, fixed answer choices, deterministic branching, and prewritten reflections. This ensures that the experience is consistent, explainable, and trustworthy.

---

## Why I Chose a Deterministic Tree

Reflection tools should feel reliable. If two users give the same answers, they should receive the same path and summary. A deterministic tree solves several problems that runtime AI systems often create:

* **Consistency** – Same answers always produce the same result
* **Auditability** – Every branch can be reviewed and improved manually
* **Safety** – No hallucinated advice or unpredictable responses
* **Speed** – No external API calls or latency
* **Control** – Product quality comes from design rather than prompt luck

I used AI during development for brainstorming, iteration, and critique, but not inside the final product.

---

## Why I Chose JSON as the Core Format

I chose JSON because it cleanly separates **content** from **application logic**.

The JSON tree stores:

* Node IDs
* Node types (start, question, reflection, bridge, summary, end)
* Question text
* Options
* Branching paths
* Signals for state tracking

This means another developer could build a web app, mobile app, or analytics dashboard using the same tree file without changing the reflection content.

It also makes the system easy to maintain. Questions can be improved without rewriting the Python engine.

---

## Psychological Design of the Three Axes

## 1. Ownership (Locus of Control)

This axis was inspired by Rotter’s Locus of Control framework and growth mindset ideas.

The purpose is to surface whether users interpreted events as:

* Something that happened to me
  or
* Something I could influence through my action

Questions focus on reactions to setbacks, planning, adaptation, and controllable next steps.

## 2. Contribution (Entitlement vs Value Creation)

This axis explores whether attention was on:

* Recognition, Apprication, what others owe me
  or
* Helping, supporting, adding value

Questions were designed to avoid shaming. They normalize natural human expectations while gently encouraging contribution-focused thinking.

## 3. Perspective (Self vs Others)

This axis examines the radius of concern.

Was the user mainly focused on:

* Their own stress, workload, frustration
  or
* Team outcomes, colleagues, customers, users

The goal is not self-sacrifice, but expanding context. Broader perspective often reduces emotional friction and increases meaning.

---

## Branching Logic and Signals

Each answer option can emit a signal such as:

* `axis1:internal`
* `axis2:contribution`
* `axis3:others`

These signals are tallied during the session.

At the summary stage, the dominant tendency in each axis is converted into readable language such as:

* ownership
* contribution
* perspective

I intentionally upgraded the design from node-level signals to **option-level signals**, because this creates more precise and extensible behavior.

---

## Design Trade-offs

## Simplicity vs Depth

I chose concise questions with 3–4 options rather than long psychological inventories. Employees using the tool at the end of a workday are likely tired, so brevity improves completion rates.

## Determinism vs Personalization

The system does not generate custom coaching text. Instead, it uses carefully written reusable reflections. This sacrifices infinite personalization in exchange for quality control.

## Warmth vs Corporate Tone

I used a balanced tone: professional but human. The system should feel like a wise friend, not a manager, therapist, or motivational speaker.

---

## What I Would Improve With More Time

If given more time, I would add:

1. **Adaptive summaries** based on stronger signal combinations
2. **Trend tracking over time** to show weekly mindset patterns
3. **Web UI** with progress indicators and better UX
4. **A/B testing of questions** to improve reflection quality
5. **Manager dashboards (aggregate only)** without violating privacy
6. **Expanded tree depth** for more nuanced branching

---

## Final Thought

The most important part of this assignment was not code—it was translating psychological ideas into a usable structure.

My goal was to design a tool that a tired employee could complete in a few minutes and still leave with one meaningful realization about how they showed up that day.
