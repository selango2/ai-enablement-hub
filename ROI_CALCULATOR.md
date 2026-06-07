# Perficient AI Adoption Operating Model
## ROI Calculator (Excel/Google Sheets Template)

---

## HOW TO USE THIS CALCULATOR

1. **Copy the data table below into Excel or Google Sheets**
2. **Enter your customer's information in the BLUE cells (Inputs section)**
3. **The calculator automatically computes savings and ROI (green cells will populate)**
4. **Share the results with the customer as part of your proposal**

---

## CALCULATOR TEMPLATE

### SECTION 1: COMPANY PROFILE (Blue = Customer Input)

| Item | Value | Notes |
|------|-------|-------|
| **Company Name** | *[Enter]* | *Customer organization* |
| **Number of Employees** | *[Enter]* | *Total headcount* |
| **Knowledge Workers (%)** | 40% | *% of workforce using AI tools* |
| **Knowledge Workers (Count)** | =B3*B4 | *Calculated* |
| **Annual Revenue** | *[Enter]* | *For context* |

---

### SECTION 2: CURRENT STATE - SHADOW AI USAGE (Blue = Customer Input)

| Item | Value | Formula/Notes |
|------|-------|-------|
| **% of Team Using Unsanctioned AI** | 65% | *Enter based on assessment or industry benchmark* |
| **Number Using Shadow AI** | =B5*B7 | *Calculated* |
| **Avg Hours/Week Lost to Tool Selection** | 2.5 | *Time spent finding/evaluating tools* |
| **Avg Hourly Cost per Employee** | $75 | *Salary burden (salary/2080 hrs)* |
| **Weekly Cost per Person (Tool Selection)** | =B9*B10 | =$187.50 |
| **Annual Cost per Person** | =B11*50 | =$9,375 |
| **Total Annual Cost (Tool Selection)** | =B6*B13 | *Calculated* |

| Item | Value | Formula/Notes |
|------|-------|-------|
| **Estimated Annual Shadow AI Spend (Untracked)** | *[Enter]* | *ChatGPT/Claude/Gemini subscriptions not tracked* |
| **Estimated Data Exposure Risk** | *[Enter or use 0]* | *Cost of potential breach/compliance issue* |
| **Estimated Duplicate Tool Spend** | *[Enter or use 0]* | *Multiple teams buying same tool* |

| Item | Value | Notes |
|------|-------|-------|
| **TOTAL CURRENT SHADOW AI COST** | =[B15+B16+B17] | *Annual cost of shadow AI state* |

---

### SECTION 3: PERFICIENT IMPLEMENTATION COSTS (Blue = Customer Input)

| Item | Cost | Notes |
|------|------|-------|
| **Perficient Service Engagement** | $300,000 | *90-day implementation (or customize if different package)* |
| **Tools & Systems Setup** | $25,000 | *Budget tracking, dashboard, training platform* |
| **Customer Internal Cost (1 FTE × 90 days)** | *[Enter or calculate]* | *Internal project manager time* |
| **TOTAL IMPLEMENTATION COST (Year 1)** | =[B20+B21+B22] | *Calculated* |

---

### SECTION 4: POST-IMPLEMENTATION BENEFITS (Blue = Customer Input)

**Benefit 1: Reduce Shadow AI Spend**

| Item | Value | Formula/Notes |
|------|-------|-------|
| **Reduction in Shadow AI Usage** | 70% | *Conservative: 70% move to sanctioned* |
| **Shadow AI Cost Reduction** | =B19*B25 | *Annual savings from eliminating untracked spend* |

**Benefit 2: Reduce Governance Overhead**

| Item | Value | Formula/Notes |
|------|-------|-------|
| **Current Annual Governance Cost** | *[Enter]* | *Hours spent chasing/approving tools* |
| **% Reduction with Operating Model** | 50% | *Hub-and-spoke reduces manual governance* |
| **Governance Cost Reduction** | =B29*B30 | *Annual savings* |

**Benefit 3: Improve Adoption Efficiency (Productivity)**

| Item | Value | Formula/Notes |
|------|-------|-------|
| **Productivity Gain per User** | 2 hrs/week | *Users spending less time finding tools, more using them* |
| **# of Users Affected** | =B5 | *Knowledge workers* |
| **Hours Saved Annually** | =B34*B35*50 | *Calculated (2 hrs × employees × 50 weeks)* |
| **Cost per Hour** | $75 | *Hourly burden* |
| **Annual Productivity Gain** | =B36*B37 | *Calculated* |

