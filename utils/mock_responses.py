"""Mock response library for the Live Agent — keeps the demo zero-cost.

Set USE_MOCK_RESPONSES=true in .env to route the Live Agent through these
pre-written J.D. Power-format briefings instead of the Claude API. Streaming
is preserved so the user experience still looks live.
"""

from __future__ import annotations

import random
import time
from typing import Iterator

# ---------- Pre-written briefings in the J.D. Power format ----------

_EV_BRIEFING = """**EV adoption — US, current quarter framing**

**Headline:** EV adoption growth in the US has slowed relative to 2023 projections, with affordability, charging infrastructure, and policy uncertainty cited as the three primary friction points across most analyst coverage. Segment differentiation matters — luxury and pure-play makers are diverging from legacy OEM EV programs.

**Why it matters now:**
- Federal EV tax credit changes and tariff policy on imported components are creating short-term demand shocks that are showing up unevenly across OEMs
- Charging infrastructure buildout is uneven by region — coastal markets are approaching density adequacy, but interior states remain materially underserved
- Legacy OEM EV programs are being repositioned (delayed launches, reduced production targets) while pure-play EV makers face margin compression

**Data points to verify:**
- Q1 2026 BEV sales share of total light-duty vehicle sales — verify against the J.D. Power EV Index or the manufacturer's quarterly investor presentations
- Charging station count by state — verify against the U.S. Department of Energy's Alternative Fuels Data Center
- Average transaction price for BEVs vs ICE — verify against the J.D. Power Power Information Network (PIN) data or Cox Automotive

**What to watch next:**
- OEM Q2 2026 earnings calls for capex revisions and EV-program update language
- The next J.D. Power U.S. EV Experience Study, expected later this year

**Confidence:** Medium — directional trend is well-established across multiple data sources; specific share numbers are still moving and worth verifying against primary sources before citing in a client deliverable."""

_HOMEOWNERS_BRIEFING = """**Homeowner's insurance customer dissatisfaction — account-team framing**

**Headline:** Homeowner's insurance customer dissatisfaction has risen materially over the past 18 months, with premium increases, claims-handling friction, and non-renewal communications cited as the top three drivers in recent J.D. Power studies. Carriers are repricing or exiting catastrophe-exposed markets, creating coverage gaps that hit both customer satisfaction and account-team retention conversations.

**Why it matters now:**
- Carriers in catastrophe-exposed states (FL, CA, LA) are repricing or non-renewing in volume — affected customers are arriving at your accounts with frustration baked in
- Average homeowner's premium has increased materially over the past 24 months; exact figures vary by carrier and state, but the direction is consistent across data sources
- Claims-handling cycle times and digital claim experience are diverging sharply between carriers — winners are pulling away on satisfaction scores while laggards lose retention

**Data points to verify:**
- Year-over-year change in the J.D. Power U.S. Home Insurance Study overall satisfaction score — verify against the most recent published study
- Claims cycle-time benchmarks by carrier — verify against the J.D. Power U.S. Property Claims Satisfaction Study
- Non-renewal rates in catastrophe-exposed states — verify against state Department of Insurance filings

**What to watch next:**
- Carrier Q2 earnings calls for combined ratio guidance and catastrophe-loss commentary
- The next J.D. Power Home Insurance Study cycle for satisfaction trajectory

**Confidence:** Medium — directionally well-supported; carrier-specific numbers should be sourced from the studies directly before going into any client deliverable."""

