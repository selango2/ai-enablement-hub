"""Use Case Marketplace — vetted AI use cases tagged by BU, value driver, and stage."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from utils.brand import apply_brand
from utils.data_loader import load_use_cases

st.set_page_config(page_title="Use Case Marketplace · AI Enablement Hub", layout="wide")
apply_brand("Use Case Marketplace · Two-track intake")

st.title("Use Case Marketplace")
st.caption(
    "Vetted AI use cases across the company. Each one names an owner, "
    "the tools used, and the productivity it returns."
)

df = load_use_cases()

# ---------- Top-line ----------
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total use cases", len(df))
c2.metric("In production", int((df["stage"] == "In production").sum()))
c3.metric("In pilot", int((df["stage"] == "Pilot").sum()))
c4.metric(
    "Hours saved / year",
    f"{int(df['annualized_hours_saved'].sum()):,}",
)

st.divider()

# ---------- Filters ----------
f1, f2, f3 = st.columns(3)
bu_filter = f1.multiselect(
    "Business unit",
    sorted(df["business_unit"].unique()),
    default=sorted(df["business_unit"].unique()),
)
stage_filter = f2.multiselect(
    "Stage",
    sorted(df["stage"].unique()),
    default=sorted(df["stage"].unique()),
)
driver_filter = f3.multiselect(
    "Value driver",
    sorted(df["value_driver"].unique()),
    default=sorted(df["value_driver"].unique()),
)

filtered = df[
    df["business_unit"].isin(bu_filter)
    & df["stage"].isin(stage_filter)
    & df["value_driver"].isin(driver_filter)
]

st.markdown(f"**{len(filtered)} use cases** match filters.")

stage_color = {
    "In production": "green",
    "Pilot": "blue",
    "Backlog": "gray",
}

for _, row in filtered.iterrows():
    with st.container(border=True):
        top = st.columns([3, 1, 1])
        top[0].markdown(f"### {row['title']}")
        top[0].caption(
            f"{row['business_unit']} · {row['value_driver']} · Risk {row['risk_tier']}"
        )
        top[1].markdown(f":{stage_color.get(row['stage'], 'gray')}[**{row['stage']}**]")
        top[2].metric("Hours / yr", f"{row['annualized_hours_saved']:,}")

        st.markdown(row["description"])
        st.markdown(
            f"**Owner:** {row['owner']}  ·  **Tools:** {', '.join(row['tools_used'])}"
        )

st.divider()

# ---------- Submit a new use case ----------
with st.expander("Propose a new use case"):
    with st.form("new_use_case"):
        title = st.text_input("Title")
        col1, col2 = st.columns(2)
        bu = col1.text_input("Business unit")
        owner = col2.text_input("Proposed owner")
        desc = st.text_area("Description (what work it replaces, where it plugs in)")
        if st.form_submit_button("Submit for triage"):
            st.success(
                f"Submitted: '{title}' from {bu}. Triage SLA: 3 business days."
            )
