"""Perficient-themed branding helpers for the AI Enablement Hub.

Call `apply_brand()` at the top of every page (after st.set_page_config)
to apply the global CSS, render the branded header bar, and inject the
custom sidebar navigation.
"""

from __future__ import annotations

import streamlit as st

from utils.auth import require_auth

_BRAND_CSS = """
<style>
/* Warm off-white page background with subtle gradient — no plain white */
.stApp {
    background: linear-gradient(180deg, #F7F4F0 0%, #EFE9E1 100%);
}

/* Sidebar — deep navy panel */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1A2238 0%, #0F1729 100%);
    padding-top: 0 !important;
}
[data-testid="stSidebar"] * {
    color: #F7F4F0 !important;
}
[data-testid="stSidebar"] a {
    color: #F4C842 !important;
}

/* Hide the default auto-generated page nav so we can show our own */
[data-testid="stSidebarNav"] {
    display: none !important;
}

/* Custom sidebar brand block */
.perficient-sidebar-brand {
    background: linear-gradient(135deg, #003D82 0%, #8C1623 100%);
    color: #FFFFFF !important;
    padding: 18px 18px 16px;
    margin: -8px -16px 14px;
    border-radius: 0 0 10px 10px;
    text-align: left;
    box-shadow: 0 4px 12px rgba(0,0,0,0.25);
}
.perficient-sidebar-brand .jp-mark {
    background: #FFFFFF;
    color: #003D82 !important;
    padding: 3px 8px;
    border-radius: 4px;
    font-weight: 900;
    font-size: 14px;
    letter-spacing: 1px;
    margin-right: 6px;
}
.perficient-sidebar-brand .jp-name {
    font-weight: 800;
    font-size: 16px;
    letter-spacing: 1.5px;
    color: #FFFFFF !important;
}
.perficient-sidebar-brand .jp-sub {
    display: block;
    font-size: 13px;
    font-weight: 500;
    color: #F7F4F0 !important;
    opacity: 0.95;
    margin-top: 6px;
}
.perficient-sidebar-brand .jp-tag {
    display: inline-block;
    font-size: 10px;
    color: #1A2238 !important;
    background: #F4C842;
    padding: 2px 8px;
    border-radius: 10px;
    margin-top: 8px;
    font-weight: 700;
    letter-spacing: 0.5px;
}

/* Sidebar section labels */
.perficient-nav-section {
    color: #F4C842 !important;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin: 18px 0 6px 6px;
    opacity: 0.85;
}

/* Sidebar page-link rows: indent child pages, hover state */
[data-testid="stSidebar"] [data-testid="stPageLink-NavLink"] {
    padding-left: 18px !important;
    border-radius: 6px;
    transition: background 0.15s;
}
[data-testid="stSidebar"] [data-testid="stPageLink-NavLink"]:hover {
    background: rgba(244, 200, 66, 0.12);
}
[data-testid="stSidebar"] .jp-home [data-testid="stPageLink-NavLink"] {
    padding-left: 8px !important;
    font-weight: 700;
}

/* Branded header bar at the top of every page */
.perficient-header {
    background: linear-gradient(90deg, #003D82 0%, #8C1623 100%);
    color: #FFFFFF;
    padding: 16px 26px;
    border-radius: 10px;
    margin-bottom: 22px;
    box-shadow: 0 4px 14px rgba(190, 30, 45, 0.18);
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.perficient-header .brand {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-weight: 800;
    font-size: 22px;
    letter-spacing: 2px;
}
.perficient-header .brand-mark {
    background: #FFFFFF;
    color: #003D82;
    padding: 4px 10px;
    border-radius: 4px;
    margin-right: 10px;
    font-weight: 900;
}
.perficient-header .sub {
    font-size: 13px;
    font-weight: 400;
    opacity: 0.92;
}

/* Metric tiles */
[data-testid="stMetric"] {
    background: #FFFFFF;
    border-radius: 10px;
    padding: 14px 18px;
    box-shadow: 0 2px 8px rgba(26, 34, 56, 0.08);
    border-left: 4px solid #003D82;
}

/* Bordered containers (st.container(border=True)) */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #FFFFFF !important;
    border: 1px solid rgba(26, 34, 56, 0.08) !important;
    box-shadow: 0 2px 10px rgba(26, 34, 56, 0.05);
    border-radius: 10px;
}

/* Section dividers */
hr {
    border-color: rgba(190, 30, 45, 0.18) !important;
}

/* Headings */
h1, h2, h3 {
    color: #1A2238 !important;
}

/* Captions */
.stCaption, [data-testid="stCaptionContainer"] {
    color: #5A6378 !important;
}

/* Page link buttons inside the main content (card grid) */
.main [data-testid="stPageLink"] a {
    color: #003D82 !important;
    font-weight: 600;
}

/* Tables */
[data-testid="stDataFrame"] {
    background: #FFFFFF;
    border-radius: 8px;
    padding: 4px;
}

/* Expander */
[data-testid="stExpander"] {
    background: #FFFFFF;
    border-radius: 8px;
    border: 1px solid rgba(26, 34, 56, 0.08);
}

/* Buttons */
.stButton > button {
    background: #003D82;
    color: #FFFFFF;
    border: none;
    font-weight: 600;
    border-radius: 6px;
}
.stButton > button:hover {
    background: #8C1623;
    color: #FFFFFF;
}

/* Chat input/messages on Live Agent */
[data-testid="stChatMessage"] {
    background: #FFFFFF;
    border-radius: 10px;
    padding: 10px;
}
</style>
"""

