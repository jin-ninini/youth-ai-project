# 🤝 Session 07 — AI Agents 2: Multi-Agent, Memory, and RAG

> Orchestrate multiple agents, give them memory, and ground answers in documents with RAG.

<br>

## Overview

Students extend single agents into teams (Sat 7/18). They run Sequential, Concurrent, and GroupChat orchestrations, compare an agent with and without session memory, and build a RAG helper that searches school documents with embeddings. Homework is a self-directed AI school helper built with GitHub Copilot.

<br>

## Approach

- **Data**: In-notebook school and career documents; `data/rag_source.md` is the career knowledge base for Quiz 3
- **Concepts**: Sequential / Concurrent / GroupChat orchestration, `create_session()` memory, retrieval-augmented generation, embeddings, `@tool`
- **Hands-on**: `notebooks/session7_main.ipynb` is the lecture notebook with five quizzes; `session7_quiz1`–`3` are standalone quiz notebooks; `practice-07.ipynb` covers memory, ChromaDB RAG, and a debate
- **Agent-Framework-Samples Practice**: `conditional_workflow.py` adapts 07.Workflow (condition): a reporter drafts an article, an editor reviews it, and the workflow publishes or rejects based on the review
- **Homework**: AI school helper (`school_helper_template.py`)
  - Fill in at least 10 school documents (timetable, lunch menu, clubs, library, rules)
  - Question → `@tool` embedding search → grounded answer; test at least 3 questions
  - Bonus: Gradio UI, session memory, or multiple agents

<br>

## Results

| Practice | Check | Result |
|---|---|---|
| `notebooks/session7_main.ipynb` | All demo cells execute with `.env` | Pass |
| `notebooks/session7_quiz1.ipynb` – `quiz3.ipynb` | Run end to end with the blanks filled in | Pass |
| `notebooks/practice-07.ipynb` | All cells execute with `.env` | Pass |
| `school_helper_template.py` | Answers from retrieved school data | Pass |
| `conditional_workflow.py` | Approves a club news story, rejects a cheating guide | Pass |

- The school helper answers "오늘 급식 뭐야?" with the exact menu from its documents
- The editor agent approves a club award story and rejects a "시험 문제 몰래 보기" article as encouraging cheating

<br>

## Tech Stack

| Category | Stack |
|---|---|
| Languages | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square\&logo=python\&logoColor=white) |
| Data Analysis | ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square\&logo=numpy\&logoColor=white) |
| Machine Learning | ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square\&logo=scikitlearn\&logoColor=white) |
| NLP & LLM | ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square\&logo=openai\&logoColor=white)  ![Microsoft Agent Framework](https://img.shields.io/badge/Microsoft%20Agent%20Framework-5C2D91?style=flat-square\&logoColor=white)  ![Gradio](https://img.shields.io/badge/Gradio-F97316?style=flat-square\&logo=gradio\&logoColor=white) |
| Database | ![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6446?style=flat-square\&logoColor=white) |
| Big Data & Cloud | ![Microsoft Azure](https://img.shields.io/badge/Microsoft%20Azure-0078D4?style=flat-square\&logoColor=white) |
| Development & Environment | ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square\&logo=jupyter\&logoColor=white)  ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square\&logo=github\&logoColor=white) |

<br>

## Project Structure

```text
session-07/
├── slides/
│   └── session-07-multi-agent-memory-rag.pdf   # Lecture slides
├── notebooks/
│   ├── session7_main.ipynb      # Lecture: Sequential, Concurrent, GroupChat, Session, RAG
│   ├── session7_quiz1.ipynb     # Quiz 1: role agents in a GroupChat
│   ├── session7_quiz2.ipynb     # Quiz 2: study planner with session memory
│   ├── session7_quiz3.ipynb     # Quiz 3: career RAG agent with TF-IDF + @tool
│   └── practice-07.ipynb        # Memory chatbot, ChromaDB RAG, multi-agent debate
├── src/
│   └── llm_client.py            # .env → MAF chat client for APIM
├── data/
│   └── rag_source.md            # Career knowledge base for Quiz 3
├── requirements.txt
├── README.md
├── conditional_workflow.py      # Agent-Framework-Samples 07: conditional workflow
└── school_helper_template.py    # Homework: RAG school helper
```

<br>

## Getting Started

```bash
cp .env.example .env            # at the repository root; fill in the APIM values
cd session-07
pip install -r requirements.txt
python school_helper_template.py
python conditional_workflow.py "학교 축제에서 AI 포토부스가 인기였다"
```

Open `notebooks/session7_main.ipynb` for the lecture. Approved articles from `conditional_workflow.py` are saved to `data/output/`.

<br>

## Notes

- `create_session()` is synchronous; `await agent.create_session()` raises `TypeError`
- `GroupChatBuilder` takes `participants=`, `selection_func=`, and `max_rounds=`; the selector reads `state.current_round` and `state.participants`
- The quiz notebooks contain `???` blanks by design, so they stop at the first blank until students fill it in
- The homework template now reads `APIM_BASE_URL` like every other session instead of the removed `APIM_ENDPOINT`
- Use GitHub Copilot by writing what you want as a Korean comment, then read the suggestion before accepting it
