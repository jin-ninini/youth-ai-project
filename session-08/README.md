# 🏁 Session 08 — Hackathon

> Pre-hackathon design thinking with an LLM coach, plus reference notebooks for data, local LLMs, and image classification.

<br>

## Overview

Teams prepare an AI service idea for the hackathon (Sat 8/8). The design thinking workbook pairs each student with an LLM coach to go from a daily pain point to a one-page service plan. The remaining notebooks are reference material adapted for this course that teams can build on during the hackathon.

<br>

## Approach

- **Data**: `data/atlantis.csv` (sample population by year) for the pandas plotting example; CIFAR-10 is downloaded by the image classifier at run time
- **Design Thinking**: `AI_Hackathon_Design_Thinking_Workbook_v3.ipynb` walks through Empathize & Define → Ideate → Prototype & Test (role-play with a simulated chatbot) → a Markdown plan draft
- **Local LLM**: `transformers_qwen2.5_0.5b_instruct.ipynb`, `wordcloud.ipynb`, and `sentence_builder.ipynb` show next-token probabilities from Qwen2.5 as tables, word clouds, and an interactive sentence builder
- **Reference**: `image-classifier.ipynb` trains a small PyTorch CNN on CIFAR-10; `matplotlib.ipynb`, `population.ipynb`, and `assignment1_sample.ipynb` cover plotting and a function-based calculator
- **Chatbot**: `myChatbot.py` is the Session 03 Chainlit chatbot, kept as a hackathon starting point

<br>

## Results

| Notebook / Script | Check | Result |
|---|---|---|
| `AI_Hackathon_Design_Thinking_Workbook_v3.ipynb` | All steps execute with `.env` and save a plan | Pass |
| `assignment1_sample.ipynb` | All cells execute | Pass |
| `matplotlib.ipynb` | All cells execute | Pass |
| `population.ipynb` | Reads `data/atlantis.csv` and plots | Pass |
| `myChatbot.py` | Chainlit app boots | Pass |
| `transformers_qwen2.5_0.5b_instruct.ipynb` | Generates text and prints top-10 next tokens | Pass |
| `image-classifier.ipynb` | Downloads CIFAR-10, trains 2 epochs, evaluates | Pass (about 1 minute on Apple Silicon) |
| `wordcloud.ipynb` | Qwen2.5-1.5B int8 model loads | Loads; first load takes over 10 minutes on CPU/MPS |
| `sentence_builder.ipynb` | Interactive Tk window | Not run (needs a desktop GUI) |

- The workbook keeps the coach's conversation history per step, so follow-up requests refine the previous answer

<br>

## Tech Stack

| Category | Stack |
|---|---|
| Languages | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square\&logo=python\&logoColor=white) |
| Data Analysis | ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square\&logo=pandas\&logoColor=white)  ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square\&logo=numpy\&logoColor=white) |
| Deep Learning | ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square\&logo=pytorch\&logoColor=white) |
| NLP & LLM | ![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=flat-square\&logo=huggingface\&logoColor=black)  ![Transformers](https://img.shields.io/badge/Transformers-FFD21E?style=flat-square\&logo=huggingface\&logoColor=black)  ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square\&logo=openai\&logoColor=white)  ![Chainlit](https://img.shields.io/badge/Chainlit-F80061?style=flat-square\&logoColor=white) |
| Visualization | ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square\&logoColor=white) |
| Big Data & Cloud | ![Microsoft Azure](https://img.shields.io/badge/Microsoft%20Azure-0078D4?style=flat-square\&logoColor=white) |
| Development & Environment | ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square\&logo=jupyter\&logoColor=white)  ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square\&logo=github\&logoColor=white) |

<br>

## Project Structure

```text
session-08/
├── notebooks/
│   ├── AI_Hackathon_Design_Thinking_Workbook_v3.ipynb   # Pre-hackathon assignment with an LLM coach
│   ├── transformers_qwen2.5_0.5b_instruct.ipynb         # Qwen2.5-0.5B next-token probabilities
│   ├── wordcloud.ipynb                                  # Next-token word cloud (Qwen2.5-1.5B, int8)
│   ├── sentence_builder.ipynb                           # Interactive word-cloud sentence builder
│   ├── image-classifier.ipynb                           # PyTorch CNN on CIFAR-10
│   ├── matplotlib.ipynb                                 # Pyplot tutorial
│   ├── population.ipynb                                 # Plot data/atlantis.csv with pandas
│   └── assignment1_sample.ipynb                         # Function-based calculator
├── data/
│   └── atlantis.csv
├── requirements.txt
├── README.md
└── myChatbot.py                                         # Chainlit chatbot from Session 03
```

<br>

## Getting Started

```bash
cp .env.example .env            # at the repository root; fill in the APIM values
cd session-08
pip install -r requirements.txt
python -m chainlit run myChatbot.py -w
```

Open `notebooks/AI_Hackathon_Design_Thinking_Workbook_v3.ipynb` first and replace each `<예: ...>` input with your own idea. The plan is saved next to the notebook as `hackathone_plan_OOO.md`.

<br>

## Notes

- The Qwen notebooks download the model from Hugging Face on first run (0.5B ≈ 1 GB, 1.5B ≈ 3 GB)
- `sentence_builder.ipynb` uses `%matplotlib tk`, so it needs a local desktop Jupyter rather than Codespaces
- `image-classifier.ipynb` downloads CIFAR-10 into `notebooks/data/` and saves `notebooks/cifar_net.pth`; both are git-ignored
- `image-classifier.ipynb` now calls `next(dataiter)`; `dataiter.next()` was removed in current PyTorch
- On a python.org macOS install, run `Install Certificates.command` once if the CIFAR-10 download fails with `CERTIFICATE_VERIFY_FAILED`
- Uses the repository-level devcontainer and `.gitignore`; generated files are listed in `session-08/.gitignore`
