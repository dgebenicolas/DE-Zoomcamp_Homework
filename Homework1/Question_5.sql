SELECT 
 CAST(lpep_pickup_datetime AS DATE) as "day",
 SUM(total_amount),
 "Borough"
FROM 
 green_taxi_trips t
JOIN
	zones zpu ON t."PULocationID" = zpu."LocationID"
WHERE CAST(lpep_pickup_datetime AS DATE) = '2019-09-18'
GROUP BY "day", "Borough"
HAVING SUM(total_amount) > 50000;	
