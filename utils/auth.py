"""Simple password gate for the JD Power AI Enablement Hub portal.

One shared access code, resolved from Streamlit Cloud secrets or env var.
Once a user enters the correct code, they're authenticated for the browser
session.

Behavior:
- If APP_PASSWORD is not configured, access is open (useful for local dev)
- If configured, every page calls `require_auth()` before rendering content;
  unauthenticated users see a branded password screen
- Auth state lives in `st.session_state["_auth_ok"]` — survives page navigation
  within the session, clears when the browser tab closes
"""

from __future__ import annotations

import hmac
import os

import streamlit as st


def _get_password() -> str:
    """Resolve the access password from Streamlit secrets, then env."""
    try:
        return st.secrets["APP_PASSWORD"]
    except (KeyError, FileNotFoundError, st.errors.StreamlitSecretNotFoundError):
        pass
    return os.environ.get("APP_PASSWORD", "")


def _render_login_screen(expected_present: bool, error: str | None) -> None:
    """Render the centered, branded login form."""
    st.markdown(
        """
<style>
/* Hide sidebar entirely on the login screen */
[data-testid="stSidebar"] { display: none !important; }
/* Center the login card */
.jp-login-wrap {
    max-width: 460px;
    margin: 90px auto 40px;
}
</style>
""",
        unsafe_allow_html=True,
    )

    st.markdown('<div class="jp-login-wrap">', unsafe_allow_html=True)
    st.markdown(
        """
<div class="jdpower-header" style="margin-bottom: 24px;">
    <div>
        <span class="brand"><span class="brand-mark">JD</span>POWER</span>
        &nbsp;&nbsp;<span class="sub">AI Enablement Hub</span>
    </div>
    <div class="sub">Access required</div>
</div>
""",
        unsafe_allow_html=True,
    )

    with st.container(border=True):
        st.markdown("### Authorized access only")
        st.caption(
            "This portal is a working prototype built for the JD Power Head of AI "
            "Enablement Hub conversation. Please enter the access code shared with you."
        )

        with st.form(key="jp_login_form", clear_on_submit=False):
            pwd = st.text_input(
                "Access code",
                type="password",
                placeholder="Enter access code...",
                key="_pwd_input",
                label_visibility="collapsed",
            )
            submitted = st.form_submit_button("Unlock portal", type="primary")
            if submitted:
                _check_and_set(pwd)

        if error:
            st.error(error)
        if not expected_present:
            st.warning(
                "⚠ No `APP_PASSWORD` is configured. The portal is currently open to "
                "anyone with the URL. Set `APP_PASSWORD` in Streamlit secrets before sharing."
            )

    st.markdown("</div>", unsafe_allow_html=True)


def _check_and_set(pwd: str) -> None:
    """Compare the submitted password to the expected value and update session state."""
    expected = _get_password()
    if expected and hmac.compare_digest(pwd or "", expected):
        st.session_state["_auth_ok"] = True
        st.session_state.pop("_pwd_input", None)
        st.rerun()
    else:
        st.session_state["_auth_error"] = "Incorrect access code. Try again."


def require_auth() -> None:
    """Block the page until the user has entered the correct access code.

    Call this from `apply_brand()` so every page is gated automatically.
    Safe to call repeatedly — returns immediately when already authenticated.
    """
    expected = _get_password()

    # No password configured → open access (typical local dev)
    if not expected:
        return

    # Already authenticated
    if st.session_state.get("_auth_ok", False):
        return

    # Render login form, halt the page
    error = st.session_state.pop("_auth_error", None)
    _render_login_screen(expected_present=bool(expected), error=error)
    st.stop()
