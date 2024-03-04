CREATE TABLE sensor_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sensor_id VARCHAR(255),
    value DECIMAL(10, 2),
    measurement_type VARCHAR(50),
    timestamp TIMESTAMP
);