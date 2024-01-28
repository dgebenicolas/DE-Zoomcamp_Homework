SELECT 
 TO_CHAR(lpep_pickup_datetime, 'YYYY-MM') AS year_month,
 zpu."Zone",
 zdo."Zone",
 MAX(tip_amount)
 
FROM 
 green_taxi_trips t
JOIN
	zones zpu ON t."PULocationID" = zpu."LocationID"
JOIN 
    zones zdo ON t."DOLocationID" = zdo."LocationID"
WHERE zpu."Zone" = 'Astoria' AND TO_CHAR(lpep_pickup_datetime, 'YYYY-MM') = '2019-09'
GROUP BY year_month, zpu."Zone", zdo."Zone"
ORDER BY MAX(tip_amount) DESC;
