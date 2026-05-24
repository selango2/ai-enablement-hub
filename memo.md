**MEMO**

**To:** Chief Product and Technology Officer, JD Power
**From:** Elango Santhanam
**Re:** Head of AI Enablement Hub — first 90 days, operating approach, and recommendations
**Date:** 2026-05-23

---

## 1. The situation as I read it

The Hub is not greenfield. Scaffolding is in place — 56+ tracked initiatives, an emerging Champions network, a Steering Committee, an externally-presented governance approach, a $400K year-one tool budget. The gap is not strategy. It is execution velocity, and the cost of that gap is compounding daily.

In parallel: three BUs on independently-purchased ChatGPT Team licenses (one drafting an OEM benchmarking deliverable shipping next month), an FS consultant feeding confidential client transcripts into a custom GPT, the CDAO shipping three internal tools without Hub coordination. This is what motivated, time-pressured people do when the sanctioned path is slower than the unsanctioned one. **My job in six months is to make the sanctioned path the path of least resistance**, while closing the highest-risk exposures fast.

## 2. Operating model — what the Hub owns and does not own

**My approach is conviction-led, supported by experience.** I built and ran a centralized AI Hub at **Toyota** across product, Agile, HR, finance, accounting, legal, procurement, and executive teams — the same shape of mostly-non-engineering workforce JD Power has. The recommendations here are mine; Toyota is the proof. The Hub is the **central nervous system**, not a delivery organization. For the first six months I am that nervous system — I set the standards, evaluate the platforms, codify governance, run the measurement framework, and unblock the Champions. BUs deliver. That separation, not headcount, is what makes the model scale.

**What I own as the Hub:** the tool catalog and evaluation process; governance policy (with Legal, Risk, HR); cross-BU intake and prioritization; the Champions program and AI literacy framework (with HR); value measurement and the board narrative; centralized observability and cost control.

**What I do not own:** BU-specific execution (Champions run it); the CDAO's production data and analytics workflows; individual tool roadmaps; approval of every use case — only those above a defined risk threshold.

**CEO, 30 seconds:** *The Hub is the central nervous system for AI at JD Power. It sets standards, evaluates platforms, runs governance, measures impact, and gives you one number on adoption and value. BUs run the work; I make sure they can do it safely, fast, and visibly.*

**Research Director, 30 seconds:** *The Hub is where you go to find approved tools, skip the procurement headache, and get help. I'm not adding approvals you don't need. I'm making sure you don't trip a wire that costs the firm a client.*

Same operating model, framed for two audiences — not two memos.

## 3. The three live situations, answered now

How these are handled sets the precedent. Week one I listen — through direct conversations with the research director, the FS consultant and his practice lead, the CDAO, Legal, and Risk. I act in week two, prioritized by risk. Fast, not impulsive.

**(a) Research team drafting an OEM-bound deliverable in ChatGPT Team.** Stopping it is wrong. Letting it ship as-is is wrong. Week one is a direct conversation with the research director — not a memo through Legal. I acknowledge the workflow is producing value; I am explicit about the risk — a benchmarking deliverable drafted in an unreviewed tool, going to a major OEM, no audit trail of inputs. By week two I bring Legal in for a 48-hour read on IP and contractual exposure. I run two parallel tracks: (1) ship this deliverable with a one-time governance wrap — Legal sign-off on inputs, manual output review against sources, a usage log; (2) within 30 days I deliver the team a sanctioned enterprise workflow they prefer because it's faster and won't get them in trouble. Governance shows up to make the workflow safe, not to take it away.

**(b) FS consultant's custom GPT on confidential client transcripts.** Higher risk: confidential client data, no enterprise account, no audit trail. Accelerated clock — the data exposure is already in flight, so this moves faster than the week-1-listen / week-2-act rhythm. Week one conversation with the consultant and his practice lead, framed as *"I can't let you carry this risk alone,"* not as discipline. I pause the workflow by the end of that conversation pending a Legal read. Within 30 days I deliver a sanctioned equivalent on enterprise infrastructure with the same insight-summary output. If we can't ship that fast, an interim policy (redacted inputs only) with a hard replacement date.

**(c) The CDAO.** Absorbing their work is wrong organizationally and self-defeating practically. Ignoring them produces two AI agendas and confused stakeholders. Week one: a listening 1:1 to understand their agenda, the three tools they've shipped, and where they see the boundary. Week two I bring a draft written split for discussion. **Proposed line:** *CDAO owns production data/analytics workflows and the models embedded in them; the Hub owns enterprise-wide enablement, the tool catalog, governance-of-use, the Champions network, and adoption measurement. We co-own governance standards, model evaluation criteria, and a single shared inventory of what's running in production.* At the next Steering Committee, I propose the CDAO co-chairs with me. That makes coordination structural, not personal.

