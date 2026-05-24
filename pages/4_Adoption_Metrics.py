"""Adoption Metrics — executive view with pre-launch baselines and per-user budget dashboards."""

from __future__ import annotations

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from utils.brand import apply_brand
from utils.data_loader import load_bu_adoption, load_metrics, load_use_cases

st.set_page_config(page_title="Adoption Metrics · AI Enablement Hub", layout="wide")
apply_brand("Adoption Metrics · Baseline-anchored")

st.title("Adoption Metrics")
st.caption(
    "**My approach to ROI:** establish baselines *before* any tool goes live, then measure against them. "
    "Productivity gains are only defensible when measured against a documented pre-tool reality, not a remembered one."
)

metrics = load_metrics()
bu_df = load_bu_adoption()
uc_df = load_use_cases()

latest = metrics.iloc[-1]
prev = metrics.iloc[-2]


def delta_pct(curr: float, prior: float) -> str:
    if prior == 0:
        return "n/a"
    return f"{(curr - prior) / prior * 100:+.0f}%"


# ---------- Headline KPIs ----------
c1, c2, c3, c4 = st.columns(4)
c1.metric(
    "Monthly active users",
    f"{int(latest['active_users']):,}",
    delta_pct(latest["active_users"], prev["active_users"]),
)
c2.metric(
    "Hours saved (month)",
    f"{int(latest['hours_saved']):,}",
    delta_pct(latest["hours_saved"], prev["hours_saved"]),
)
c3.metric("Use cases in production", int(latest["production_use_cases"]))
c4.metric("Trained employees", f"{int(latest['trained_employees']):,}")

st.divider()

# ---------- Pre-launch baselines ----------
st.subheader("Pre-launch baselines vs current — by workflow")
st.caption(
    "Baselines measured in the 6 weeks **before** any tool went live. Current measurements are post-rollout. "
    "Difference attributable to the program — defensible to a PE owner because we measured what was there first."
)

baselines = pd.DataFrame([
    {
        "workflow": "Insight drafting (analyst)",
        "baseline_hours": 8.5,
        "current_hours": 5.2,
        "delta_pct": -38.8,
        "baseline_method": "Time-and-motion study, 24 analysts, 6-week pre-launch window",
        "sample_size": 24,
    },
    {
        "workflow": "Syndicated study analysis (researcher)",
        "baseline_hours": 14.0,
        "current_hours": 9.7,
        "delta_pct": -30.7,
        "baseline_method": "Self-reported diary studies, 18 researchers, 6-week pre-launch window",
        "sample_size": 18,
    },
    {
        "workflow": "Client deliverable QA (consultant)",
        "baseline_hours": 6.0,
        "current_hours": 4.3,
        "delta_pct": -28.3,
        "baseline_method": "QA cycle timestamps + sample review, 12 consultants, 6 weeks",
        "sample_size": 12,
    },
    {
        "workflow": "Account briefing prep (client services)",
        "baseline_hours": 3.2,
        "current_hours": 1.9,
        "delta_pct": -40.6,
        "baseline_method": "Self-reported time logs, 30 reps, 4-week pre-launch window",
        "sample_size": 30,
    },
    {
        "workflow": "Meeting summary turnaround (all)",
        "baseline_hours": 0.75,
        "current_hours": 0.20,
        "delta_pct": -73.3,
        "baseline_method": "Calendar-to-summary timestamps, all-hands sample, 4 weeks",
        "sample_size": 88,
    },
])

fig = go.Figure()
fig.add_trace(go.Bar(
    name="Baseline (pre-launch)",
    y=baselines["workflow"],
    x=baselines["baseline_hours"],
    orientation="h",
    marker_color="#5A6378",
    text=baselines["baseline_hours"].apply(lambda x: f"{x:.1f}h"),
    textposition="outside",
))
fig.add_trace(go.Bar(
    name="Current (post-rollout)",
    y=baselines["workflow"],
    x=baselines["current_hours"],
    orientation="h",
    marker_color="#BE1E2D",
    text=baselines["current_hours"].apply(lambda x: f"{x:.1f}h"),
    textposition="outside",
))
fig.update_layout(
    barmode="group",
    xaxis_title="Hours per task",
    yaxis_title="",
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    legend=dict(orientation="h", y=-0.15),
    margin=dict(l=10, r=10, t=10, b=10),
    height=380,
)
st.plotly_chart(fig, use_container_width=True)

