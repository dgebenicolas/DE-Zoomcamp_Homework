SELECT 
 CAST(lpep_pickup_datetime AS DATE) as "day",
 COUNT(1)
FROM green_taxi_trips
WHERE CAST(lpep_pickup_datetime AS DATE) = '2019-09-18'
GROUP BY CAST(lpep_pickup_datetime AS DATE)
