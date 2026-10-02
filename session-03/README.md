# 💬 Session 03 — Build Your Own Chatbot with Chainlit

> A keyword chatbot that grows from a function to a class inside a Chainlit chat UI.

<br>

## Overview

Students connect the rules they wrote in Session 02 to a real chat screen (Sat 5/9). As the answer logic grows, they refactor it from `if` chains to a dictionary and then to an `AdviceBot` class. The session closes by previewing why rule-based bots hit a limit and how an LLM removes it.

<br>

## Approach

- **Concepts**: Chainlit events (`on_message`, `on_chat_start`), functions vs classes, attributes, methods, `self`, `__init__`, `user_session`
- **Hands-on**: `steps/01`–`05` mirror each slide section, so students can jump to any stage
- **Final Build**: `myChatbot.py` combines answer rules, answer modes (`짧게` / `자세히` / `예시`), a greeting, and a question counter
- **Bonus**: `llm_chatbot.py` swaps the rules for an LLM through the course APIM proxy, previewing Session 04

<br>

## Results

| Practice | Check | Result |
|---|---|---|
| `steps/01_echo.py` – `steps/05_llm_preview.py` | App boots and handlers reply | Pass |
| `myChatbot.py` | Mode switching and question counter | Pass |
| `llm_chatbot.py` | LLM reply with `.env` credentials | Pass |

- `"자세히 공부 알려줘"` returns the detailed study tip, `"짧게 진로 알려줘"` the short career tip
- The LLM bot answers questions that are not in any rule, which the rule-based bot cannot do

<br>

## Tech Stack

| Category | Stack |
|---|---|
| Languages | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square\&logo=python\&logoColor=white) |
| NLP & LLM | ![Chainlit](https://img.shields.io/badge/Chainlit-F80061?style=flat-square\&logoColor=white)  ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square\&logo=openai\&logoColor=white) |
| Big Data & Cloud | ![Microsoft Azure](https://img.shields.io/badge/Microsoft%20Azure-0078D4?style=flat-square\&logoColor=white) |
| Development & Environment | ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square\&logo=github\&logoColor=white)  ![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=flat-square\&logoColor=white) |

<br>

## Project Structure

```text
session-03/
├── slides/
│   └── session-03-chainlit-chatbot.pdf   # Lecture slides
├── steps/
│   ├── 01_echo.py                # Echo the user message
│   ├── 02_answer_function.py     # Move answers into a function with if/elif
│   ├── 03_answer_dict.py         # Collect answers in a dictionary
│   ├── 04_advice_bot_class.py    # Wrap rules in the AdviceBot class
│   └── 05_llm_preview.py         # Tokenize → numbers preview of how LLMs read text
├── requirements.txt
├── README.md
├── myChatbot.py                  # Final class-based chatbot
└── llm_chatbot.py                # Bonus: LLM-powered chatbot (needs .env)
```

<br>

## Getting Started

```bash
cd session-03
pip install -r requirements.txt
python -m chainlit run myChatbot.py -w
python -m chainlit run steps/03_answer_dict.py -w
```

Open port `8000` from the **PORTS** tab to see the chat screen. Use the terminal command, not the VS Code run button.

For the bonus bot, copy `.env.example` to `.env` at the repository root, fill in the APIM values, then run:

```bash
python -m chainlit run llm_chatbot.py -w
```

<br>

## Notes

- Restart with `Ctrl + C` if changes do not show up
- `IndentationError` usually means a missing indent under `class`, `def`, or `if`
- Only `llm_chatbot.py` calls the API; every other file runs offline
