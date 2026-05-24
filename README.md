# AI Enablement Hub

A working prototype of an enterprise AI Enablement Hub — built as a hands-on demonstration for the Head of AI Enablement role.

The hub is a single landing place where every business unit can discover approved AI tools, browse vetted use cases, find their Champion, track adoption, and run governed AI workflows — without each team reinventing the wheel.

## What's inside

| Section | What it shows |
|---|---|
| **Home** | Mission, operating model, how the hub serves BUs |
| **Tools Catalog** | Approved LLM and copilot tools with risk tier, intended users, approval status |
| **Use Case Marketplace** | Vetted AI use cases tagged by business unit and value driver |
| **Champions Network** | Distributed AI Champions across BUs — the operating model that scales without a large central team |
| **Adoption Metrics** | Executive dashboard: active users, hours saved, ROI, BU rollout heatmap |
| **Responsible AI** | Risk tiering matrix, review checklist, escalation paths |
| **Prompt Library** | Vetted prompts mapped to research and analyst workflows |
| **Live Agent** | A working Claude-powered Industry Insight Assistant — proof of hands-on technical depth |

## Quick start

```bash
# 1. Clone and enter
git clone <this-repo> ai-enablement-hub
cd ai-enablement-hub

# 2. Install
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 3. Add your Anthropic API key
cp .env.example .env
# edit .env and set ANTHROPIC_API_KEY=sk-ant-...

# 4. Run
streamlit run app.py
```

The app opens at http://localhost:8501.

## Deploy a shareable URL

1. Push this repo to GitHub
2. Go to https://streamlit.io/cloud and connect the repo
3. Set `ANTHROPIC_API_KEY` as a secret in the Streamlit Cloud dashboard
4. Deploy — you'll get a public URL like `your-app.streamlit.app`

## Stack

- **Streamlit** — multi-page web app, no frontend code required
- **Anthropic Claude API** — powers the live agent
- **Plotly** — interactive charts for the metrics dashboard
- **Pandas** — data handling for catalogs and metrics

## How this maps to the role

| Role expectation | Where it shows up |
|---|---|
| Personally prototype tools | This entire repo |
| Set standards and governance | Responsible AI page, Tools Catalog risk tiers |
| Distributed Champions model (influence, not hierarchy) | Champions Network page |
| Measurable business impact | Adoption Metrics dashboard |
| Deep technical credibility (LLMs, agents) | Live Agent page (Claude API integration) |
| Enterprise change leadership | Use Case Marketplace + Champions operating model |

## Repository structure

```
ai-enablement-hub/
├── app.py                      # Home / landing page
├── pages/                      # Streamlit multi-page screens
├── data/                       # Mock catalogs and metrics
├── utils/                      # Claude client + data loader
├── .streamlit/config.toml      # Theme
├── requirements.txt
├── .env.example
└── README.md
```

## Notes on the demo data

All adoption metrics, Champion names, and BU rollout numbers are illustrative — they represent what the dashboard would look like 6 months into the program. The Tools Catalog and Responsible AI framework reflect real patterns from current enterprise AI deployments.