## 4. Intake, governance, and responsible AI

**Intake.** I operationalize a two-track intake by week three. Track A (BU-led): low-risk use cases stay with the BU through the Champion, with Hub visibility but no approval bottleneck. Track B (Hub-led): use cases touching client data, shipping to clients, using confidential third-party material, or crossing BU boundaries — I run structured intake with Legal, Risk, and the CDAO at the table from the start. I make the 56+ initiative tracker the system of record for Track B and a visibility layer for Track A.

**Governance.** I codify the externally-presented approach as a **4-page internal operating policy** within 30 days — not a 40-page binder no one reads. It covers data classification, model usage boundaries by risk tier, client-facing content guardrails, escalation paths, and acceptable-use for shadow patterns being sunsetted. **My strongest recommendation:** embed Legal, Security, and Compliance in evaluation and onboarding from Day 1 — not bolt-on after the tool is in use. Highest-leverage governance move available; I made this call at Toyota with payoff (faster approvals, fewer escalations). At JD Power, Legal and Risk are partners *in* the Hub, not approvers *after* it.

## 5. Tool strategy and the $400K allocation

**My principle: consolidation over proliferation, but not single-vendor.** I stand up two general-purpose platforms by design — a productivity baseline from the Microsoft/OpenAI family, and Claude Enterprise for analytical and high-judgment workloads. Productivity drafting and reasoning-heavy analysis are different jobs benefiting from different model strengths; the split also gives the Hub real evaluation data across families and reduces single-vendor lock-in. **Hard-won lesson:** choose the strategic set against non-engineering workflows, not engineering defaults. Highest-leverage tool decision I made at Toyota.

Year-one allocation (illustrative; refined after a 2-week BU evaluation in weeks 2–4):

- **~$150K — Productivity-suite LLM. ChatGPT Enterprise — approved.** Sanctions and upgrades the three BUs already on ChatGPT Team licenses, turning shadow usage into a governed enterprise workflow. Covers the non-engineering productivity baseline — drafting, summarization, meeting transcription, email triage, document Q&A. ~400 seats for analysts, client services, ops, executive support. **Microsoft Copilot for M365 held under review** in a 50-seat pilot, pending MS-alignment confirmation in the 2-week BU evaluation.
- **~$170K — Claude Enterprise + Claude Code. Non-negotiable.** Claude Enterprise for complex reasoning, long-document analysis on syndicated studies and benchmarking material, agentic workflows, and client-facing work where evidence-led tone and refusal-to-fabricate matter — where Claude consistently outperforms. Claude Code as the sanctioned coding assistant for engineering: agentic, integrated into the developer environment, and governed under the same Anthropic relationship — one vendor, one observability surface, one procurement contract. ~200 Enterprise seats across senior analysts, consultants, research teams, and the Hub, plus ~80–100 Claude Code seats across engineering.
- **~$50K — Observability and governance tooling.** **Portkey** (or equivalent) as a centralized control plane — routing, monitoring, and policy enforcement across models and agents. **Non-negotiable**, in my view. I deployed this at Toyota: without a single pane of glass on usage, cost, and risk, governance is a posture, not a practice.
- **~$30K — Buffer** for pilots and contingency.

I hold specialized agent/RAG tools for year two — once baseline data shows what the two platforms cover and where the gaps are. No long tail of single-team licenses; tools not in the catalog get evaluated, default answer *"the catalog first."*

**Per-user budgets — my strongest recommendation on cost discipline.** Allocate every employee a monthly AI usage budget with a live dashboard, daily-consumption alerts, and no rollover. Single biggest lever for responsible adoption velocity I've seen — cost becomes personal awareness, not finance abstraction. Implemented at Toyota; same model at JD Power within 60 days.

**HR's request for a recommended tools list:** I deliver it in 30 days. Until then, the public answer is *"use the sanctioned ChatGPT Team licenses with interim guidance — no client PII, no confidential interview content."* Honest holding answer, not stalling.

## 6. Workforce enablement, training, and the Champions network

Two-thirds of JD Power's workforce are analysts, researchers, consultants, and client services. **Engineering-defaulted enablement will fail here.** **My recommendation: a hub-and-spoke operating model to scale enablement, training, and ongoing support.** The Hub builds curriculum, owns standards, runs certification; spokes — Champions embedded in each BU — deliver training, run office hours, and handle day-to-day questions in functional context. This is how a small central team scales to a non-engineering workforce. I built it this way at Toyota — same model at JD Power.