**Benefit 4: Reduce Compliance Risk**

| Item | Value | Formula/Notes |
|------|-------|-------|
| **Estimated Risk Mitigation Value** | *[Enter or use 0]* | *Avoided breach, audit, regulatory cost* |

**Benefit 5: Training & Adoption Stickiness**

| Item | Value | Formula/Notes |
|------|-------|-------|
| **Adoption Rate Improvement** | 60% → 85% | *Tools deployed but not used → actively used* |
| **Additional Users Engaged** | =(B5*0.85)-(B5*0.60) | *Calculated* |
| **Value per Additional User** | $5,000 | *Productivity gain from improved adoption* |
| **Adoption Improvement Value** | =B44*B45 | *Calculated* |

---

### SECTION 5: YEAR 1 SUMMARY

| Item | Amount |
|------|--------|
| **Total Benefits (Year 1)** | =SUM(B26,B31,B38,B41,B46) |
| **Total Costs (Year 1)** | B23 |
| **NET BENEFIT (Year 1)** | =B49-B50 |
| **ROI (%)** | =(B51/B50)*100 |
| **Payback Period (Months)** | =12*(B50/B49) |

---

### SECTION 6: 3-YEAR PROJECTION

| Year | Costs | Benefits | Net Benefit | Cumulative |
|------|-------|----------|-------------|------------|
| **Year 1** | $325K | [From B49] | [From B51] | [From B51] |
| **Year 2** | $50K* | [B49 × 1.0] | =[B53-B52] | =C51+C54 |
| **Year 3** | $50K* | [B49 × 1.1] | =[B53-B52] | =D54+C55 |

*Year 2-3 assumes recurring governance services only (no implementation cost)

| Metric | Value |
|--------|-------|
| **3-Year Total ROI** | =[(D55)/(B23+(B52*2))]*100 |
| **3-Year Cumulative Benefit** | D55 |

---

## SCENARIO EXAMPLES

### Example 1: Mid-Market Company (500 employees, 40% knowledge workers)

```
Company Profile:
- Total employees: 500
- Knowledge workers: 200
- Annual revenue: $200M
- Shadow AI usage: 65%

Current State:
- Shadow AI cost: $1,950,000
  (200 workers × 65% × $9,375 from tool selection
   + $800K untracked ChatGPT spend)

Implementation Cost: $325,000

Benefits (Year 1):
- Shadow AI reduction (70%): $1,365,000
- Governance overhead (50%): $150,000
- Productivity gain: $600,000
- Risk mitigation: $200,000
TOTAL: $2,315,000

Year 1 ROI: ($2,315,000 - $325,000) / $325,000 = 612%
Payback: 2 months
```

### Example 2: Enterprise (2,000 employees, 50% knowledge workers)

```
Company Profile:
- Total employees: 2,000
- Knowledge workers: 1,000
- Annual revenue: $1B+
- Shadow AI usage: 70%

Current State:
- Shadow AI cost: $9,750,000
  (1,000 workers × 70% × $9,375
   + $2.5M untracked enterprise spend
   + $500K risk exposure)

Implementation Cost: $350,000

Benefits (Year 1):
- Shadow AI reduction (70%): $6,825,000
- Governance overhead (50%): $600,000
- Productivity gain: $3,000,000
- Risk mitigation: $500,000
- Adoption improvement: $750,000
TOTAL: $11,675,000

Year 1 ROI: ($11,675,000 - $350,000) / $350,000 = 3,236%
Payback: 11 days
```

### Example 3: Small Enterprise (300 employees, 35% knowledge workers)

```
Company Profile:
- Total employees: 300
- Knowledge workers: 105
- Annual revenue: $150M
- Shadow AI usage: 55%

Current State:
- Shadow AI cost: $542,000
  (105 workers × 55% × $9,375
   + $150K untracked spend)

Implementation Cost: $300,000

Benefits (Year 1):
- Shadow AI reduction (70%): $379,400
- Governance overhead (50%): $60,000
- Productivity gain: $315,000
- Adoption improvement: $175,000
TOTAL: $929,400

Year 1 ROI: ($929,400 - $300,000) / $300,000 = 210%
Payback: 3.9 months
```

