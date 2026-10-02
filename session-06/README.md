# 🛠️ Session 06 — AI Agents 1: Tools and Function Calling

> From chatbot to agent: tools, the ReAct loop, Microsoft Agent Framework, and a Semantle clone.

<br>

## Overview

Students learn that an agent is an LLM plus tools (Sat 7/11, 10:00–13:00). They define tools, implement the Think → Act → Observe loop, and rebuild it with Microsoft Agent Framework (MAF). Practice scripts adapted from [microsoft/Agent-Framework-Samples](https://github.com/microsoft/Agent-Framework-Samples) (folders 02 and 04) extend the lesson to a travel agent and an image-reading agent.

<br>

## Approach

- **Concepts**: Function calling, tool definitions, ReAct (Reason + Act), agent loop, MAF `Agent`, `AgentExecutor`, `WorkflowBuilder`
- **Hands-on**: `notebooks/01_function_calling_agent.ipynb` builds a math agent (calculator + graph tools) and a web search agent; `notebooks/maf_sample_scenarios.ipynb` walks through four MAF scenarios
- **Agent-Framework-Samples Practice**: `travel_agent.py` (02.CreateYourFirstAgent) calls a random-destination tool to plan a day trip; `vision_agent.py` (04.Tools, vision) explains an image with `VISION_MODEL`
- **Homework**: Semantle clone (`semantle_template.py`)
  - Pick a target word; each guess returns a 0–100 similarity score from embeddings
  - Guess the word in as few tries as possible
  - Bonus: Gradio UI polish, hints for words scoring 80+, a leaderboard of fewest tries

<br>

## Results

| Practice | Check | Result |
|---|---|---|
| `notebooks/01_function_calling_agent.ipynb` | All cells execute with `.env` | Pass |
| `notebooks/maf_sample_scenarios.ipynb` | All cells execute with `.env` | Pass |
| `maf_sample_scenarios.py` | Scenarios 1–4 complete | Pass |
| `travel_agent.py` | Agent calls the destination tool and plans a trip | Pass |
| `vision_agent.py` | Describes `data/graph.png` (y = 2x + 3) | Pass |
| `semantle_template.py` | Scores rise with closer words; exact word wins | Pass |

- For target "고양이", guesses score 철학 0 → 컴퓨터 19 → 강아지 41 → 동물 48 → 고양이 🎉
- Tool calls run through `OpenAIChatCompletionClient`, which stays stateless and works behind the APIM proxy

<br>

## Tech Stack

| Category | Stack |
|---|---|
| Languages | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square\&logo=python\&logoColor=white) |
| Data Analysis | ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square\&logo=numpy\&logoColor=white) |
| NLP & LLM | ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square\&logo=openai\&logoColor=white)  ![Microsoft Agent Framework](https://img.shields.io/badge/Microsoft%20Agent%20Framework-5C2D91?style=flat-square\&logoColor=white)  ![Gradio](https://img.shields.io/badge/Gradio-F97316?style=flat-square\&logo=gradio\&logoColor=white) |
| Visualization | ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square\&logoColor=white) |
| Big Data & Cloud | ![Microsoft Azure](https://img.shields.io/badge/Microsoft%20Azure-0078D4?style=flat-square\&logoColor=white) |
| Development & Environment | ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square\&logo=jupyter\&logoColor=white)  ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square\&logo=github\&logoColor=white) |

<br>

## Project Structure

```text
session-06/
├── slides/
│   └── session-06-maf-intro.pdf   # Lecture slides
├── notebooks/
│   ├── 01_function_calling_agent.ipynb   # Tools, agent loop, math and web search agents
│   └── maf_sample_scenarios.ipynb        # MAF: hello, tools, collaboration, workflow
├── src/
│   └── llm_client.py                     # .env → MAF chat client for APIM
├── data/
│   └── graph.png                         # Sample image for vision_agent.py
├── requirements.txt
├── README.md
├── maf_sample_scenarios.py               # Script version of the MAF scenarios
├── travel_agent.py                       # Agent-Framework-Samples 02: first agent with a tool
├── vision_agent.py                       # Agent-Framework-Samples 04: vision agent
└── semantle_template.py                  # Homework: Semantle clone with Gradio
```

<br>

## Getting Started

```bash
cp .env.example .env            # at the repository root; fill in the APIM values
cd session-06
pip install -r requirements.txt
python maf_sample_scenarios.py
python travel_agent.py "친구랑 바다 보러 가고 싶어"
python vision_agent.py data/graph.png "이 그래프의 기울기는?"
python semantle_template.py     # opens a Gradio app on port 7860
```

Run the scripts from the `session-06` folder so `src/` can be imported.

<br>

## Notes

- `OpenAIChatClient` (Responses API) fails on tool calls through the APIM proxy with `previous_response_not_found`; the notebooks and scripts use `OpenAIChatCompletionClient` instead
- `semantle_template.py` maps `text-embedding-3-small` similarity (about 0.15–0.6 for related words) to 0–100; the older `(sim - 0.5) * 200` formula scored almost every guess 0
- Agent-Framework-Samples uses GitHub Models and Azure AI Foundry; these adaptations use the course APIM endpoint and replace hosted tools with local ones
- `01_function_calling_agent.ipynb` saves its plot as `notebooks/graph.png` when it runs
