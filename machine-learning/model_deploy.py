# Deploy the model to an endpoint
linear_predictor = linear.deploy(initial_instance_count=1, instance_type='ml.m4.xlarge')

linear_predictor.content_type = 'text/csv'
linear_predictor.serializer = sagemaker.serializers.CSVSerializer()
linear_predictor.deserializer = sagemaker.deserializers.CSVDeserializer()

# predict with the test dataset
predictions = linear_predictor.predict(X_test.values)
print(predictions)

# NEED TO STOP AFTER. IT WILL CHARGE YOU ALOT OF MONEY.
sagemaker.Session().delete_endpoint(linear_predictor.endpoint)