- **Persona-based training tracks, not generic AI literacy.** Tracks for Analyst, Researcher, Consultant, Client Services, Operations, Executive, Engineer. Each is a four-session arc — what AI is, what's approved, hands-on practice on the actual workflows that role performs, and governance/acceptable-use. Designed with Champions so examples are real, not synthetic. Certification on completion, tracked in the HR learning platform.
- **Training as the gate to tool access — my recommendation.** I gate per-user AI budgets and sanctioned tool licenses behind persona-track completion. Cleanest adoption lever I've seen — employees self-pace because the carrot is access, not because HR is chasing them. Also a clean adoption funnel for the Hub to measure. Proven at Toyota.
- **Ongoing support — the spoke layer.** Weekly Champion-led office hours per BU. A single AI-questions channel monitored by Champions and the Hub. Monthly cross-BU "what's working" sessions. AI literacy added to HR new-hire onboarding within 90 days, so the program scales with the company.
- **Champions: 2 per BU,** selected by BU leaders from candidates I surface. Defined remit (intake, enablement, office hours, surface what's working), ~4 hrs/week. Not reporting to the Hub — the operating model is participation and influence, which is how I built the Toyota network without formal authority.
- **HR partnership.** Co-ownership: HR runs the learning platform, tracks completion, and integrates AI literacy into role expectations and onboarding; I provide curriculum, Champions, and the standards completion is measured against.

**By design:** as IC I will not try to personally train 2,700 employees. The hub-and-spoke model — Champions as spokes, HR as platform partner — is how this scales, and the operating model the role is built for.

## 7. Value realization and the eight-week board update

**My approach to ROI: establish baselines before any tool goes live.** Productivity gains are only defensible when measured against a documented pre-tool reality, not a remembered one. Most enterprise AI ROI claims fail scrutiny because they skip this — I won't. I spent the first six weeks pre-launch establishing baselines at Toyota across teams and personas, including non-engineering. Same discipline at JD Power — what makes the value story defensible to a PE owner looking for measurable creation, not narrative.

**Metrics I track:** monthly active users by BU and persona; depth (sessions, workflows per user); time-to-completion on defined workflows vs pre-rollout baselines; hours saved × loaded cost by role — the P&L number for CEO and owner; $/active user/month, $/workflow, % usage within budget.

**Metrics I will refuse to track as primaries:** *count of AI initiatives* and *AI seats deployed.* The current tracker is a useful inventory, not a north star. Initiative and seat counts are vanity metrics the PE owner will see through.

**Eight-week board update — what I'll present:**
1. State of AI at JD Power — sanctioned + shadow, with honest numbers.
2. Hub operating model and the now-codified governance framework.
3. Tool portfolio, $400K allocation, and rationale.
4. Champions network and persona-based enablement program live across all BUs; CDAO partnership and shared governance.
5. Early productivity indicators — baselines established, first measurements with explicit caveats; what I will and will not deliver by month six, and what changes with one additional headcount.

## 8. What I will not deliver in the first six months — the honest part

- **Not a full role-based AI literacy program for 2,700 employees.** I will deliver the framework, persona tracks, Champions running first cohorts, and a measurable adoption baseline.
- **Not a fully codified governance policy book.** I will deliver a 4-page operating policy, three workflow-specific guardrails for the highest-risk patterns (client deliverables, confidential client data, externally-shared AI-generated content), and a roadmap for year two.
- **Not enterprise rollouts of multiple new tool categories.** Two general-purpose platforms (productivity baseline + Claude Enterprise) and the observability layer. Specialized agent/RAG tools wait for year two, once we know where the real gaps are.
- **Not personal management of every shadow workflow.** Champions, observability, and the catalog handle the long tail. I handle the high-risk patterns directly.

I run the role as IC through month six. At that point, with adoption and baseline-to-current value data in hand, I'll bring the business case for the first additional headcount — a **Principal AI Enablement Engineer** with strong engineering depth and shipping discipline, working across the Hub's full responsibility surface (intake, governance, tool catalog, Champions, literacy, measurement) and unlocking roadmap items beyond what one IC can scale. What comes after IC gets written from evidence, not assumption.

## 9. Disclosure on AI assistance for this memo

I used chatGPT & Claude (Anthropic) to pressure-test this memo against the brief and to sharpen prose. The structure, operating model, live-situation answers, $400K allocation, and Toyota patterns are mine. Specific edits over Claude's first draft: tightened the live-situation handling (too cautious on the OEM deliverable), removed two engineering-defaulted metrics, and made the CDAO Steering Committee co-chair proposal explicit. If selected, I'd bring the same posture to internal AI-assisted work — disclosed, edited, and owned.
