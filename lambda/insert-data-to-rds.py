import psycopg2
import os
import json

def lambda_handler(event, context):
    
    records = json.loads(event['body'])['records']
    
    conn = psycopg2.connect(dbname=os.environ['DB_NAME'], user=os.environ['DB_USER'], password=os.environ['DB_PASSWORD'], host=os.environ['DB_HOST'])
    cur = conn.cursor()
    
    insert_query = """
    INSERT INTO sensor_data (time, R1, R2, R3, R4, R5, R6, R7, R8, temperature, humidity)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    for record in records:
        
        data = (record['time'], record['R1'], record['R2'], record['R3'], record['R4'], record['R5'], record['R6'], record['R7'], record['R8'], record['Temp.'], record['Humidity'])
        cur.execute(insert_query, data)
    
    conn.commit()
    cur.close()
    conn.close()

    return {
        'statusCode': 200,
        'body': 'Successfully inserted data into RDS'
    }