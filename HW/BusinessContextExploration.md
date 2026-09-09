# Business Context Exploration #
---

## Question 1

# Prompt
How could someone at Wildcat Capital use credit score, debt-to-income ratio, and annual income data to assess a consumer's credit risk when deciding to approve or deny a loan?

# Summary of Response
Borrowers with a credit score under 620 and DTI over 43% default at 10.1%, versus 1.4% default for borrowers with a score of 720+ and DTI under 36%. Credit score summarizes someone's actual repayment history into a single number. Wildcat creates a set of hard cutoffs as it assigns interest rates. Debt-to-income ratio is the forward looking signal as it measures how much of the borrowers income is committed to debt payment. This tells you how much room they have to absorb new loan payments. Annual income on its own is a weaker risk signal. Wildcat can build a simple risk-tiering model using credit score as a primary gate, DTI as a secondary constraint, and income to size the maximum loan or payment amount. 

# Follow up Question
Are there specific metrics that would cause Wildcat to completely deny someone a loan instead of just charging them high rates? If so, what are those conditions?
---

## Question 2

# Prompt
What key metrics and trends would a portfolio committee want to see in a quarterly review to evaluate the performance and credit risk of Wildcats Auto, Personal, Home Improvement, Education, and Business Loan portfolios?

# Summary of Response
The committee will first want to see the size and the mix of the portfolio. In Wildcat's data, there is an uneven mix as home improvement is the largest by count followed by Auto next. Business carries the smallest count but the largest average ticket size. The committee would want originations by quarter and by product to identify which lines are growing, shrinking, or becoming concentrated. The credit quality of new originations is important. The committee will want to see average credit scores, DTI, and income for the borrowers approved that quarter and how that compares to previous quarters. The committee will also want to know delinquency and default rates by product and in aggregate. They will also want to see vintage and seasoning trends, loss severity and profitability, and concentration and segment risk. 

# Follow up Question
If the average credit score, DTI, and income for the borrowers approved in that quarter is lower than prior quarters, what does this tell the committee and what adjustments would the committee want to make? If they are higher than prior quarters what does that suggest?

---

## Question 3

# Prompt
When looking at Wildcat's four loan status categories, how should the committee distinguish between delinquent and default loans, what does the distribution of these statuses tell us about the credit risk of the portfolio?

# Summary of Response
Delinquent means the borrower has missed one or more scheduled payments but the loan hasn't been written off. Default means the loan has deteriorated past the point Wildcat expects to collect on the original terms. Of 2,340 loans, 62.1% are Current and 22.7% have Paid Off. So 84.8% of the book has performed as expected. This leaves 10.6% Delinquent and 4.5% in Default ($14.3 M and $7.0M respectively). A committee would read this as largely healthy but carrying a non-trivial early-stage risk pool. 

# Follow up Question
What is something Wildcat could do in their screening stage to reduce the amount of Delinquent and Default percentages? What would the roll-rate-delinquent-to-default conversion metric tell the committee? How would it be interpreted?

---

## Question 4
# Prompt
If two Wildcat clients have similar credit scores but different debt-to-income ratios and annual income levels, how should Wildcats assessment of their credit risks differ?

# Summary of Response
The credit scores being similar tells Wildcat that they have a similar repayment history. DTI measures how much of income is already committed to debt payment, so it tells Wildcat how much shock a client can absorb. For a high DTI client, a new loan payment stacked on top of existing obligations is a bigger relative burden compared to a new loan payment for a low DTI client. 

# Follow up Question
How does the size of the loan impact how Wildcat evaluates the client in this situation? 
---

## Question 5
# Prompt
Which loan types should Wildcats portfolio committee pay the most attention to during a quarterly review, and why?

# Summary of Response
The loan type Wildcat should pay the most attention to is the products that are getting worse, not just the ones that already look risky. In this case, that is the Business Loans. Their default rate jumped from 1% to 7.3% (2015-2021 vs 2022-2025). Home improvement is their largest chronic weak spot as it is not accelerating as fast. It is the worst performer overall with the highest default rate and the highest delinquency rate. It is also important to note home improvement has the largest loan count. 
# Follow up Question
Would it make sense for Wildcat to charge higher rates for the loan types that are more risky for them? Is that fair to the client?
