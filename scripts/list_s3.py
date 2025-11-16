from dotenv import load_dotenv
import os
import boto3


def main():
    load_dotenv()
    bucket = os.getenv('TRAINING_BUCKET_NAME')
    region = os.getenv('AWS_REGION')
    if bucket is None:
        print('TRAINING_BUCKET_NAME not set in environment or .env')
        return
    try:
        s3 = boto3.client('s3', region_name=region)
        resp = s3.list_objects_v2(Bucket=bucket)
        objs = resp.get('Contents', [])
        if not objs:
            print('NO_OBJECTS')
        else:
            for o in objs:
                print(o['Key'])
    except Exception as e:
        print('ERROR', e)


if __name__ == '__main__':
    main()
