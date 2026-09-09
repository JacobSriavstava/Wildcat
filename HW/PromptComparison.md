# Prompt Engineering Comparison #


## Strategy 1: Zero-Shot ##

### Prompt ###
What are the most important metrics for measuring credit risk in a consumer loan portfolio?

### First 150 words of Claudes Output ###
A well-rounded credit risk assessment for a consumer loan portfolio pulls from several categories of metrics, each answering a different question about where risk sits and how it's moving.
Borrower-level risk indicators tell you how risky the loans were at origination. Credit score is the single strongest predictor — it's a backward-looking summary of repayment history, and as you saw in Wildcat's own data, default rates fall almost monotonically with score (18.6% for sub-580 borrowers down to about 1.3% for 800+). Debt-to-income ratio measures repayment capacity relative to existing obligations and works best as a secondary filter or rate modifier rather than a standalone cutoff, since its relationship to default is real but weaker on its own. Loan-to-value (for secured products like auto or home improvement loans) measures how much cushion exists if the lender has to repossess or foreclose. Together these are the inputs a portfolio would track…..


### Evaluation ###
I thought that overall it was a pretty good response. It had a lot of good information and it pulled data from the Wildcat file. It was a little vague and general however and could have been a little more detailed. 
---

## Strategy 2: Role-Assigned ##

### Prompt ###
You are a senior credit risk analyst presenting to a portfolio committee of three senior executives with 30+ years of experience, What are the most important metrics for measuring credit risk in a consumer loan portfolio

### First 150 words of Claudes Output ###
For a portfolio committee of that caliber, the framing matters as much as the list — they've seen every backward-looking loss number before, so the presentation earns its keep by connecting lagging indicators to leading ones and tying both to what the committee can actually act on (underwriting, pricing, reserves, capital allocation).
Loss and delinquency metrics (the lagging core)
Net charge-off rate (NCOs as a % of average outstandings) is still the anchor metric — it's what flows to the P&L. Pair it with the delinquency roll rate (30→60→90+ DPD), which tells the committee whether losses are accelerating or stabilizing before they hit NCO. Vintage curve analysis — cumulative loss by origination cohort, indexed to months on book — is arguably the single most useful chart in the deck, because it isolates underwriting quality by vintage from macro noise and shows whether recent originations are performing better or worse than the cohorts that preceded….


### Evaluation ###
One thing I noticed right away was that it took Claude a lot longer to come up with this output than it did for the first output. This output was a lot more specific and comprehensive as it seems to have gone a lot deeper into the details to answer the question. It broke it down into an easy to follow format. It had a lot of different formulas and good information points. This was a more insightful output than the first prompt and was more efficient in answering the question.

---

## Strategy 3: Few-shot ##

### Prompt ###
You are a senior credit risk analyst presenting to a portfolio committee of three senior executives with 30+ years of experience, What are the most important metrics for measuring credit risk in a consumer loan portfolio. Put the output into organized categories with easy to follow bullet points.

### First 150 words of Claudes Output ###
Loss & Delinquency Metrics (Lagging Indicators)
Net charge-off (NCO) rate — losses as a % of average outstandings; the primary P&L-facing loss metric
Delinquency roll rates — movement from 30→60→90+ days past due; shows whether losses are accelerating before they hit NCO
Vintage curve analysis — cumulative loss by origination cohort, indexed to months on book; isolates underwriting quality from macro noise
Recovery rate — collections/recoveries as a % of charged-off balances
Forward-Looking / Predictive Metrics
Probability of default (PD) — likelihood of default within a defined horizon, typically by score band or segment
Loss given default (LGD) — expected loss severity once default occurs
Exposure at default (EAD) — expected outstanding balance at time of default
Expected loss (EL = PD × LGD × EAD) — the building block for both pricing and reserving
Credit score migration — movement of the book across FICO/internal score bands over time; an early drift signal
First-payment default (FPD) rate — borrowers defaulting before or…



### Evaluation ###
This was a lot easier to follow as the format was more organized. This was the most insigtful output out of all of the three. It was structured easily and was written in language that was easy to understand. 

---

## Conclusion ##

This was a very interesting exercise to do. The first output provided good information, however, as the prompt got more specific, the output became stronger and more organized. The first one was not as detailed as the second one. The third output was structured in a way that made the information easier to digest. I think the third output was the best output and the most insightful. The biggest difference was telling claude to act as a senior analyst with 30+ years of experience and also telling Claude the output format I wanted. Overall, strategy 3 produced the best output for a BI analyst. 


## Fact-Check

### The exact claim Claude made ###
"Debt-to-income ratio measures repayment capacity relative to existing obligations and works best as a secondary filter or rate modifier rather than a standalone cutoff, since its relationship to default is real but weaker on its own."

### The source you used and the URL ### 
Investopedia
URL: https://www.investopedia.com/answers?q=Debt-to-income+ratio&utm_source=investopedia&utm_medium=internal&utm_campaign=inv_answers&utm_content=site-search

### What the source says ### 
Debt-to-income ratio (DTI) measures how much of your gross monthly income goes to required debt payments.
Calculate it by dividing total monthly debt payments by gross monthly income, then multiplying by 100.
A lower DTI generally signals more capacity to repay new borrowing.
Many lenders use roughly 36% as a preferred benchmark, though allowable limits vary by loan and lender.
For mortgages, lenders may assess housing costs separately as a front-end ratio and all debts as a back-end ratio.

### Whether they agree — and if not, what you conclude about the reliability of that type of claim from Claude ###
Yes, they agree. However, the answer from Investopedia explains what it is and how it is calculated while the one from Claude describes how it should be used in credit-risk analysis. This is because that is the context that of the conversation I was having within claude was. 