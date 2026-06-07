"""Perficient AI Adoption Operating Model — landing page.

Run locally:
    streamlit run app.py
"""

from __future__ import annotations

import streamlit as st

from utils.brand import apply_brand
from utils.data_loader import (
    load_bu_adoption,
    load_champions,
    load_metrics,
    load_tools,
    load_use_cases,
)

st.set_page_config(
    page_title="Perficient · AI Adoption Operating Model",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_brand("Enterprise AI Adoption Framework")

# ---------- Hero ----------
st.title("Enterprise AI Adoption Operating Model")
st.caption(
    "A proven framework to scale AI responsibly: unified tool governance, champion-led adoption, "
    "metrics-driven measurement, and training that locks in behavior change. "
    "For enterprises ready to move beyond pilot programs."
)

st.divider()

# ---------- Headline metrics ----------
tools_df = load_tools()
use_cases_df = load_use_cases()
champions_df = load_champions()
metrics_df = load_metrics()
bu_df = load_bu_adoption()

latest = metrics_df.iloc[-1]

m1, m2, m3, m4, m5 = st.columns(5)
m1.metric("Monthly active users", f"{int(latest['active_users']):,}", "+22% MoM")
m2.metric("Hours saved (month)", f"{int(latest['hours_saved']):,}", "+23% MoM")
m3.metric("Use cases in production", int(latest["production_use_cases"]))
m4.metric("Approved tools", int((tools_df["approval_status"] == "Approved").sum()))
m5.metric("Active Champions", len(champions_df))

st.divider()

# ---------- Operating model ----------
left, right = st.columns([3, 2])

with left:
    st.subheader("How this hub works")
    st.markdown(
        """
        The hub is the **central nervous system** for AI adoption — but the work
        happens in the business units, run by Champions who know their domain.

        - **Hub team (solo IC, for the first six months)** sets standards, evaluates platforms,
          builds shared infrastructure, and unblocks Champions. Owns governance, the tool
          catalog, and the responsible-AI playbook.
        - **Champions (distributed)** are senior practitioners embedded in every BU. They
          ship use cases, train peers, and surface what's working. They are not direct
          reports — the operating model is influence, not hierarchy.
        - **Every employee** has self-serve access to approved tools, prompt libraries,
          and a clear path to propose a new use case.
        """
    )

with right:
    st.subheader("Why this exists")
    st.markdown(
        """
        - **Avoid Shadow AI.** Without an approved path, people paste customer data
          into consumer chatbots. The hub gives them a safer, faster default.
        - **Compound learning.** A use case shipped in Auto Research should accelerate the
          next one in Insurance. Without a hub, that knowledge stays siloed.
        - **Defensible governance.** One catalog, one risk framework, one source of truth
          for what's approved — auditable end-to-end.
        - **Measurable impact.** Adoption and hours-saved are tracked the same way across
          every BU, so the executive team sees one number, not twelve dashboards.
        """
    )

st.divider()

# ---------- Section index ----------
st.subheader("Where to go from here")

sections = [
    (
        "Tools Catalog",
        "pages/1_Tools_Catalog.py",
        "Two-platform tool strategy: productivity baseline + Claude Enterprise. Approved with risk tiers.",
    ),
    (
        "Use Case Marketplace",
        "pages/2_Use_Case_Marketplace.py",
        "Vetted AI use cases, tagged by BU and value driver.",
    ),
    (
        "Champions Network",
        "pages/3_Champions_Network.py",
        "The distributed Champions model — hub-and-spoke that scales adoption.",
    ),
    (
        "Adoption Metrics",
        "pages/4_Adoption_Metrics.py",
        "Pre-launch baselines, per-user budgets, BU rollout — the exec view.",
    ),
    (
        "Responsible AI",
        "pages/5_Responsible_AI.py",
        "Risk tiering, review checklist, escalation paths.",
    ),
    (
        "Prompt Library",
        "pages/6_Prompt_Library.py",
        "Vetted prompts mapped to research and analyst workflows.",
    ),
    (
        "Live Agent",
        "pages/7_Live_Agent.py",
        "Claude-powered Industry Insight Assistant — governance encoded in the system prompt.",
    ),
    (
        "Training & Personas",
        "pages/8_Training_Personas.py",
        "Persona-based AI literacy tracks — training as the gate to tool access.",
    ),
]

cols = st.columns(2)
for i, (title, path, desc) in enumerate(sections):
    with cols[i % 2]:
        with st.container(border=True):
            st.markdown(f"**{title}**")
            st.caption(desc)
            st.page_link(path, label=f"Open {title} →")

st.divider()

with st.expander("About this prototype"):
    st.markdown(
        """
        This is a working prototype of the Perficient AI Adoption Operating Model —
        built end-to-end as a demonstration of the framework in action.

        - **Stack:** Streamlit, Anthropic Claude API, Plotly, pandas.
        - **Data:** Adoption metrics, Champion names, and BU rollout figures are illustrative
          — they represent what the dashboard would look like 6 months into the program. The
          tool catalog and responsible-AI framework reflect real patterns from my prior
          experience leading the AI Hub at Toyota Connected North America.
        - **What's real:** The Live Agent on page 7 calls the Claude API directly. Prompt
          caching is enabled, governance is encoded in the system prompt, and the agent
          refuses to fabricate facts.
        """
    )
