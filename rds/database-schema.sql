CREATE TABLE sensor_data (
    id SERIAL PRIMARY KEY,
    time TIMESTAMP,
    R1 DECIMAL(10, 2),
    R2 DECIMAL(10, 2),
    R3 DECIMAL(10, 2),
    R4 DECIMAL(10, 2),
    R5 DECIMAL(10, 2),
    R6 DECIMAL(10, 2),
    R7 DECIMAL(10, 2),
    R8 DECIMAL(10, 2),
    temperature DECIMAL(5, 2),
    humidity DECIMAL(5, 2)
);