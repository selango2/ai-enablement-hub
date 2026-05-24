"""Prompt Library — vetted prompts mapped to research and analyst workflows."""

from __future__ import annotations

import streamlit as st

from utils.brand import apply_brand
from utils.data_loader import load_prompts

st.set_page_config(page_title="Prompt Library · AI Enablement Hub", layout="wide")
apply_brand("Prompt Library · Vetted patterns")

st.title("Prompt Library")
st.caption(
    "Reviewed and versioned prompts that encode our quality standards. "
    "Every prompt names a category, audience, approved tools, and review status."
)

prompts = load_prompts()

# ---------- Filters ----------
categories = sorted({p["category"] for p in prompts})
audiences = sorted({p["audience"] for p in prompts})

f1, f2, f3 = st.columns(3)
cat_filter = f1.multiselect("Category", categories, default=categories)
aud_filter = f2.multiselect("Audience", audiences, default=audiences)
search = f3.text_input("Search", placeholder="briefing, verbatim, ...")

filtered = [
    p
    for p in prompts
    if p["category"] in cat_filter
    and p["audience"] in aud_filter
    and (search.lower() in (p["title"] + p["prompt"]).lower() if search else True)
]

st.markdown(f"**{len(filtered)} prompts**")
st.divider()

# ---------- Cards ----------
for p in filtered:
    with st.container(border=True):
        top = st.columns([3, 1])
        top[0].markdown(f"### {p['title']}")
        top[0].caption(f"{p['category']} · {p['audience']} · Tools: {', '.join(p['tools'])}")
        top[1].markdown(f":green[**{p['review_status']}**]")

        st.code(p["prompt"], language="markdown")

        actions = st.columns([1, 1, 4])
        actions[0].button("Copy", key=f"copy_{p['title']}", help="In a real deploy this would copy to clipboard")
        actions[1].button("Suggest edit", key=f"edit_{p['title']}")

st.divider()

with st.expander("How prompts get into the library"):
    st.markdown(
        """
        1. **Drafted** by a Champion or hub member, paired with a sample input/output.
        2. **Eval'd** against a small held-out set — at minimum: format correctness,
           refusal behavior, source-grounding where applicable.
        3. **Reviewed** by Methodology Office for any prompt that affects research output.
        4. **Versioned** in this library; older versions stay accessible for reproducibility.
        5. **Re-reviewed** when the underlying model changes meaningfully (e.g., new model family).
        """
    )
