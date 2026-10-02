# 🔆 Youth AI Project 2026 — P.I.N.E. 2nd Cohort

> A hands-on AI course where high school students go from their first `print` to multi-agent RAG services.

<br>

## Overview

P.I.N.E. (Youth AI Project) is a 2026 program for high school students aged 17–19 who plan to pursue AI, run with KB Data System and Microsoft Korea alongside lead instructors and university mentors. Across nine Saturday sessions from April to August, students learn Python, how LLMs work, the OpenAI SDK, and Microsoft Agent Framework. They then build their own AI service at a hackathon and present it at the P.I.N.E. CON AI festival.

<br>

## Approach

- **Environment**: GitHub Codespaces with Jupyter notebooks, set up automatically by `.devcontainer/`
- **Model Access**: Every LLM, vision, and embedding call goes through an Azure API Management (APIM) proxy configured in `.env`
- **Structure**: Each `session-XX/` folder is a self-contained project with its own slides, notebooks, scripts, `requirements.txt`, and README
- **Slides**: Every deck is a PDF in `session-XX/slides/`, named `session-XX-<topic>.pdf`
- **Homework**: Each session ends with a small build that the next session reuses

| Session | Date | Topic | Homework |
|---|---|---|---|
| 1 | Sat 4/4 | Kick-off ceremony | - |
| 2 | Sat 4/11 | [Python for Beginners](./session-02/) | Team code battle + mini agent |
| 3 | Sat 5/9 | [Chatbot with Chainlit](./session-03/) | Class-based chatbot |
| 4 | Sat 5/16 | [AI Fundamentals](./session-04/) | Prompt Master Challenge |
| 5 | Sat 5/30 | [AI Programming with the OpenAI SDK](./session-05/) | Persona chatbot with Gradio |
| 6 | Sat 7/11 | [AI Agents 1: Tools and Function Calling](./session-06/) | Semantle clone |
| 7 | Sat 7/18 | [AI Agents 2: Multi-Agent, Memory, and RAG](./session-07/) | AI school helper (RAG) |
| 8 | Sat 8/8 | [Hackathon](./session-08/) | Team AI service prototype |
| 9 | Sat 8/22 | P.I.N.E. CON AI festival | Demo day, awards, industry talks |

<br>

## Results

| Session | What Students Build | Verified |
|---|---|---|
| 02 | Rule-based mini agent in the terminal | All notebooks and `mini_agent.py` run |
| 03 | Chainlit chatbot with answer modes and a question counter, plus an LLM version | All 7 Chainlit apps boot and reply |
| 04 | MicroGPT trained from scratch on 32,000 names | All 5 notebooks run |
| 05 | Persona chatbot with conversation memory | Notebook and template run |
| 06 | Tool-using agents, travel and vision agents, Semantle clone | All notebooks and scripts run |
| 07 | Multi-agent orchestration, session memory, RAG school helper, conditional workflow | All notebooks, quizzes (filled), and scripts run |
| 08 | Design-thinking plan with an LLM coach, local LLM and image classifier references | All runnable notebooks pass; see the session README |

- Verified on 2026-10-02 with the locked dependencies in `uv.lock` and the shared `.env`
- Agent code uses `OpenAIChatCompletionClient`, because tool calls through the APIM proxy fail with the Responses-based `OpenAIChatClient`

<br>

## Tech Stack

| Category | Stack |
|---|---|
| Languages | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square\&logo=python\&logoColor=white) |
| Data Analysis | ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square\&logo=pandas\&logoColor=white)  ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square\&logo=numpy\&logoColor=white) |
| Machine Learning | ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square\&logo=scikitlearn\&logoColor=white) |
| Deep Learning | ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square\&logo=pytorch\&logoColor=white) |
| NLP & LLM | ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square\&logo=openai\&logoColor=white)  ![Microsoft Agent Framework](https://img.shields.io/badge/Microsoft%20Agent%20Framework-5C2D91?style=flat-square\&logoColor=white)  ![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=flat-square\&logo=huggingface\&logoColor=black)  ![Gradio](https://img.shields.io/badge/Gradio-F97316?style=flat-square\&logo=gradio\&logoColor=white)  ![Chainlit](https://img.shields.io/badge/Chainlit-F80061?style=flat-square\&logoColor=white) |
| Visualization | ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square\&logoColor=white) |
| Database | ![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6446?style=flat-square\&logoColor=white) |
| Big Data & Cloud | ![Microsoft Azure](https://img.shields.io/badge/Microsoft%20Azure-0078D4?style=flat-square\&logoColor=white) |
| Development & Environment | ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square\&logo=git\&logoColor=white)  ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square\&logo=github\&logoColor=white)  ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square\&logo=jupyter\&logoColor=white)  ![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=flat-square\&logoColor=white) |

<br>

## Project Structure

```text
youth-ai-project/
├── .devcontainer/      # Codespaces setup (uv sync, Korean fonts, .env)
├── session-02/         # Python for Beginners
├── session-03/         # Chatbot with Chainlit
├── session-04/         # AI Fundamentals
├── session-05/         # AI Programming with the OpenAI SDK
├── session-06/         # AI Agents 1: Tools and Function Calling
├── session-07/         # AI Agents 2: Multi-Agent, Memory, and RAG
├── session-08/         # Hackathon
├── setup-apim/         # APIM proxy architecture, policy, and test notebook
├── utils/              # Shared APIM client helpers
├── fonts/              # NanumGothic for Korean chart labels
├── archive/            # Earlier curriculum drafts
├── .env.example        # APIM settings template
├── pyproject.toml
├── uv.lock
└── README.md
```

<br>

## Getting Started

In GitHub Codespaces, `.devcontainer/post-create.sh` installs every dependency with `uv sync` and creates `.env` automatically. Fill in the APIM values in `.env` and open any session.

Locally:

```bash
uv sync                          # or: pip install -r session-XX/requirements.txt
cp .env.example .env             # fill in APIM_BASE_URL and APIM_KEY
cd session-03
python -m chainlit run myChatbot.py -w
```

Each session README lists its own commands.

<br>

## Notes

- Never commit `.env`; it holds the shared APIM key
- Set `max_completion_tokens` on API calls to keep costs predictable
- Always check AI answers for bias, hallucinations, and copyright issues
- References: [Microsoft Agent Framework Samples](https://github.com/microsoft/Agent-Framework-Samples), [Azure OpenAI docs](https://learn.microsoft.com/azure/ai-services/openai/), [Prompt Engineering Guide](https://www.promptingguide.ai/kr), [Gradio docs](https://www.gradio.app/docs), [Chainlit docs](https://docs.chainlit.io)

<br>

## License

Copyright © 2026 Hyunjin Hwang, Youth AI Project. All rights reserved.

This repository is provided for viewing and portfolio evaluation purposes only.

No permission is granted to copy, modify, distribute, sublicense, publish, or commercially use any part of this project, including its source code, assets, documentation, design, or other contents, without prior written permission from the copyright holder.

If you want to use this project or any portion of it, please obtain written permission from the repository owner in advance.
