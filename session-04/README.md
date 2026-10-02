# 🧠 Session 04 — AI Fundamentals

> How LLMs work, from prompts and tokens to embeddings and a tiny GPT trained from scratch.

<br>

## Overview

Students build an intuition for what happens inside ChatGPT (Sat 5/16, 10:00–13:00). Each notebook takes one idea from a beginner explanation down to working code. The session ends by training MicroGPT on 32,000 names and comparing its output with a real GPT model.

<br>

## Approach

- **Data**: `data/input.txt` holds about 32,000 English first names ([karpathy/makemore](https://github.com/karpathy/makemore)) used to train MicroGPT
- **Concepts**: Prompt engineering (role, goal, context, format, constraints), tokenization, token IDs, embeddings, cosine similarity, Transformer, attention, temperature
- **Model**: MicroGPT, a pure-Python GPT with autograd, attention, and MLP blocks, plus the course chat model for the final comparison
- **Homework**: Prompt Master Challenge
  - Write a bad and a good prompt for five topics (science, math, history, English, daily life) and compare the answers
  - Good prompts use a role, concrete context and constraints, an output format, and few-shot examples
  - Bonus: Solve a complex problem with prompt chaining

<br>

## Results

| Notebook | Check | Result |
|---|---|---|
| `prompt_engineering_guide.ipynb` | All cells execute | Pass |
| `tokenizer_tutorial.ipynb` | All cells execute | Pass |
| `embedding_guide.ipynb` | All cells execute | Pass |
| `microgpt-preview.ipynb` | All cells execute | Pass |
| `microgpt-tutorial.ipynb` | Training, sampling, and GPT comparison with `.env` | Pass (about 2 minutes on CPU) |

- MicroGPT names improve visibly as the training loss drops
- Lower temperature gives safer, more repetitive names; higher temperature gives more creative ones

<br>

## Tech Stack

| Category | Stack |
|---|---|
| Languages | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square\&logo=python\&logoColor=white) |
| NLP & LLM | ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square\&logo=openai\&logoColor=white) |
| Visualization | ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square\&logoColor=white) |
| Big Data & Cloud | ![Microsoft Azure](https://img.shields.io/badge/Microsoft%20Azure-0078D4?style=flat-square\&logoColor=white) |
| Development & Environment | ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square\&logo=jupyter\&logoColor=white)  ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square\&logo=github\&logoColor=white) |

<br>

## Project Structure

```text
session-04/
├── slides/
│   ├── session-04-ai-fundamentals.pdf  # AI history and generative AI overview
│   ├── session-04-embedding.pdf        # Embedding lecture slides
│   └── session-04-inside-chatgpt.pdf   # Inside ChatGPT slides
├── notebooks/
│   ├── prompt_engineering_guide.ipynb  # Role, goal, context, format, constraints (20 min)
│   ├── tokenizer_tutorial.ipynb        # Word, character, and subword tokenizers (30 min)
│   ├── embedding_guide.ipynb           # Vectors, similarity, mini search engine (30 min)
│   ├── microgpt-preview.ipynb          # Next-word guessing game and roadmap (15 min)
│   └── microgpt-tutorial.ipynb         # Build and train MicroGPT (60 min)
├── data/
│   └── input.txt                       # Names dataset for MicroGPT
├── requirements.txt
└── README.md
```

<br>

## Getting Started

```bash
cd session-04
pip install -r requirements.txt
```

Open the notebooks in `notebooks/` in lesson order. Only the last section of `microgpt-tutorial.ipynb` calls the API; it reads `APIM_BASE_URL`, `APIM_KEY`, and `CHAT_MODEL` from the repository-root `.env`.

<br>

## Notes

- `microgpt-tutorial.ipynb` uses the Korean font in `../../fonts/NanumGothic.ttf` for chart labels
- If `data/input.txt` is missing, the tutorial downloads it again
- Submit homework as a Notion, Google Docs, or GitHub page with screenshots before the next class