_SIDEBAR_BRAND_HTML = """
<div class="jdpower-sidebar-brand">
    <div>
        <span class="jp-mark">P</span><span class="jp-name">ERFICIENT</span>
    </div>
    <span class="jp-sub">AI Adoption Operating Model</span>
    <span class="jp-tag">v1 · proven framework</span>
</div>
"""


def _render_sidebar_nav() -> None:
    """Custom sidebar nav — branded, grouped, indented."""
    with st.sidebar:
        st.markdown(_SIDEBAR_BRAND_HTML, unsafe_allow_html=True)

        # Home link — slightly elevated styling vs child pages
        st.markdown('<div class="jp-home">', unsafe_allow_html=True)
        st.page_link("app.py", label="◆  Hub Home", icon=None)
        st.markdown("</div>", unsafe_allow_html=True)

        # Tools & governance group
        st.markdown('<div class="jdpower-nav-section">Tools & Governance</div>', unsafe_allow_html=True)
        st.page_link("pages/1_Tools_Catalog.py", label="Tools Catalog")
        st.page_link("pages/5_Responsible_AI.py", label="Responsible AI")
        st.page_link("pages/6_Prompt_Library.py", label="Prompt Library")

        # Adoption & people group
        st.markdown('<div class="jdpower-nav-section">Adoption & People</div>', unsafe_allow_html=True)
        st.page_link("pages/2_Use_Case_Marketplace.py", label="Use Case Marketplace")
        st.page_link("pages/3_Champions_Network.py", label="Champions Network")
        st.page_link("pages/8_Training_Personas.py", label="Training & Personas")
        st.page_link("pages/4_Adoption_Metrics.py", label="Adoption Metrics")

        # Live agent group
        st.markdown('<div class="jdpower-nav-section">Live Agent</div>', unsafe_allow_html=True)
        st.page_link("pages/7_Live_Agent.py", label="Industry Insight Assistant")


def apply_brand(page_label: str | None = None) -> None:
    """Inject brand CSS, gate on auth, render header + custom sidebar nav."""
    st.markdown(_BRAND_CSS, unsafe_allow_html=True)
    # Gate before rendering anything else — login form will st.stop() if needed
    require_auth()
    _render_sidebar_nav()
    right_label = page_label or "Governed by design"
    st.markdown(
        f"""
<div class="jdpower-header">
    <div>
        <span class="brand"><span class="brand-mark">P</span>ERFICIENT</span>
        &nbsp;&nbsp;<span class="sub">AI Adoption Operating Model</span>
    </div>
    <div class="sub">{right_label}</div>
</div>
""",
        unsafe_allow_html=True,
    )
