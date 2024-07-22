# budgy (Personal Budget Dashboard) 
# Contents:
-  [Executive Summary](#executive-summary)
-  [Pre-analysis questions ](#pre-analysis-questions)
-  [Visual output ](#visual-output)
-  [Findings ](#findings)
-  [Summary and Recommendations](#summary-and-recommendations)


## *Executive Summary*
Personal project used to consolidate all bank statements creating an ETL framework ending in a published Tableau dashboard. Reason for creation of this is to have an interactive way to manage spending from different accounts and highlight specific spending patterns that I have in order to minimise my spend and maximise saving potentials.  


#### Tools and techniques used: Python, SQL, Tableau, Pandas, REST API, Data Warehousing, Data Manipulation, Data Visualisation

## Pre-analysis questions 
Initial thoughts when conducting this is to both answer certain questions and confirm initial budgeting hypothesis that I had: 
1. [I am spending more than I am earning](#i-am-spending-more-than-i-am-earning)
2. [Biggest expenditure is my partner (main category over-budget)](#biggest-expenditure-is-my-partner)
3. [How consistent are my additional income streams?](#how-consistent-are-my-additional-income-streams)


## Visual output
An intiial flow was created below to map out the different stages of the ETL process


![image](https://github.com/saifaw165/budgy/assets/69206545/1deb6c53-271f-4d0b-880c-d602e8537895)

From the initial flow an interactive dashboard can be seen via this [link](https://public.tableau.com/app/profile/saif.widyatmoko/viz/PersonalBudgetingDashboard/Dashboard) (a screenshot of dashboard can be seen below)
![image](https://github.com/saifaw165/budgy/assets/69206545/7df3263d-84f5-4119-a3dd-8fd822f3e5e7)

## Findings 

### *I am spending more than I am earning*
We can see that on average I am spending more than I am earning. 

<img width="1078" alt="image" src="https://github.com/user-attachments/assets/6f331233-4617-48f0-9da9-c381945b092e">

Looking at the months where I spent less than what I earn, the root cause of this was a reduction in `other` expenditure

![image](https://github.com/user-attachments/assets/b7fb7c67-3702-4cf0-aa8f-7fd447674fd4)

Also the largest month of income both from tutoring alongside salary bonus. 

![image](https://github.com/user-attachments/assets/224fea5c-0fd2-4eb1-ac94-32dca78562d6)

We can see that the majority of the time, I am spending more than I am earning. What is next is to see what exactly is the largest driver and is this in line against the budgets that have been made for them. 

### *Biggest expenditure is my partner*

Initial hypothesis was my partner was my main expense which is why I mapped a max budget of £600 against her. Looking at my mapped categories over time, I can see that my partner `Girlfriend_tax` is significantly under the amount. 
<img width="1095" alt="image" src="https://github.com/user-attachments/assets/8958fcc9-e9df-4f25-acc6-3e3cdcb83d96">

The main category that has been significantly sporadic are my `groceries` month over month alongside `transport`. A re-evaluation of my budgets should be considered to keep me consistent against my budget. 

### *How consistent are my additional income streams?*

From the time series chart we can see that there was a downward trend in the additional income (tutoring) from February. Tutoring also only accounts for at highest <3% of income so recommendations would be to increase tutoring amount to acount for 5% of my income.  
<img width="800" alt="image" src="https://github.com/user-attachments/assets/19f2784a-30fc-4676-84e8-838c60332ff7">


## Summary and Recommendations

### *Summary*

1. Looking at spend over time, we can see that `other` is the main driver of spend
   - Looking into the description of what this entails the majority of this is food and luxury miscalaneaous expenditure
2. Seeing the trend chart of account balance, we can see the positive months are when I increase my amount of additional income streams
3. I have overestimated the amount of budget for my partner and underestimated the amount for groceries and trasnport

This calls for a re-evaluation and recommendation for spending behaviour

### *Recommendations*
In order to improve spending behaviour a number of factors need to be done to chnage:
- Reduce expenditure on luxury goods to have a postitive account balance
- Increase the amount of additional income streams. This will allow to spend more and remain still at a positive balance
- Re-map muy budget reducing the amount for budget
  - Reduce `girlfriend_tax` to 350
  - Increase `groceries` to 150
  - Increase `transport` to 200




