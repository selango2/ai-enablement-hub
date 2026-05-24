"""Champions Network — distributed AI Champions across BUs."""

from __future__ import annotations

import streamlit as st

from utils.brand import apply_brand
from utils.data_loader import load_champions

st.set_page_config(page_title="Champions Network · AI Enablement Hub", layout="wide")
apply_brand("Champions Network · Hub-and-spoke")

st.title("Champions Network")
st.caption(
    "Senior practitioners embedded in every business unit. They ship use cases, "
    "train peers, and surface what's working. They report into their BU — not the hub."
)

df = load_champions()

# ---------- Headline ----------
c1, c2, c3, c4 = st.columns(4)
c1.metric("Active Champions", len(df))
c2.metric("Business units covered", df["business_unit"].nunique())
c3.metric("Use cases shipped", int(df["use_cases_shipped"].sum()))
c4.metric("Peers trained", int(df["trained_peers"].sum()))

st.divider()

# ---------- Operating model ----------
left, right = st.columns([3, 2])
with left:
    st.subheader("Operating model")
    st.markdown(
        """
        **Influence, not hierarchy.** Champions are not direct reports. They are senior
        practitioners with credibility in their domain, who volunteer (or are nominated)
        to be the AI bridge between their BU and the hub.

        **The deal**
        - 20% of their time is funded by the hub via their BU.
        - They commit to: shipping at least one use case per quarter, training 5+ peers,
          and joining the weekly Champion sync.
        - In return: early access to new tools, executive visibility, and a learning budget.

        **What the hub provides**
        - Approved tools and infrastructure.
        - Prompt library and methodology playbooks.
        - Office hours and pair-building sessions.
        - A clear escalation path for governance and security questions.
        """
    )

with right:
    st.subheader("How a Champion gets nominated")
    st.markdown(
        """
        1. **BU leader proposes** a senior practitioner with subject-matter depth.
        2. **Practitioner self-nominates** through the intake form.
        3. **Hub interviews** for fit: curiosity, willingness to teach, throughput.
        4. **Onboarding cohort** quarterly: 1 day of orientation + 4 weekly working sessions.
        5. **Quarterly review** of contributions; rotation is fine — burnout is real.
        """
    )

st.divider()

st.subheader("Current Champions")

# ---------- Filters ----------
bu_filter = st.multiselect(
    "Filter by business unit",
    sorted(df["business_unit"].unique()),
    default=sorted(df["business_unit"].unique()),
)
filtered = df[df["business_unit"].isin(bu_filter)]

# ---------- Cards ----------
cols = st.columns(2)
for i, (_, row) in enumerate(filtered.iterrows()):
    with cols[i % 2]:
        with st.container(border=True):
            top = st.columns([3, 1])
            top[0].markdown(f"### {row['name']}")
            top[0].caption(f"{row['role']} · {row['business_unit']}")
            top[1].caption(f"Since {row['champion_since']}")

            st.markdown(f"**Focus:** {', '.join(row['focus_areas'])}")

            stats = st.columns(2)
            stats[0].metric("Use cases shipped", row["use_cases_shipped"])
            stats[1].metric("Peers trained", row["trained_peers"])
