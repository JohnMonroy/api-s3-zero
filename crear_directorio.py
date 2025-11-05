import boto3
import json

def lambda_handler(event, context):
    body = json.loads(event['body'])
    bucket = body['bucket']
    directorio = body['directorio']

    s3 = boto3.client('s3')
    key = f"{directorio.strip('/')}/"  # aseguramos que termine en /
    s3.put_object(Bucket=bucket, Key=key)

    return {
        'statusCode': 200,
        'body': json.dumps({'mensaje': f'Directorio "{directorio}" creado en el bucket "{bucket}"'})
    }
