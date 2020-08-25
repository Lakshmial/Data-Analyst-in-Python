## 2. Communication is a Two-way Street ##

# ans = "A"
# ans = "B"
ans = "C"

## 3. Dealing with Fuzzy Language ##

 ans = "A"
# ans = "B"
# ans = "C"

## 4. Churned Customers ##

import pandas as pd
import datetime as dt

data = pd.read_csv("rfm_xmas19.txt", parse_dates=["trans_date"])
group_by_customer = data.groupby("customer_id")
last_transaction = group_by_customer["trans_date"].max()

#pd.DataFrame() to have the data in last_transaction as a dataframe. Assign it to best_churn.
best_churn=pd.DataFrame(last_transaction)

#Create a datetime object representing October 16, 2019. Assign it to cutoff_day.
cutoff_day=dt.datetime(2019,10,16)

#Use best_churn["trans_date"].apply() with an appropriate function to code the rationale in the instruction.

best_churn["churned"]=best_churn["trans_date"].apply(lambda date:1 if date <cutoff_day else 0)


## 5. Aggregate Data by Customer ##

best_churn["nr_of_transactions"] = group_by_customer.size()
best_churn["amount_spent"] = group_by_customer.sum()
best_churn.drop("trans_date",axis = "columns",inplace=True)

## 6. Ranking Customers ##


#Create a column named scaled_tran (in the best_churn dataframe) that scales nr_of_transactions.

best_churn["scaled_tran"]=(best_churn["nr_of_transactions"] -best_churn["nr_of_transactions"].min()) /(best_churn["nr_of_transactions"].max()- best_churn["nr_of_transactions"].min())

#Create a column named scaled_amount in the best_churn dataframe that scales amount_spent

best_churn["scaled_amount"]=(best_churn["amount_spent"] -best_churn["amount_spent"].min()) /(best_churn["amount_spent"].max()- best_churn["amount_spent"].min())

#Create a column called score using the formula at the beginning of this screen. Make sure you use the scaled columns created in the previous instruction.Multiply score by 100 to make it more readable. Assign back to the score column in best_churn.


best_churn["score"]=((best_churn["scaled_tran"]/2)+(best_churn["scaled_amount"]/2))*100

#Use the method pandas.DataFrame.sort_values() to sort best_churn by score.Either use the inplace argument or assign back to best_churn.Sort it in descending order.
best_churn.sort_values("score",inplace=True,ascending=False)









## 7. Determining a Threshold ##

coupon=data["tran_amount"].mean()*.30
nr_of_customers= 1000/coupon


## 8. Delivering the Results ##

churned_customers=best_churn[best_churn["churned"]==1]
top_50_churned=churned_customers[0:50]
top_50_churned.to_csv("best_customers.txt")