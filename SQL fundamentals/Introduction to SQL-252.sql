## 6. The LIMIT Clause ##

SELECT * FROM recent_grads LIMIT 10

## 8. Filtering Rows Using WHERE ##

SELECT Major ,ShareWomen FROM recent_grads
WHERE ShareWomen < 0.5

## 9. Expressing Multiple Filter Criteria Using AND ##

SELECT Major,Major_category,Median,ShareWomen FROM recent_grads
WHERE ShareWomen > 0.5 AND Median >50000


## 10. Returning One of Several Conditions With OR ##

SELECT Major,Median,Unemployed from recent_grads
WHERE Median>=10000 or Unemployed <=1000
Limit 20

## 11. Grouping Operators With Parentheses ##

SELECT Major,Major_category,ShareWomen,Unemployment_rate
from recent_grads
WHERE (Major_category = 'Engineering') AND
(ShareWomen > 0.5 or Unemployment_rate < 0.051 )

## 12. Ordering Results Using ORDER BY ##

SELECT Major ,ShareWomen,Unemployment_rate
FROM recent_grads
WHERE ShareWomen > 0.3 and Unemployment_rate < 0.1
ORDER BY ShareWomen DESC

## 13. Practice Writing a Query ##

SELECT Major_category, Major ,Unemployment_rate
from recent_grads
where Major_category='Engineering'or Major_category='Physical Sciences'
ORDER BY Unemployment_rate