_BANK_APP_BRIEFING = """**US bank app customer experience — analyst orientation**

**Headline:** US retail banking app satisfaction has continued to improve, with mid-size and direct/online-only banks closing the gap on the largest national banks — but the gap has narrowed, not disappeared. AI-powered features (proactive insights, smart categorization, fraud alerts) are moving from differentiator to expected baseline.

**Why it matters now:**
- Card controls and money-movement features remain the highest-leverage satisfaction drivers in app experience — feature parity here is becoming table stakes
- Outage and reliability events are disproportionately damaging — a single notable outage can erase a year of satisfaction gains for a bank
- Direct/online-only banks continue to lead on app satisfaction, but the gap to large nationals is narrower than two years ago

**Data points to verify:**
- Latest J.D. Power U.S. Banking Mobile App Satisfaction Study scores and bank-by-bank ranking — verify against the most recent published study
- App-store ratings as a noisy but timely signal — verify against the iOS App Store and Google Play public ratings
- Outage frequency — verify against Downdetector aggregates and the banks' published service status pages

**What to watch next:**
- Generative-AI feature rollouts planned for 2026 by several large banks, and whether satisfaction lifts on the rollout
- The next J.D. Power Mobile App Satisfaction Study cycle for satisfaction movement

**Confidence:** Medium-High — well-instrumented category with regular J.D. Power coverage and public app-store signals."""

_GENERIC_BRIEFING = """**Industry orientation — your topic**

**Headline:** I don't have a pre-built briefing on that exact topic at hand. Let me give you the right framing instead so you can drive an efficient first hour of research.

**How a J.D. Power analyst should approach this:**
- Identify which industry vertical this sits in — automotive, financial services, insurance, utilities, telecom, travel & hospitality, or healthcare consumer experience
- Frame the question precisely: customer satisfaction trajectory, market structure, a specific event, or a comparison
- Identify the audience: client deliverable, internal account team, or executive summary — the framing changes for each

**Sources worth triangulating:**
- The relevant J.D. Power syndicated study for the vertical (recent publication cycle)
- Primary regulatory or industry filings — SEC, NHTSA, state DOIs, FCC, depending on vertical
- Public-facing reports from established industry analyst houses (cite source *class*, not invented specific titles)

**What to do next:**
- Come back with the vertical and the audience and I'll give you a structured briefing in the J.D. Power format
- For client-facing work, route any deliverable drafting through the sanctioned client-deliverable workflow with the human review layer

**Confidence:** Low on the specific topic without more context. The framing above is high-confidence as an orientation approach."""


def _pick_response(user_message: str) -> str:
    """Keyword-match the user's last message to a pre-built briefing."""
    msg = user_message.lower()

    # EV / electric vehicles
    if any(k in msg for k in ["ev ", "ev adoption", "electric vehicle", "electric car", "evs"]):
        return _EV_BRIEFING
    # Homeowner's insurance
    if any(k in msg for k in ["homeowner", "home insurance", "homeowners"]):
        return _HOMEOWNERS_BRIEFING
    # Insurance generally → use homeowner briefing as nearest match
    if "insurance" in msg and "dissat" in msg:
        return _HOMEOWNERS_BRIEFING
    # Bank app / banking
    if any(k in msg for k in ["bank app", "banking app", "mobile bank", "mobile app"]):
        return _BANK_APP_BRIEFING
    if any(k in msg for k in ["bank", "banking"]) and any(k in msg for k in ["customer", "experience", "cx", "satisfaction", "app"]):
        return _BANK_APP_BRIEFING
    # Fallback
    return _GENERIC_BRIEFING


def stream_mock(user_message: str, seed: int | None = None) -> Iterator[str]:
    """Yield text chunks progressively to simulate Claude's streaming response.

    Chunks of 3-7 characters with small variable delays, plus a slight pause on
    sentence-ending punctuation. Feels live, costs nothing, no key required.
    """
    if seed is not None:
        random.seed(seed)

    response = _pick_response(user_message)

    i = 0
    while i < len(response):
        chunk_size = random.randint(3, 7)
        chunk = response[i:i + chunk_size]
        delay = random.uniform(0.012, 0.028)
        if any(p in chunk for p in ".!?"):
            delay += random.uniform(0.05, 0.11)
        elif any(p in chunk for p in ",;:"):
            delay += random.uniform(0.02, 0.05)
        time.sleep(delay)
        yield chunk
        i += chunk_size
