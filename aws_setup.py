import os
import json
import time
from datetime import datetime
from dotenv import load_dotenv
import boto3
from botocore.exceptions import ClientError

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION', 'ap-south-1')
TRAINING_BUCKET = os.getenv('TRAINING_BUCKET_NAME', f'customer-categorizer-training-{int(time.time())}')
PREDICTION_BUCKET = os.getenv('PREDICTION_BUCKET_NAME', f'customer-categorizer-prediction-{int(time.time())}')

OUTPUT_FILE = 'infra_output.json'

result = {
    'timestamp': datetime.utcnow().isoformat(),
    'caller_identity': None,
    'training_bucket': TRAINING_BUCKET,
    'prediction_bucket': PREDICTION_BUCKET,
    'iam_user': None,
    'iam_access_key': None,
    'errors': []
}

if not AWS_ACCESS_KEY_ID or not AWS_SECRET_ACCESS_KEY:
    print('AWS credentials not found in environment. Please set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY in .env')
    result['errors'].append('Missing AWS credentials')
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(result, f, indent=2)
    raise SystemExit(1)

# Create session
session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

sts = session.client('sts')
try:
    identity = sts.get_caller_identity()
    result['caller_identity'] = identity
    print('AWS Caller Identity:', identity)
except Exception as e:
    print('Failed to get caller identity:', e)
    result['errors'].append(str(e))
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(result, f, indent=2)
    raise SystemExit(1)

s3 = session.client('s3')
iam = session.client('iam')

# Create buckets
for bucket in [TRAINING_BUCKET, PREDICTION_BUCKET]:
    try:
        # Determine if bucket exists
        s3.head_bucket(Bucket=bucket)
        print(f'Bucket {bucket} already exists and is accessible')
    except ClientError as e:
        code = int(e.response['Error']['Code']) if e.response.get('Error', {}).get('Code', '').isdigit() else None
        # Try to create
        try:
            if AWS_REGION == 'us-east-1':
                s3.create_bucket(Bucket=bucket)
            else:
                s3.create_bucket(Bucket=bucket, CreateBucketConfiguration={'LocationConstraint': AWS_REGION})
            print(f'Created bucket: {bucket}')
        except ClientError as e2:
            msg = f'Failed to create bucket {bucket}: {e2}'
            print(msg)
            result['errors'].append(msg)

# Create IAM user
iam_user_name = f'customer-categorizer-user-{int(time.time())}'
try:
    iam.create_user(UserName=iam_user_name)
    print('Created IAM user:', iam_user_name)
except ClientError as e:
    if e.response['Error']['Code'] == 'EntityAlreadyExists':
        print('IAM user already exists, using existing user:', iam_user_name)
    else:
        msg = f'Failed to create IAM user: {e}'
        print(msg)
        result['errors'].append(msg)

# Attach AmazonS3FullAccess managed policy
policy_arn = 'arn:aws:iam::aws:policy/AmazonS3FullAccess'
try:
    iam.attach_user_policy(UserName=iam_user_name, PolicyArn=policy_arn)
    print('Attached policy AmazonS3FullAccess to', iam_user_name)
except ClientError as e:
    msg = f'Failed to attach policy: {e}'
    print(msg)
    result['errors'].append(msg)

# Create access key for IAM user
try:
    ak = iam.create_access_key(UserName=iam_user_name)
    access_key = ak['AccessKey']['AccessKeyId']
    secret_key = ak['AccessKey']['SecretAccessKey']
    print('Created access key for user:', iam_user_name)
    result['iam_user'] = iam_user_name
    result['iam_access_key'] = {'AccessKeyId': access_key, 'SecretAccessKey': secret_key}
except ClientError as e:
    msg = f'Failed to create access key: {e}'
    print(msg)
    result['errors'].append(msg)

# Save infra output
with open(OUTPUT_FILE, 'w') as f:
    json.dump(result, f, indent=2)

print('\n=== INFRA OUTPUT SAVED TO', OUTPUT_FILE, '===')
print(json.dumps(result, indent=2))

print('\nNext steps:')
print('- If access keys were created, add them to your local .env as AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY')
print('- Update TRAINING_BUCKET_NAME and PREDICTION_BUCKET_NAME if you want different names')
print('- Restart the application')
