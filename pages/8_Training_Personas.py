"""Training & Personas — persona-based AI literacy tracks with training-as-gate model."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

from utils.brand import apply_brand

st.set_page_config(page_title="Training & Personas · AI Enablement Hub", layout="wide")
apply_brand("Training & Personas · Training is the gate")

st.title("Training & Personas")
st.caption(
    "**My recommendation:** persona-based AI literacy tracks, not generic AI literacy. "
    "Two-thirds of JD Power's workforce are analysts, researchers, consultants, and client services — "
    "engineering-defaulted enablement fails here. **Training is the gate to tool access** — the "
    "cleanest adoption lever I've seen."
)

# ---------- Load personas ----------
DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "personas.json"
with open(DATA_PATH) as f:
    personas = json.load(f)

# ---------- Roll-up metrics ----------
total_headcount = sum(p["headcount"] for p in personas)
total_certified = sum(p["certified"] for p in personas)
total_access = sum(p["tool_access_unlocked"] for p in personas)
overall_completion = total_certified / total_headcount * 100

c1, c2, c3, c4 = st.columns(4)
c1.metric("Personas in scope", len(personas))
c2.metric("Total workforce in tracks", f"{total_headcount:,}")
c3.metric("Certified (track complete)", f"{total_certified:,}", f"{overall_completion:.0f}% of workforce")
c4.metric("Tool access unlocked", f"{total_access:,}")

st.divider()

# ---------- The conviction callout ----------
with st.container(border=True):
    st.markdown("### Why persona-based, and why training-as-gate")
    cols = st.columns(2)
    cols[0].markdown(
        """
        **Persona-based, not generic AI literacy.**

        - A research analyst's day looks nothing like a client services rep's.
        - Generic "Intro to AI" trainings fail because the examples are synthetic.
        - Each track teaches AI through *the actual workflows that role performs*.
        - Curriculum designed with each persona's Champion — examples are real.
        """
    )
    cols[1].markdown(
        """
        **Training as the gate to tool access — my strongest adoption lever.**

        - Per-user AI budgets and sanctioned tool licenses activate **only after** persona-track completion.
        - Employees self-pace because the carrot is access, not because HR is chasing them.
        - The Hub gets a clean adoption funnel to measure.
        - Proven at Toyota; same model at JD Power.
        """
    )

st.divider()

# ---------- Persona completion funnel chart ----------
st.subheader("Track completion by persona")

rows = []
for p in personas:
    rows.append({
        "Persona": p["persona"],
        "Headcount": p["headcount"],
        "Certified": p["certified"],
        "Completion %": p["certified"] / p["headcount"] * 100,
    })
df = pd.DataFrame(rows)

fig = px.bar(
    df.sort_values("Completion %", ascending=True),
    x="Completion %",
    y="Persona",
    orientation="h",
    color="Completion %",
    color_continuous_scale=["#F4C842", "#BE1E2D"],
    labels={"Completion %": "% of persona certified", "Persona": ""},
    text="Completion %",
)
fig.update_traces(texttemplate="%{text:.0f}%", textposition="outside")
fig.update_layout(coloraxis_showscale=False, plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig, use_container_width=True)

st.divider()

# ---------- Each persona's detail ----------
st.subheader("Persona tracks — the 4-session arc")

for p in personas:
    with st.container(border=True):
        top = st.columns([3, 1, 1, 1])
        top[0].markdown(f"### {p['persona']}")
        top[0].caption(f"Champion: {p['champion']}")
        top[1].metric("Headcount", f"{p['headcount']:,}")
        top[2].metric("Certified", f"{p['certified']:,}")
        completion_pct = p["certified"] / p["headcount"] * 100
        top[3].metric("Completion", f"{completion_pct:.0f}%")

        st.markdown("**4-session training arc:**")
        for i, s in enumerate(p["sessions"], 1):
            pct = s["completed"] / p["headcount"] * 100
            st.progress(
                pct / 100,
                text=f"**Session {i}:** {s['name']} — {s['completed']}/{p['headcount']} ({pct:.0f}%)",
            )

        cols = st.columns(2)
        cols[0].markdown(f"**Primary tools:** {', '.join(p['primary_tools'])}")
        cols[1].markdown(f"**Key workflows:** {', '.join(p['key_workflows'])}")

st.divider()

# ---------- Hub-and-spoke explainer ----------
with st.expander("How the hub-and-spoke training model works"):
    st.markdown(
        """
        **My recommendation:** the Hub builds and owns the curriculum; the spokes deliver it in context.

        - **Hub (me)** designs the persona tracks, owns the standards, runs certification, and provides
          the curriculum content. Hub maintains the HR learning platform integration.
        - **Champions (spokes — 2 per BU)** deliver the training in their functional context. They run
          office hours, handle day-to-day questions, and surface what's working back to the Hub.
        - **HR** owns the learning platform, tracks completion, and integrates AI literacy into role
          expectations and new-hire onboarding.

        This is how a one-person Hub scales to 2,700 employees. Without Champions and HR partnership,
        the workforce enablement plan is not viable.
        """
    )
