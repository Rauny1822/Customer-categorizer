# Customer Categorizer - Complete Setup & Deployment Guide

## Table of Contents
1. [Development Setup](#development-setup)
2. [Environment Variables](#environment-variables)
3. [Database Setup](#database-setup)
4. [AWS Configuration](#aws-configuration)
5. [Running the Application](#running-the-application)
6. [Troubleshooting](#troubleshooting)

---

## Development Setup

### System Requirements
- **Python**: 3.8 or higher
- **Git**: For version control
- **pip**: Python package manager
- **Virtual Environment**: Recommended (venv or conda)

### Step 1: Clone Repository

```bash
git clone https://github.com/Rauny1822/Customer-categorizer.git
cd Customer-categorizer
```

### Step 2: Create Virtual Environment

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Create Environment File

```bash
# Copy the example file
cp .env.example .env

# Edit .env with your configuration
# (Instructions in the next section)
```

---

## Environment Variables

### Overview

The application uses environment variables for sensitive configuration. Create a `.env` file in the project root directory.

### Required Variables

#### 1. MongoDB Configuration

```env
MONGO_DB_URL=mongodb+srv://username:password@cluster.mongodb.net/database_name
```

**How to get MongoDB credentials:**

**Option A: MongoDB Atlas (Cloud)**

1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Create a free account
3. Create a new cluster
4. Click "CONNECT" on your cluster
5. Choose "Connect your application"
6. Copy the connection string
7. Replace `username`, `password`, and `database_name`

Example:
```
MONGO_DB_URL=mongodb+srv://admin:MyPassword123@cluster0.abcd123.mongodb.net/customer_db
```

**Option B: Local MongoDB**

If MongoDB is installed locally:
```
MONGO_DB_URL=mongodb://localhost:27017
```

#### 2. AWS Configuration

```env
AWS_ACCESS_KEY_ID=your_aws_access_key_here
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key_here
AWS_REGION=ap-south-1
```

**How to get AWS credentials:**

1. Log in to [AWS Management Console](https://console.aws.amazon.com)
2. Go to **IAM** (Identity and Access Management)
3. Click **Users** in the left sidebar
4. Click **Create user** (or select existing user)
5. Attach policy: **AmazonS3FullAccess**
6. Go to **Security credentials** tab
7. Click **Create access key**
8. Copy Access Key ID and Secret Access Key
9. Add to `.env` file

⚠️ **Security Warning**: Never share your AWS credentials. Treat them like passwords.

#### 3. AWS S3 Bucket Configuration

```env
TRAINING_BUCKET_NAME=customer-categorizer-training
PREDICTION_BUCKET_NAME=customer-categorizer-prediction
```

**How to create S3 buckets:**

1. Go to [AWS S3 Console](https://s3.console.aws.amazon.com/)
2. Click **Create bucket**
3. Enter bucket name (must be unique globally)
4. Select region (same as AWS_REGION)
5. Click **Create bucket**
6. Repeat for prediction bucket
7. Add bucket names to `.env`

#### 4. Application Configuration

```env
APP_HOST=0.0.0.0
APP_PORT=5000
APP_ENV=development
```

#### 5. Database Configuration

```env
DATABASE_NAME=customer_segmentation_db
COLLECTION_NAME=customer_marketing_data
```

#### 6. Model Configuration

```env
N_CLUSTERS=3
CLUSTERING_ALGORITHM=agglomerative
PCA_COMPONENTS=2
N_FEATURES_TO_SELECT=15
MODEL_EXPECTED_SCORE=0.6
MODEL_IMPROVEMENT_THRESHOLD=0.02
```

### Complete .env Example

```env
# MongoDB
MONGO_DB_URL=mongodb+srv://admin:password123@cluster0.xyz.mongodb.net/customer_db

# AWS
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
AWS_REGION=ap-south-1

# S3 Buckets
TRAINING_BUCKET_NAME=customer-categorizer-training
PREDICTION_BUCKET_NAME=customer-categorizer-prediction

# Application
APP_HOST=0.0.0.0
APP_PORT=5000
APP_ENV=development

# Database
DATABASE_NAME=customer_segmentation_db
COLLECTION_NAME=customer_marketing_data

# Model
N_CLUSTERS=3
CLUSTERING_ALGORITHM=agglomerative
PCA_COMPONENTS=2

# Logging
LOG_LEVEL=INFO
LOG_FILE_PATH=./src/artifact/logs/customer_segmentation.log

# Data
TRAIN_TEST_SPLIT_RATIO=0.2
RAW_DATA_PATH=./notebooks/marketing_campaign.csv
```

---

## Database Setup

### MongoDB Setup

#### Step 1: Choose MongoDB Type

**Option A: MongoDB Atlas (Recommended for Production)**

Best for cloud deployment and scalability.

1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Sign up for free account
3. Create organization and project
4. Create cluster (Free tier available)
5. Setup authentication
6. Get connection string
7. Add connection string to `.env`

**Option B: MongoDB Local Installation**

Best for local development.

**Windows:**
```bash
# Download MongoDB Community Edition
# https://www.mongodb.com/try/download/community

# Or use Chocolatey
choco install mongodb-community
```

**Linux (Ubuntu):**
```bash
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo systemctl start mongod
```

**Mac:**
```bash
brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb-community
```

#### Step 2: Verify MongoDB Connection

```bash
# Test with Python
python -c "from pymongo import MongoClient; client = MongoClient('your_connection_string'); print('Connected!' if client.server_info() else 'Failed')"
```

### Database Structure

The application creates the following collections:

**customer_marketing_data**
- Contains raw customer data
- Used for training the model
- Fields: Age, Income, Total_Spending, etc.

**clustered_data**
- Contains processed and clustered data
- Used for model evaluation
- Fields: Original features + cluster label

---

## AWS Configuration

### AWS IAM Setup

#### Create IAM User for Application

1. Go to [AWS IAM Console](https://console.aws.amazon.com/iam/)
2. Click **Users** → **Create user**
3. Enter username: `customer-categorizer-app`
4. Click **Next**
5. Click **Attach policies directly**
6. Search and select: **AmazonS3FullAccess**
7. Click **Next** → **Create user**

#### Generate Access Keys

1. Click on the newly created user
2. Go to **Security credentials** tab
3. Scroll to **Access keys**
4. Click **Create access key**
5. Select **Command Line Interface (CLI)**
6. Check the confirmation box
7. Click **Create access key**
8. Copy **Access Key ID** and **Secret Access Key**
9. Add to `.env` file

### S3 Bucket Configuration

#### Create Buckets

1. Go to [S3 Console](https://s3.console.aws.amazon.com/)
2. Click **Create bucket**
3. Bucket name: `customer-categorizer-training-{unique-id}`
4. Region: `ap-south-1` (or your preferred region)
5. Click **Create**
6. Repeat for `customer-categorizer-prediction-{unique-id}`

#### Configure Bucket Policies

For each bucket, add the following policy:

**Bucket Settings:**
1. Open bucket → **Permissions** tab
2. Click **Bucket Policy**
3. Add policy:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowUserOperations",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::ACCOUNT_ID:user/customer-categorizer-app"
            },
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::bucket-name",
                "arn:aws:s3:::bucket-name/*"
            ]
        }
    ]
}
```

Replace `ACCOUNT_ID` with your AWS account ID and `bucket-name` with your bucket name.

---

## Running the Application

### Development Mode

```bash
# Activate virtual environment
# Windows: .venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# Run application
python app.py
```

Access at: `http://localhost:5000`

### Production Mode

```bash
# Using Gunicorn with Uvicorn workers
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app --bind 0.0.0.0:5000
```

### Docker Deployment

#### Build Docker Image

```bash
docker build -t customer-categorizer:latest .
```

#### Run Docker Container

```bash
docker run -p 5000:5000 \
  -e MONGO_DB_URL="your_mongodb_url" \
  -e AWS_ACCESS_KEY_ID="your_access_key" \
  -e AWS_SECRET_ACCESS_KEY="your_secret_key" \
  -e AWS_REGION="ap-south-1" \
  -e TRAINING_BUCKET_NAME="your_bucket" \
  customer-categorizer:latest
```

---

## Testing the Application

### Manual Testing

1. Open browser: `http://localhost:5000`
2. Fill in customer details:
   - Age: 42
   - Education: 2 (Graduation)
   - Marital Status: 1 (Married)
   - Children: 2
   - Income: 58000
   - Total Spending: 1500
   - Fill other fields with reasonable values
3. Click **Predict Customer Cluster**
4. View result (Cluster 0, 1, or 2)

### API Testing with cURL

```bash
curl -X POST http://localhost:5000/ \
  -d "Age=42&Education=2&Marital_Status=1&Parental_Status=1&Children=2&Income=58000&Total_Spending=1500&Days_as_Customer=1236&Recency=58&Wines=635&Fruits=88&Meat=546&Fish=172&Sweets=88&Gold=88&Web=8&Catalog=10&Store=4&Discount_Purchases=7&Total_Promo=3&NumWebVisitsMonth=7"
```

### Training Pipeline Test

```bash
curl -X GET http://localhost:5000/train
```

---

## Troubleshooting

### Issue: "Environment variable AWS_ACCESS_KEY_ID is not set"

**Solution:**
1. Check if `.env` file exists in project root
2. Verify `.env` file has correct variable names
3. Make sure virtual environment is activated
4. Restart the application

```bash
# Verify environment variables are loaded
python -c "import os; print('AWS_ACCESS_KEY_ID' in os.environ)"
```

### Issue: MongoDB Connection Failed

**Solution:**
1. Check MongoDB connection string in `.env`
2. Verify MongoDB is running:
   ```bash
   # For local MongoDB
   net start MongoDB
   
   # For MongoDB Atlas
   Check internet connection and firewall
   ```
3. Test connection:
   ```bash
   python -c "from pymongo import MongoClient; MongoClient('your_connection_string').server_info()"
   ```

### Issue: AWS S3 Access Denied

**Solution:**
1. Verify AWS Access Key ID and Secret Access Key
2. Check IAM user has S3 permissions
3. Verify bucket names are correct and exist
4. Check bucket policies are correct

```bash
# Test AWS credentials
aws s3 ls --profile default
```

### Issue: "Prediction shows nothing"

**Solution:**
1. Check browser console for errors (F12)
2. Check application logs in `./src/artifact/logs/`
3. Verify all form fields are filled with valid data
4. Make sure data types match (numbers for numeric fields)

### Issue: Model Loading Error

**Solution:**
1. If AWS not configured, app runs in demo mode (should work)
2. Check S3 bucket and model file exist
3. Verify AWS credentials have S3 access
4. Check model file path in configuration

---

## Production Deployment Checklist

- [ ] All environment variables set correctly
- [ ] MongoDB Atlas cluster created and accessible
- [ ] AWS IAM user created with S3 permissions
- [ ] S3 buckets created and configured
- [ ] Dockerfile tested and optimized
- [ ] Environment variables not hardcoded
- [ ] Error logging enabled
- [ ] Security groups and firewall configured
- [ ] SSL/HTTPS configured (for production)
- [ ] Database backups configured
- [ ] Monitoring and alerts set up

---

## Security Best Practices

1. **Never commit `.env` file**: Add to `.gitignore`
2. **Use strong passwords**: For MongoDB and AWS
3. **Rotate credentials**: Regularly change access keys
4. **Use IAM roles**: Prefer roles over access keys
5. **Encrypt data**: Use HTTPS/SSL in production
6. **Monitor access**: Enable AWS CloudTrail
7. **Limit permissions**: Use least privilege principle
8. **Backup data**: Regular database backups
9. **Update dependencies**: Keep packages updated
10. **Use secrets manager**: For production (AWS Secrets Manager, Vault, etc.)

---

## Additional Resources

- [MongoDB Documentation](https://docs.mongodb.com/)
- [AWS S3 Documentation](https://docs.aws.amazon.com/s3/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com/)
- [Python-dotenv](https://python-dotenv.readthedocs.io/)

---

**Last Updated**: November 16, 2025  
**Version**: 1.0
