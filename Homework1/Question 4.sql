SELECT 
 CAST(lpep_pickup_datetime AS DATE) as "day",
 MAX(trip_distance)
FROM green_taxi_trips
GROUP BY "day"
ORDER BY MAX(trip_distance) DESC;
