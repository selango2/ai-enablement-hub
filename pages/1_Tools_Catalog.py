"""Tools Catalog — two-platform strategy grouped by tier."""

from __future__ import annotations

import streamlit as st

from utils.brand import apply_brand
from utils.data_loader import load_tools

st.set_page_config(page_title="Tools Catalog · AI Enablement Hub", layout="wide")
apply_brand("Tools Catalog · Two-platform strategy")

st.title("Tools Catalog")
st.caption(
    "My principle: **consolidation over proliferation, but not single-vendor.** Two general-purpose "
    "platforms by design — productivity baseline + Claude Enterprise. Specialized tools deferred to "
    "year two until baseline data shows where the real gaps are."
)

df = load_tools()

# ---------- Summary metrics ----------
c1, c2, c3, c4 = st.columns(4)
c1.metric("Approved tools", int((df["approval_status"] == "Approved").sum()))
c2.metric("In pilot", int((df["approval_status"].isin(["Pilot", "Under review"])).sum()))
c3.metric(
    "Total monthly spend",
    f"${int(df['monthly_cost_usd'].sum()):,}",
)
c4.metric(
    "Annualized budget",
    f"${int(df['monthly_cost_usd'].sum()) * 12:,}",
)

st.divider()

# ---------- Two-platform strategy callout ----------
with st.container(border=True):
    st.markdown("### My tool-strategy conviction")
    cols = st.columns(4)
    cols[0].markdown(
        """
        **Tier A — Analytical / high-judgment**
        *(non-negotiable)*

        Claude Enterprise + Claude Code, one Anthropic relationship,
        single observability surface.
        """
    )
    cols[1].markdown(
        """
        **Tier B — Productivity baseline**

        **ChatGPT Enterprise — approved.**
        Microsoft Copilot held under review,
        pending MS-alignment confirmation.
        Pick one, not both.
        """
    )
    cols[2].markdown(
        """
        **Tier C — Observability**
        *(non-negotiable)*

        Portkey as the centralized control plane.
        Without it, governance is a posture.
        """
    )
    cols[3].markdown(
        """
        **Tier D — Specialized**
        *(year two)*

        RAG, agents, search.
        Wait for baseline data on what
        the two platforms don't cover.
        """
    )

st.divider()

# ---------- Filters ----------
f1, f2, f3 = st.columns(3)
tier_filter = f1.multiselect(
    "Platform tier",
    sorted(df["platform_tier"].unique()),
    default=sorted(df["platform_tier"].unique()),
)
status_filter = f2.multiselect(
    "Approval status",
    sorted(df["approval_status"].unique()),
    default=sorted(df["approval_status"].unique()),
)
search = f3.text_input("Search", placeholder="vendor, use case, owner...")

filtered = df[
    df["platform_tier"].isin(tier_filter) & df["approval_status"].isin(status_filter)
]
if search:
    s = search.lower()
    filtered = filtered[
        filtered.apply(lambda row: s in str(row.to_dict()).lower(), axis=1)
    ]

# ---------- Cards grouped by tier ----------
status_color = {
    "Approved": "green",
    "Pilot": "blue",
    "Under review": "orange",
    "Blocked": "red",
}

tier_order = [
    "Tier A — Analytical / high-judgment",
    "Tier B — Productivity baseline",
    "Tier C — Observability",
    "Tier D — Specialized (year two)",
]

for tier in tier_order:
    tier_df = filtered[filtered["platform_tier"] == tier]
    if tier_df.empty:
        continue
    st.subheader(tier)
    for _, row in tier_df.iterrows():
        with st.container(border=True):
            top = st.columns([3, 1, 1, 1])
            top[0].markdown(f"### {row['name']}")
            top[0].caption(f"{row['category']} · {row['vendor']}")
            top[1].markdown(
                f":{status_color.get(row['approval_status'], 'gray')}[**{row['approval_status']}**]"
            )
            if row.get("tier_badge"):
                top[1].caption(row["tier_badge"])
            top[2].metric("Seats", f"{row['seats']:,}")
            top[3].metric("Monthly", f"${row['monthly_cost_usd']:,}")

            if row.get("rationale"):
                st.markdown(f"> **Why this tool, my view:** {row['rationale']}")

            info = st.columns(2)
            with info[0]:
                st.markdown(f"**Risk tier:** {row['risk_tier']}")
                st.markdown(f"**Intended users:** {row['intended_users']}")
                st.markdown(f"**Data residency:** {row['data_residency']}")
                st.markdown(f"**SSO:** {'Yes' if row['sso_enabled'] else 'No'}")
            with info[1]:
                st.markdown("**Approved use cases:**")
                if row["approved_use_cases"]:
                    for uc in row["approved_use_cases"]:
                        st.markdown(f"- {uc}")
                else:
                    st.markdown("_None yet_")
                st.markdown(f"**Restrictions:** {row['restrictions']}")
                st.markdown(f"**Owner:** {row['owner']} · **Next review:** {row['review_date']}")

st.divider()

with st.expander("How tools get into this catalog — my intake process"):
    st.markdown(
        """
        1. **Request** — anyone can propose a tool through the intake form (Use Case Marketplace).
        2. **Triage** — I review fit against the two-platform strategy first. *Default answer: "the catalog first."*
        3. **Security + Privacy review** — SSO, data residency, retention, DPIA if needed. Legal/Security in from Day 1, not bolt-on.
        4. **Pilot** — bounded cohort (typically 20–50 seats), 6–8 weeks, **success criteria measured against pre-launch baselines**.
        5. **Approve / decline** — with clear scope. Approved tools enter the catalog with risk tier, intended-user statement, and my rationale.
        6. **Re-review** — every 6 months, or sooner if vendor materially changes the product.
        """
    )