with st.expander("Baseline methodology — how each was measured pre-launch"):
    st.markdown(
        """
        Every baseline was measured **before the tool went live for that persona**. We did this in three ways
        depending on workflow:

        - **Time-and-motion observation** — analyst sat with practitioners and clocked discrete sub-steps.
          Used for insight drafting.
        - **Self-reported diary studies** — practitioners logged time on defined activities for 4–6 weeks.
          Used for research workflows.
        - **System-derived timestamps** — calendar invites, doc creation/modification times, ticket lifecycles.
          Used for meeting summaries and account briefings.

        Why this matters: most enterprise AI ROI claims fail scrutiny because the baseline was constructed
        *from memory* after the tool was already in use. That's not a baseline — it's an estimate of what
        people remember. My discipline is to measure *before* anything changes, then attribute the delta.
        """
    )

st.markdown("**Baseline detail (sample sizes, methodology):**")
st.dataframe(
    baselines.rename(columns={
        "workflow": "Workflow",
        "baseline_hours": "Baseline (hrs)",
        "current_hours": "Current (hrs)",
        "delta_pct": "Δ %",
        "baseline_method": "Baseline method",
        "sample_size": "n",
    }),
    use_container_width=True,
    hide_index=True,
)

st.divider()

# ---------- Per-user AI budget dashboard ----------
st.subheader("Per-user AI budgets — my strongest cost-discipline lever")
st.caption(
    "Every employee gets a monthly AI usage budget with a live dashboard, daily-consumption alerts at threshold, "
    "and no rollover. Single biggest lever for responsible adoption velocity I've seen — cost becomes personal "
    "awareness, not a finance abstraction."
)

# ---------- Aggregate budget metrics ----------
budget_total = 920
budget_under = 758
budget_warning = 124
budget_over = 38
mean_pct_used = 64

bc1, bc2, bc3, bc4 = st.columns(4)
bc1.metric("Active budgeted users", f"{budget_total:,}")
bc2.metric(
    "Within budget", f"{budget_under:,}", f"{budget_under/budget_total*100:.0f}%"
)
bc3.metric(
    "Threshold alert (>80%)", f"{budget_warning:,}", f"{budget_warning/budget_total*100:.0f}%"
)
bc4.metric(
    "Over budget (capped)", f"{budget_over:,}", f"{budget_over/budget_total*100:.0f}%"
)

# ---------- Sample user daily consumption (illustrative) ----------
st.markdown("**Illustrative daily consumption — a single user (analyst, $80 monthly budget):**")

np.random.seed(42)
days = pd.date_range("2026-05-01", periods=23)
daily_spend = np.cumsum(np.random.gamma(2.0, 1.4, len(days)))
df_user = pd.DataFrame({"date": days, "cumulative_spend_usd": daily_spend, "budget": 80})

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df_user["date"], y=df_user["cumulative_spend_usd"],
    mode="lines+markers",
    name="Cumulative spend",
    line=dict(color="#BE1E2D", width=3),
    fill="tozeroy",
    fillcolor="rgba(190, 30, 45, 0.15)",
))
fig.add_hline(y=80, line_dash="dash", line_color="#1A2238",
              annotation_text="Monthly budget $80", annotation_position="top left")
fig.add_hline(y=64, line_dash="dot", line_color="#F4C842",
              annotation_text="Alert at 80%", annotation_position="bottom left")
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="USD",
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    height=320,
    margin=dict(l=10, r=10, t=10, b=10),
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("**Budget distribution across the active user population:**")
budget_bins = pd.DataFrame({
    "band": ["0–25%", "25–50%", "50–80%", "80–100%", ">100% (capped)"],
    "users": [142, 286, 330, 124, 38],
})
fig = px.bar(
    budget_bins, x="band", y="users", color="band",
    color_discrete_map={
        "0–25%": "#A8C5DA",
        "25–50%": "#6FA0C0",
        "50–80%": "#3D7BA8",
        "80–100%": "#F4C842",
        ">100% (capped)": "#BE1E2D",
    },
    labels={"band": "% of monthly budget used", "users": "Users"},
)
fig.update_layout(
    showlegend=False, plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
    margin=dict(l=10, r=10, t=10, b=10), height=300,
)
st.plotly_chart(fig, use_container_width=True)

