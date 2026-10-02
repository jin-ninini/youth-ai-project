# 🤖 Session 05 — AI Programming with the OpenAI SDK

> First API calls, text generation, image analysis, tool calling, and embeddings through the course APIM proxy.

<br>

## Overview

Students move from using ChatGPT to calling a model from Python (Sat 5/30, 10:00–13:00). They set up `.env`, make a first chat completion, and build small apps: a study plan generator, an image analyzer, and an FAQ bot. Homework turns this into a persona chatbot with a Gradio web UI.

<br>

## Approach

- **Concepts**: `chat.completions.create()`, system/user roles, temperature, vision input, tool (function) calling, embeddings, cosine similarity
- **Hands-on**: `notebooks/openai_workshop.ipynb` covers setup, five practice parts, and two mini assignments
- **Model**: `CHAT_MODEL`, `VISION_MODEL`, and `EMBEDDING_MODEL` from `.env`, served at `{APIM_BASE_URL}/{model}/`
- **Homework**: Build your own AI chatbot from `chatbot_template.py`
  - A system prompt that defines a persona and behavior rules
  - Conversation history so the bot remembers earlier turns
  - A Gradio web UI; submit code, a README, and two or three screenshots on GitHub

<br>

## Results

| Practice | Check | Result |
|---|---|---|
| `notebooks/openai_workshop.ipynb` | All 35 cells execute with `.env` | Pass |
| `chatbot_template.py` | Replies and remembers earlier turns | Pass |

- The template answers "방금 내가 뭐라고 했지?" correctly when history is passed in
- Typing `/reset` in the chat clears the conversation

<br>

## Tech Stack

| Category | Stack |
|---|---|
| Languages | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square\&logo=python\&logoColor=white) |
| Data Analysis | ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square\&logo=numpy\&logoColor=white) |
| Machine Learning | ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square\&logo=scikitlearn\&logoColor=white) |
| NLP & LLM | ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square\&logo=openai\&logoColor=white)  ![Gradio](https://img.shields.io/badge/Gradio-F97316?style=flat-square\&logo=gradio\&logoColor=white) |
| Big Data & Cloud | ![Microsoft Azure](https://img.shields.io/badge/Microsoft%20Azure-0078D4?style=flat-square\&logoColor=white) |
| Development & Environment | ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square\&logo=jupyter\&logoColor=white)  ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square\&logo=github\&logoColor=white) |

<br>

## Project Structure

```text
session-05/
├── notebooks/
│   └── openai_workshop.ipynb   # Setup, chat, generation, vision, tools, embeddings
├── requirements.txt
├── README.md
└── chatbot_template.py         # Homework template: persona chatbot + Gradio UI
```

<br>

## Getting Started

```bash
cp .env.example .env            # at the repository root; fill in the APIM values
cd session-05
pip install -r requirements.txt
python chatbot_template.py      # opens a Gradio app on port 7860
```

Open `notebooks/openai_workshop.ipynb` for the lecture practice.

<br>

## Notes

- Never commit `.env`; it holds the shared APIM key
- Set `max_completion_tokens` on every call to control cost
- Edit only the block marked `👇 여기를 수정하세요!` in the template: bot name, system prompt, and example questions