---

## HOW TO CUSTOMIZE THIS FOR YOUR CUSTOMER

### Step 1: Gather Information
Ask the customer:
- "How many people in your organization?"
- "What % use AI tools?"
- "How much shadow AI spend do you estimate?"
- "How much time do you spend on tool approvals?"
- "What's the biggest pain point?"

### Step 2: Build the Case
- Use actual numbers where you have them
- Use industry benchmarks for estimates
- Be conservative on savings (clients will verify)

### Step 3: Present the Model
- Start with their current state ("You're spending $X on shadow AI")
- Show the path forward ("Our framework reduces that by 70%")
- Show the ROI ("That's $X in Year 1 benefits for $X investment")
- Show the payback ("You pay for this in Y months")

### Step 4: Handle Objections
- "These numbers seem high" → "We're actually being conservative. Many customers find shadow AI costs are higher than estimated"
- "Can we reduce the service cost?" → "Yes, we can discuss a phased approach or do a smaller pilot first"
- "What if we don't achieve these savings?" → "We measure everything. If we don't hit targets, we adjust the program"

---

## TIPS FOR SALES

**Keep it simple:**
- You don't need to show all the calculations in the proposal
- Just show: Current Cost → Implementation Cost → Year 1 Benefits → ROI
- Offer to "run the numbers" specifically for them if they ask

**Focus on their biggest pain:**
- For a CIO worried about compliance → Emphasize risk reduction
- For a CFO worried about costs → Emphasize shadow AI spend
- For a VP of Digital → Emphasize adoption efficiency

**Use their own numbers when possible:**
- "You mentioned you're managing 15 different AI tools"
- "That suggests you're probably spending $500K-1M in untracked spend"
- "Let me show you what happens if we consolidate and govern that"

**Always close with ROI:**
- "In your case, this would save you $1.5M in Year 1"
- "That pays for the service in less than 3 months"
- "Then you have $1.2M in net benefit, plus all the governance benefits"

---

## EXCEL/SHEETS SETUP

### To Import This Into Excel or Google Sheets:

1. Copy the markdown table above
2. Paste into Google Sheets (or Excel)
3. Format blue cells as user input (light blue background)
4. Format green cells as calculated (light green background)
5. Add formulas to calculated cells
6. Test with example numbers

### Formulas to Use:

```
B5 (Knowledge Workers Count) = B3*B4
B8 (Number Using Shadow AI) = B5*B7
B11 (Weekly Cost per Person) = B9*B10
B13 (Annual Cost per Person) = B11*50
B15 (Total Cost Tool Selection) = B6*B13

[Continue for other calculated cells...]
```

---

## SALES CONVERSATION FLOW WITH THIS CALCULATOR

**During Discovery Call:**
1. "Can you help me understand your current AI tool usage?"
2. *Listen and take notes on: # employees, shadow AI %, current costs*
3. "I'd like to model what this would look like for you"

**Post-Call:**
1. Fill in the calculator with their numbers
2. Run a few scenarios (current state, optimistic, conservative)
3. Email back: "I ran the numbers for your organization..."
4. Include 1-2 page summary showing their ROI
5. Offer to walk through it on next call

**On Next Call:**
1. "Here's what I found..."
2. Show current shadow AI cost (usually surprises them)
3. Show implementation cost
4. Show Year 1 benefits
5. "The payback is [X months], and Year 1 benefit is [$ amount]"
6. Ask: "Does this make sense? Should we move to a scoping workshop?"

---

## DISCLAIMER / NOTES

Add this to any proposal using these numbers:

> "The financial projections in this ROI analysis are based on industry benchmarks and customer data. Actual results will vary based on the specific customer context, implementation quality, and organizational adoption. Perficient recommends establishing baseline measurements before implementation and tracking actual outcomes throughout the engagement. These figures are estimates and should be refined with customer-specific data during the scoping phase."

---

## FILE EXPORT OPTIONS

- **Excel (.xlsx):** Copy table into Excel, add formulas
- **Google Sheets:** Copy table into Google Sheets (it auto-formats)
- **PDF:** Export from Excel/Sheets for formal proposal
- **CSV:** Export table as CSV for further processing

All are customizable for your specific customer scenarios.
