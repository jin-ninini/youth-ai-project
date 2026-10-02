# 🐍 Session 02 — Python for Beginners

> Hands-on Python basics that end with a rule-based mini agent and a team code battle.

<br>

## Overview

First-time programmers (Sat 4/11) write small working programs instead of memorizing syntax. The session moves from `print` to classes in one storyline: a "student finance helper" built by each team. By the end, every team ships a mini agent that takes input, checks rules, and answers.

<br>

## Approach

- **Concepts**: `print`, `import`, variables, data types, `input`, `if`/`else`, `for`/`range`, lists, functions, dictionaries, `json`, `try`/`except`, classes
- **Hands-on**: `notebooks/python_basics.ipynb` follows the lecture slides cell by cell, with team activities marked 👥
- **Game**: `notebooks/team_battle.ipynb` runs the five-round code battle (symbols, output prediction, debugging, code assembly, build-off) with facilitator answer cells
- **Final Build**: `mini_agent.py` is the class-based mini agent from the last lecture section, runnable from the terminal

<br>

## Results

| Practice | Check | Result |
|---|---|---|
| `notebooks/python_basics.ipynb` | All 52 cells execute | Pass |
| `notebooks/team_battle.ipynb` | All answer cells execute | Pass |
| `mini_agent.py` | Answers keyword questions and exits on `종료` | Pass |

- Rule-based answers come from one dictionary, so new topics take one line
- The same `answers.get(...)` pattern grows into the Chainlit chatbot in Session 03

<br>

## Tech Stack

| Category | Stack |
|---|---|
| Languages | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square\&logo=python\&logoColor=white) |
| Development & Environment | ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square\&logo=jupyter\&logoColor=white)  ![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=flat-square\&logoColor=white)  ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square\&logo=github\&logoColor=white) |

<br>

## Project Structure

```text
session-02/
├── slides/
│   ├── session-02-python-basics.pdf   # Lecture slides
│   └── session-02-team-battle.pdf     # Team battle game slides
├── notebooks/
│   ├── python_basics.ipynb         # Lecture walkthrough (print → class → mini agent)
│   └── team_battle.ipynb           # Five-round team battle with answer cells
├── requirements.txt
├── README.md
└── mini_agent.py                   # Final mini agent (terminal)
```

<br>

## Getting Started

```bash
cd session-02
pip install -r requirements.txt
python mini_agent.py
```

Open `notebooks/python_basics.ipynb` in VS Code or Jupyter and run cells with `Shift + Enter`. Cells with `input()` wait for an answer in the input box.

<br>

## Notes

- Uses only the Python standard library, so no `.env` or API key is needed
- Run team battle answer cells only after teams submit their answers
- Next session wraps the same rule-based bot in a Chainlit chat UI
