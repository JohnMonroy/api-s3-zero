import boto3
import json

def lambda_handler(event, context):
    # Entrada
    body = json.loads(event['body'])
    nombre_bucket = body['bucket']

    # Proceso
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=nombre_bucket)

    # Salida
    return {
        'statusCode': 200,
        'body': json.dumps({'mensaje': f'Bucket {nombre_bucket} creado correctamente'})
    }
