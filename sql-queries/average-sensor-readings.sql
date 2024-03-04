SELECT AVG(R1) as avg_R1, AVG(R2) as avg_R2, AVG(temperature) as avg_temp, AVG(humidity) as avg_humidity
FROM sensor_data
WHERE time BETWEEN '2024-01-01' AND '2024-01-31';