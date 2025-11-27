import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Extract bucket & file from event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    
    print(f"Triggered for: {bucket_name}/{file_name}")

    # Read file
    obj = s3.get_object(Bucket=bucket_name, Key=file_name)
    data = obj['Body'].read().decode('utf-8')

    print("File Content:")
    print(data)

    return "OK"

