import psycopg2
import os

def lambda_handler(event, context):
    # Database connection parameters
    conn = psycopg2.connect(
        dbname=os.environ['DB_NAME'], 
        user=os.environ['DB_USER'], 
        password=os.environ['DB_PASSWORD'], 
        host=os.environ['DB_HOST']
    )
    cur = conn.cursor()
    
    # Example of inserting a single data record
    sensor_id = event['sensor_id']
    value = event['value']
    measurement_type = event['measurement_type']
    timestamp = event['timestamp']
    
    cur.execute("INSERT INTO sensor_data (sensor_id, value, measurement_type, timestamp) VALUES (%s, %s, %s, %s)",
                (sensor_id, value, measurement_type, timestamp))
    
    conn.commit()
    cur.close()
    conn.close()

    return {
        'statusCode': 200,
        'body': 'Successfully inserted data into RDS'
    }
    