with st.expander("How the per-user budget mechanic works"):
    st.markdown(
        """
        - Each persona gets a default monthly budget (analyst $80, consultant $120, exec $200, etc.).
          Budgets can be adjusted per role with a documented business reason.
        - Usage is routed through Portkey, so we see real per-user, per-model, per-workflow consumption.
        - At **80% of budget**, the user gets a Slack/email alert showing what's driving the spend.
        - At **100%**, the user is **capped**, not cut off — they can request an extension via the Hub with a
          one-line justification, approved within 24 hours.
        - Budgets reset monthly with **no rollover**. This is deliberate: rollover creates hoarding behavior
          and breaks the cost-as-personal-awareness signal.

        This was the single biggest behavioral lever I deployed at Toyota — moves cost from a finance
        abstraction into a personal awareness, and turns AI adoption into a self-managed system.
        """
    )

st.divider()

# ---------- Time series ----------
st.subheader("Adoption over time")

tab1, tab2, tab3 = st.tabs(["Active users", "Hours saved", "Use cases in production"])

with tab1:
    fig = px.area(
        metrics,
        x="month",
        y=["weekly_active_users", "active_users"],
        labels={"value": "Users", "variable": "Metric", "month": ""},
        title=None,
        color_discrete_sequence=["#5A6378", "#BE1E2D"],
    )
    fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    fig = px.bar(metrics, x="month", y="hours_saved", labels={"month": "", "hours_saved": "Hours saved"})
    fig.update_traces(marker_color="#BE1E2D")
    fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    fig = px.line(
        metrics,
        x="month",
        y=["production_use_cases", "pilots"],
        labels={"value": "Count", "variable": "", "month": ""},
        markers=True,
        color_discrete_sequence=["#BE1E2D", "#F4C842"],
    )
    fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# ---------- BU rollout ----------
st.subheader("Rollout by business unit")

fig = px.bar(
    bu_df.sort_values("adoption_pct", ascending=True),
    x="adoption_pct",
    y="business_unit",
    orientation="h",
    color="adoption_pct",
    color_continuous_scale=["#F4C842", "#BE1E2D"],
    labels={"adoption_pct": "% of BU active monthly", "business_unit": ""},
)
fig.update_layout(coloraxis_showscale=False, plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig, use_container_width=True)

st.dataframe(
    bu_df.rename(
        columns={
            "business_unit": "Business unit",
            "active_users": "Active users",
            "headcount": "Headcount",
            "adoption_pct": "Adoption %",
            "use_cases_in_prod": "Use cases in prod",
            "hours_saved_ytd": "Hours saved YTD",
        }
    ),
    use_container_width=True,
    hide_index=True,
)

st.divider()

# ---------- Where the value is concentrated ----------
st.subheader("Where the value is concentrated")
top_uc = (
    uc_df.sort_values("annualized_hours_saved", ascending=False)
    .head(8)
    .rename(
        columns={
            "title": "Use case",
            "business_unit": "BU",
            "stage": "Stage",
            "annualized_hours_saved": "Hours / yr",
            "owner": "Owner",
        }
    )[["Use case", "BU", "Stage", "Hours / yr", "Owner"]]
)
st.dataframe(top_uc, use_container_width=True, hide_index=True)

with st.expander("Metrics I track — and metrics I refuse to track as primaries"):
    st.markdown(
        """
        **Primaries:**
        - **Monthly active users** by BU and persona, with depth (sessions, workflows per user)
        - **Workflow time-to-completion** vs pre-rollout baselines (the chart above)
        - **Hours saved × loaded cost by role** — the P&L number for CEO and owner
        - **Cost discipline** — $/active user/month, $/workflow, % usage within budget thresholds

        **Refused as primaries:**
        - *Count of AI initiatives* — useful inventory, not a north star
        - *AI seats deployed* — seats without active usage are vanity. We report active users, not licensees.

        Initiative and seat counts are the metrics that look good for a quarter and then quietly stop
        moving when adoption stalls. The PE owner will see through them. I'd rather report harder numbers
        that survive scrutiny.
        """
    )
