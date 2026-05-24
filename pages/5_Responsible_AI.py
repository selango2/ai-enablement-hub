"""Responsible AI — risk tiering matrix, review checklist, escalation paths."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from utils.brand import apply_brand

st.set_page_config(page_title="Responsible AI · AI Enablement Hub", layout="wide")
apply_brand("Responsible AI · 4-page operating policy")

st.title("Responsible AI")
st.caption(
    "A practical framework so every employee — and every Champion — can answer one question: "
    "'is what I want to do safe to ship, and what review do I need first?'"
)

st.divider()

# ---------- Principles ----------
st.subheader("Operating principles")
p1, p2 = st.columns(2)
with p1:
    st.markdown(
        """
        - **Default to human-in-the-loop** for any output that reaches a client.
        - **No raw customer PII or regulated data** in any external LLM, period.
        - **One catalog, one risk tier.** No shadow tools.
        - **Cite the source** for any factual claim in a model output that ships externally.
        """
    )
with p2:
    st.markdown(
        """
        - **Bias and fairness reviews** are required for any model output that influences
          customer-impacting decisions.
        - **Reversibility first.** Prefer designs where a wrong AI output is caught and
          recoverable, not silently propagated.
        - **Document, don't gatekeep.** Approvals are written down so the next person
          doesn't re-litigate them.
        """
    )

st.divider()

# ---------- Risk matrix ----------
st.subheader("Risk tiering matrix")

risk_data = pd.DataFrame(
    [
        {
            "Tier": "Tier 1",
            "What's involved": "Public information or non-sensitive internal text",
            "Examples": "Drafting public blog copy, summarizing public docs, code suggestions",
            "Reviews required": "None beyond manager sign-off",
            "Human-in-the-loop": "Recommended",
        },
        {
            "Tier": "Tier 2",
            "What's involved": "Internal documents, no customer PII or regulated data",
            "Examples": "Meeting summaries, internal Q&A copilots, proposal drafting",
            "Reviews required": "Hub sign-off, IT data classification check",
            "Human-in-the-loop": "Required for any client-facing output",
        },
        {
            "Tier": "Tier 3",
            "What's involved": "Anonymized customer data (survey verbatims, etc.)",
            "Examples": "Verbatim coding, sentiment tagging, theme extraction",
            "Reviews required": "Hub + Privacy + Methodology",
            "Human-in-the-loop": "Required",
        },
        {
            "Tier": "Tier 4",
            "What's involved": "Regulated data (PHI, regulated financial data) or decisions with material customer impact",
            "Examples": "Patient experience analysis, claims decisioning support",
            "Reviews required": "Hub + Privacy + Legal + BU exec + executive sponsor",
            "Human-in-the-loop": "Required + audit log + fairness review",
        },
    ]
)

st.dataframe(risk_data, use_container_width=True, hide_index=True)

st.divider()

# ---------- Self-check ----------
st.subheader("Pre-flight self-check")
st.caption(
    "Work through this before submitting a new use case. The output of this section "
    "is what gets pasted into the intake form."
)

with st.form("self_check"):
    name = st.text_input("Use case name")
    bu = st.text_input("Business unit")
    data_in = st.selectbox(
        "What data will the model see?",
        [
            "Public info only",
            "Internal documents (no customer PII)",
            "Anonymized customer data",
            "Identified customer data / regulated data",
        ],
    )
    output_dest = st.selectbox(
        "Where does the output go?",
        ["Internal-only", "Reviewed by human before client/external use", "Direct to customer/external"],
    )
    reversible = st.selectbox(
        "If the model is wrong, is the impact reversible?",
        ["Yes — easy to catch and correct", "Partially — caught at QA", "No — could ship before noticed"],
    )

    checks = st.columns(2)
    with checks[0]:
        bias_thought = st.checkbox("I have considered bias / fairness implications")
        owner_named = st.checkbox("There is a named human owner for the output")
    with checks[1]:
        sources_cite = st.checkbox("Outputs cite sources where appropriate")
        rollback = st.checkbox("There is a rollback / pause plan")

    submitted = st.form_submit_button("Compute risk tier")

if submitted:
    tier = 1
    if data_in == "Internal documents (no customer PII)":
        tier = max(tier, 2)
    if data_in == "Anonymized customer data":
        tier = max(tier, 3)
    if data_in == "Identified customer data / regulated data":
        tier = max(tier, 4)
    if output_dest == "Direct to customer/external" and tier < 3:
        tier = max(tier, 3)
    if reversible == "No — could ship before noticed":
        tier = max(tier, 3)

    color = {1: "green", 2: "blue", 3: "orange", 4: "red"}[tier]
    st.markdown(f"## Suggested tier: :{color}[**Tier {tier}**]")
    st.markdown(
        f"**{name or 'This use case'}** ({bu or 'Unspecified BU'}) — "
        "follow the review path in the matrix above. Anything not checked off needs to be addressed before submission."
    )

    unchecked = [
        label for label, val in [
            ("Bias / fairness considered", bias_thought),
            ("Named owner", owner_named),
            ("Sources cited", sources_cite),
            ("Rollback plan", rollback),
        ] if not val
    ]
    if unchecked:
        st.warning("Open items: " + ", ".join(unchecked))
    else:
        st.success("All pre-flight items checked — ready to submit to triage.")

st.divider()

# ---------- Escalation ----------
st.subheader("Escalation paths")
st.markdown(
    """
    - **General questions:** post in `#ai-enablement` (24h SLA).
    - **Tool approval / governance question:** Hub office hours, Tue/Thu 10–11 ET.
    - **Privacy or regulated-data question:** raise a ticket to Privacy Office; copy Hub lead.
    - **Suspected misuse or shadow-tool risk:** confidential intake form — reviewed within 1 business day.
    """
)
