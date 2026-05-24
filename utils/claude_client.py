"""Thin wrapper around the Anthropic Claude API used by the live agent page.

Reads ANTHROPIC_API_KEY from environment or Streamlit secrets so the same code
works locally (via .env) and on Streamlit Community Cloud (via secrets manager).

When USE_MOCK_RESPONSES=true (default for demos), routes through mock_responses
to avoid API cost and key dependency.
"""

from __future__ import annotations

import os

import streamlit as st
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

DEFAULT_MODEL = "claude-sonnet-4-6"


def _use_mock() -> bool:
    """True when the Live Agent should serve pre-written briefings instead of calling Claude."""
    return os.environ.get("USE_MOCK_RESPONSES", "true").lower() in ("true", "1", "yes")


def _resolve_api_key() -> str | None:
    if key := os.environ.get("ANTHROPIC_API_KEY"):
        return key
    try:
        return st.secrets["ANTHROPIC_API_KEY"]
    except (KeyError, FileNotFoundError, st.errors.StreamlitSecretNotFoundError):
        return None


def get_client() -> Anthropic | None:
    """Return an Anthropic client, or None in mock mode / when no key is configured."""
    if _use_mock():
        # Sentinel — the page guard treats this as "client available" so the chat UI renders.
        # Actual requests are intercepted by stream_response and served from mock_responses.
        return _MOCK_SENTINEL
    key = _resolve_api_key()
    if not key:
        return None
    return Anthropic(api_key=key)


class _MockSentinel:
    """Placeholder returned by get_client() in mock mode."""

    def __repr__(self) -> str:  # pragma: no cover - debug helper
        return "<MockSentinel>"


_MOCK_SENTINEL = _MockSentinel()


def stream_response(
    system_prompt: str,
    messages: list[dict],
    model: str = DEFAULT_MODEL,
    max_tokens: int = 1024,
):
    """Yield text chunks from Claude (or the mock library) as they stream in.

    Caller is responsible for handling the absence of an API key (get_client returns None).
    """
    # Mock mode — serve pre-written J.D. Power briefings, no API call.
    if _use_mock():
        from utils.mock_responses import stream_mock

        last_user = next(
            (m["content"] for m in reversed(messages) if m["role"] == "user"),
            "",
        )
        yield from stream_mock(last_user)
        return

    # Real API path.
    client = get_client()
    if client is None or isinstance(client, _MockSentinel):
        yield "[No ANTHROPIC_API_KEY configured. Set it in .env locally or in Streamlit Cloud secrets.]"
        return

    with client.messages.stream(
        model=model,
        max_tokens=max_tokens,
        system=[
            {
                "type": "text",
                "text": system_prompt,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=messages,
    ) as stream:
        for text in stream.text_stream:
            yield text
