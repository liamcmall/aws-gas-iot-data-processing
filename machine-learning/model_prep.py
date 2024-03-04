import pandas as pd
import numpy as np
import os
import sagemaker
from sagemaker import get_execution_role
from sagemaker.amazon.amazon_estimator import get_image_uri
from sagemaker.session import s3_input, Session

# SageMaker Prep

sagemaker_session = sagemaker.Session()
role = get_execution_role()

bucket_name = 'liam-iot-gas-sensor-data'
file_key = 'HT_sensor_data.csv'

data_location = f's3://{bucket_name}/{file_key}'
df = pd.read_csv(data_location)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df[['Temp.', 'Humidity']] = scaler.fit_transform(df[['Temp.', 'Humidity']])


# Train

from sklearn.model_selection import train_test_split

# Assume 'R1' is the target variable
X = df.drop(['R1'], axis=1)
y = df['R1']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Uploading Training Data to S3

import io
import sagemaker.amazon.common as smac

buf = io.BytesIO()
smac.write_numpy_to_dense_tensor(buf, X_train.values, y_train.values)
buf.seek(0)

key = 'linear-train-data'
prefix = 'sagemaker/input'
boto3.resource('s3').Bucket(bucket_name).Object(os.path.join(prefix, key)).upload_fileobj(buf)
s3_train_data = f's3://{bucket_name}/{prefix}/{key}'
print('uploaded training data location: {}'.format(s3_train_data)