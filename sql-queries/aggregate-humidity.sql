SELECT 
    AVG(humidity) AS average_humidity, 
    MAX(humidity) AS max_humidity, 
    MIN(humidity) AS min_humidity 
FROM sensor_data;