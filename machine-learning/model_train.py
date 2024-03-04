from sagemaker.amazon.amazon_estimator import get_image_uri

# Will use Linear Learner container image
container = get_image_uri(sagemaker_session.boto_region_name, 'linear-learner')

linear = sagemaker.estimator.Estimator(container,
                                       role, 
                                       train_instance_count=1, 
                                       train_instance_type='ml.c4.xlarge',
                                       output_path=f's3://{bucket_name}/sagemaker/output',
                                       sagemaker_session=sagemaker_session)

linear.set_hyperparameters(feature_dim=X_train.shape[1],
                           predictor_type='regressor',
                           mini_batch_size=100)

s3_input_train = sagemaker.s3_input(s3_data=s3_train_data, content_type='text/csv')

# Train the model
linear.fit({'train': s3_input_train})

