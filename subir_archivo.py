import boto3
import base64
import json

def lambda_handler(event, context):
    body = json.loads(event['body'])
    bucket = body['bucket']
    directorio = body['directorio']
    nombre_archivo = body['nombre_archivo']
    contenido_base64 = body['contenido_base64']

    s3 = boto3.resource('s3')
    key = f"{directorio.strip('/')}/{nombre_archivo}"

    # Subimos el archivo
    s3.Object(bucket, key).put(Body=base64.b64decode(contenido_base64))

    return {
        'statusCode': 200,
        'body': json.dumps({'mensaje': f'Archivo "{nombre_archivo}" subido a {bucket}/{directorio}'})
    }
