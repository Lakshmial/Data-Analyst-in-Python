## 2. Joining Three Tables ##

SELECT il.track_id,t.name track_name,mt.name track_type,il.unit_price,il.quantity FROM invoice_line il
INNER JOIN track t ON t.track_id = il.track_id
INNER JOIN media_type mt ON mt.media_type_id = t.media_type_id
WHERE invoice_id=4



## 3. Joining More Than Three Tables ##

SELECT
    il.track_id,
    t.name track_name,
    ar.name artist_name,
    mt.name track_type,
    il.unit_price,
    il.quantity
FROM invoice_line il
INNER JOIN track t ON t.track_id = il.track_id
INNER JOIN album al ON al.album_id = t.album_id
INNER JOIN artist ar ON ar.artist_id = al.artist_id
INNER JOIN media_type mt ON mt.media_type_id = t.media_type_id
WHERE il.invoice_id = 4

## 4. Combining Multiple Joins with Subqueries ##

SELECT 
        ta.title album,
        ta.name artist,
        count(*) tracks_purchased
from invoice_line il
INNER JOIN(
    select al.album_id,al.title , t.track_id ,ar.name  from track t
INNER JOIN album al on al.album_id=t.album_id
INNER JOIN artist ar on ar.artist_id = al.artist_id)ta
ON ta.track_id=il.track_id

GROUP by album
ORDER by tracks_purchased DESC

limit 5








## 5. Recursive Joins ##

Select e1.first_name || " " ||e1.last_name employee_name,
       e1.title employee_title,
       e2.first_name ||" "||e2.last_name supervisor_name,
       e2.title supervisor_title
    
from employee e1
LEFT JOIN employee e2
on e1.reports_to = e2.employee_id
ORDER BY 1


## 6. Pattern Matching Using Like ##

SELECT first_name,
last_name ,
phone
from customer 
where first_name like "%Belle%"

## 7. Generating Columns With The Case Statement ##

Select c.first_name || " " ||c.last_name customer_name,
COUNT(iv.invoice_id) number_of_purchases,SUM(iv.total) total_spent,


 CASE 
     WHEN SUM(iv.total)<40 then "small spender"
     WHEN SUM(iv.total)>100 then "big spender"
     ELSE  "regular"
     END
     as customer_category
FROM customer c INNER JOIN invoice iv 
ON iv.customer_id=c.customer_id
GROUP by 1
ORDER by 1







