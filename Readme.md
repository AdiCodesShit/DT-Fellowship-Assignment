# DT Fellowship Assignment – Daily Reflection Tree

## Overview

This project is a deterministic end-of-day employee reflection tool designed as a structured decision tree.

Instead of relying on a live LLM or free-text journaling, the system guides users through a short reflection conversation using fixed-choice questions, branching logic, and prewritten insights.

The goal is to help employees reflect on how they approached their day through three psychological dimensions:

1. **Ownership** – Did I focus on what I could control?
2. **Contribution** – Was I focused on giving value or expecting value?
3. **Perspective** – Was I thinking only about myself or also about others?

The final product is predictable, auditable, and consistent.

---

## Why This Approach

Many AI reflection tools generate responses dynamically, but that creates issues such as inconsistency, hallucinations, and poor explainability.

This project uses a **deterministic tree-based system** where:

* Same answers always produce the same flow
* Every branch is human designed
* No runtime API calls are required
* Logic is transparent and maintainable

---

## Project Structure

```text
DT-Fellowship-Assignment/
│── tree/
│   ├── reflection-tree.json
│   ├── tree-diagram.md
│
│── agent/
│   └── main.py
│
│── transcripts/
│   ├── persona-1.md
│   └── persona-2.md
│
│── write-up.md
│── README.md
```

---

## How It Works

The reflection session progresses through three sequential axes:

### Axis 1 – Ownership

Explores whether the user interpreted events with agency or helplessness.

### Axis 2 – Contribution

Explores whether attention was on giving value or expecting value.

### Axis 3 – Perspective

Explores whether focus remained self-centered or expanded toward team/customer impact.

---

## Data Design

The reflection tree is stored in JSON.

Each node contains:

* `id` – unique identifier
* `type` – start, question, reflection, bridge, summary, end
* `text` – user-facing content
* `options` – fixed answer choices
* `next` – next node path
* `signal` – internal state markers for scoring patterns

This separates content from engine logic.

---

## Running the Python Agent

## Requirements

* Python 3.9+

## Run

```bash
cd agent
python main.py
```

Make sure `reflection-tree.json` is available in the correct path.

---

## Example Session Flow

```text
Good evening. Let’s take a few minutes to reflect on your day.

How would you describe your day overall?
1. Productive
2. Mixed
3. Frustrating
4. Draining

Choose option number: 1
```

The system continues through branching questions and ends with a personalized summary.

---

## Design Highlights

* Deterministic and explainable logic
* Human-written reflections
* No free text input required
* Option-level signals for improved precision
* Expandable for web/mobile deployment

---

## Future Improvements

* Weekly trend tracking
* Web interface
* Better adaptive summaries
* Analytics dashboard (privacy-safe)
* Expanded tree depth and more nuanced branches

---

## Final Note

This project was built to demonstrate structured thinking, behavioral design, and product reasoning—not only coding.

The core challenge was translating psychology into a usable system that a tired employee could complete in a few minutes and still gain value from.
