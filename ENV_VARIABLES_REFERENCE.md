# Environment Variables & Configuration Details

## Complete Reference Guide

### Overview
This document provides comprehensive details about all environment variables and configuration options used by the Customer Categorizer application.

---

## Environment Variables Reference

### 1. Database Variables

#### MONGO_DB_URL
- **Type**: String (connection string)
- **Required**: Yes
- **Default**: None
- **Description**: MongoDB connection string for database operations
- **Examples**:
  ```
  # Local MongoDB
  MONGO_DB_URL=mongodb://localhost:27017
  
  # MongoDB Atlas
  MONGO_DB_URL=mongodb+srv://username:password@cluster.mongodb.net/dbname
  ```

#### DATABASE_NAME
- **Type**: String
- **Required**: No
- **Default**: `customer_segmentation_db`
- **Description**: Name of the database to use

#### COLLECTION_NAME
- **Type**: String
- **Required**: No
- **Default**: `customer_marketing_data`
- **Description**: Name of the collection containing customer data

---

### 2. AWS Configuration

#### AWS_ACCESS_KEY_ID
- **Type**: String (AWS credential)
- **Required**: No (optional - app works without for demo mode)
- **Default**: None
- **Description**: AWS Access Key ID for authentication
- **Security**: Never hardcode in application; use .env file
- **How to get**: 
  1. Go to AWS IAM Console
  2. Create or select user
  3. Generate Access Key
  4. Copy Access Key ID

#### AWS_SECRET_ACCESS_KEY
- **Type**: String (AWS credential)
- **Required**: No (optional - app works without for demo mode)
- **Default**: None
- **Description**: AWS Secret Access Key for authentication
- **Security**: Highly sensitive - treat like a password
- **How to get**:
  1. Same as Access Key ID
  2. Copy Secret Access Key immediately after creation

#### AWS_REGION
- **Type**: String
- **Required**: No
- **Default**: `ap-south-1`
- **Description**: AWS region for S3 operations
- **Common Values**:
  - `us-east-1` - US East (N. Virginia)
  - `us-west-2` - US West (Oregon)
  - `eu-west-1` - Europe (Ireland)
  - `ap-south-1` - Asia Pacific (Mumbai)
  - `ap-southeast-1` - Asia Pacific (Singapore)

---

### 3. S3 Bucket Configuration

#### TRAINING_BUCKET_NAME
- **Type**: String
- **Required**: No (optional for demo mode)
- **Default**: `customer-categorizer-training`
- **Description**: S3 bucket for storing trained models
- **Rules**:
  - Must be globally unique
  - Cannot contain uppercase letters
  - 3-63 characters long
  - Can contain hyphens

#### PREDICTION_BUCKET_NAME
- **Type**: String
- **Required**: No (optional for demo mode)
- **Default**: `customer-categorizer-prediction`
- **Description**: S3 bucket for storing predictions and results
- **Rules**: Same as training bucket

---

### 4. Application Configuration

#### APP_HOST
- **Type**: String (IP address)
- **Required**: No
- **Default**: `0.0.0.0`
- **Description**: Server host address to bind to
- **Common Values**:
  - `0.0.0.0` - Listen on all interfaces (production)
  - `127.0.0.1` - Localhost only (development)
  - `localhost` - Same as 127.0.0.1

#### APP_PORT
- **Type**: Integer
- **Required**: No
- **Default**: `5000`
- **Description**: Server port number
- **Valid Range**: 1-65535
- **Common Values**:
  - `80` - HTTP (requires admin)
  - `443` - HTTPS (requires admin)
  - `8000` - Common alternative
  - `5000` - Flask/development default

#### APP_ENV
- **Type**: String
- **Required**: No
- **Default**: `development`
- **Description**: Application environment
- **Valid Values**:
  - `development` - Development environment
  - `staging` - Staging environment
  - `production` - Production environment

---

### 5. Model Configuration

#### N_CLUSTERS
- **Type**: Integer
- **Required**: No
- **Default**: `3`
- **Description**: Number of customer clusters
- **Valid Range**: 2-10
- **Impact**: Higher values = more granular segmentation

#### CLUSTERING_ALGORITHM
- **Type**: String
- **Required**: No
- **Default**: `agglomerative`
- **Description**: Clustering algorithm to use
- **Valid Values**:
  - `agglomerative` - Hierarchical clustering
  - `kmeans` - K-means clustering
  - `birch` - BIRCH clustering

#### PCA_COMPONENTS
- **Type**: Integer
- **Required**: No
- **Default**: `2`
- **Description**: Number of PCA components for dimensionality reduction
- **Valid Range**: 1-21 (max features)
- **Impact**: Affects model complexity and performance

#### N_FEATURES_TO_SELECT
- **Type**: Integer
- **Required**: No
- **Default**: `15`
- **Description**: Number of features to select from total features
- **Valid Range**: 1-21
- **Impact**: Feature selection for model training

---

### 6. Model Performance

#### MODEL_EXPECTED_SCORE
- **Type**: Float
- **Required**: No
- **Default**: `0.6`
- **Description**: Minimum expected model accuracy/score
- **Valid Range**: 0.0-1.0
- **Impact**: Model acceptance threshold

#### MODEL_IMPROVEMENT_THRESHOLD
- **Type**: Float
- **Required**: No
- **Default**: `0.02`
- **Description**: Minimum improvement needed to accept new model
- **Valid Range**: 0.0-1.0
- **Example**: 0.02 = 2% improvement required

---

### 7. Data Configuration

#### TRAIN_TEST_SPLIT_RATIO
- **Type**: Float
- **Required**: No
- **Default**: `0.2`
- **Description**: Ratio of test data to total data
- **Valid Range**: 0.0-1.0
- **Example**: 0.2 = 20% test, 80% train

#### RAW_DATA_PATH
- **Type**: String (file path)
- **Required**: No
- **Default**: `./notebooks/marketing_campaign.csv`
- **Description**: Path to raw customer data

#### PROCESSED_DATA_PATH
- **Type**: String (file path)
- **Required**: No
- **Default**: `./notebooks/data/clustered_data.csv`
- **Description**: Path to processed clustered data

---

### 8. Logging Configuration

#### LOG_LEVEL
- **Type**: String
- **Required**: No
- **Default**: `INFO`
- **Description**: Logging verbosity level
- **Valid Values** (in order of verbosity):
  - `DEBUG` - Detailed information for debugging
  - `INFO` - General informational messages
  - `WARNING` - Warning messages
  - `ERROR` - Error messages
  - `CRITICAL` - Critical error messages

#### LOG_FILE_PATH
- **Type**: String (file path)
- **Required**: No
- **Default**: `./src/artifact/logs/customer_segmentation.log`
- **Description**: Path to log file

---

### 9. Debug/Development Configuration

#### DEBUG_MODE
- **Type**: Boolean (True/False)
- **Required**: No
- **Default**: `False`
- **Description**: Enable debug mode
- **Impact**: More detailed error messages, slower performance

#### VERBOSE_LOGGING
- **Type**: Boolean (True/False)
- **Required**: No
- **Default**: `False`
- **Description**: Enable verbose logging output
- **Impact**: More log messages, larger log files

---

## Configuration Examples

### Development Setup
```env
# Local development with MongoDB
MONGO_DB_URL=mongodb://localhost:27017
APP_HOST=127.0.0.1
APP_PORT=5000
APP_ENV=development
LOG_LEVEL=DEBUG
DEBUG_MODE=True
VERBOSE_LOGGING=True
```

### Production Setup with AWS
```env
# Production with MongoDB Atlas and AWS S3
MONGO_DB_URL=mongodb+srv://prod_user:password@cluster.prod.mongodb.net/customer_db
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
AWS_REGION=us-east-1
TRAINING_BUCKET_NAME=company-prod-models
PREDICTION_BUCKET_NAME=company-prod-predictions
APP_HOST=0.0.0.0
APP_PORT=5000
APP_ENV=production
LOG_LEVEL=INFO
DEBUG_MODE=False
VERBOSE_LOGGING=False
```

### Docker Setup
```env
# Docker container configuration
MONGO_DB_URL=mongodb://mongodb-service:27017
AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
APP_HOST=0.0.0.0
APP_PORT=5000
LOG_LEVEL=INFO
```

---

## Configuration Files

### config/schema.yaml
Defines the schema for input data validation.

```yaml
columns:
  Age: int
  Education: int
  Marital_Status: int
  Income: float
  Total_Spending: float
  # ... etc
```

### config/model.yaml
Specifies model training parameters.

```yaml
n_clusters: 3
clustering_algorithm: agglomerative
n_components: 2
random_state: 42
```

### config/prediction_schema.yaml
Defines schema for prediction input data.

---

## AWS Credentials Security

### Best Practices
1. **Never hardcode credentials** in code
2. **Use environment variables** for local development
3. **Use IAM roles** for EC2/Lambda deployments
4. **Use AWS Secrets Manager** for production
5. **Rotate credentials** every 90 days
6. **Delete old access keys** immediately
7. **Monitor usage** with CloudTrail
8. **Restrict permissions** (least privilege)

### AWS Credential Formats

**Access Key ID**: 20 alphanumeric characters
```
AKIAIOSFODNN7EXAMPLE
```

**Secret Access Key**: 40 characters (letters, numbers, +, /)
```
wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

---

## MongoDB Connection Strings

### Local MongoDB
```
mongodb://localhost:27017
mongodb://localhost:27017/database_name
```

### MongoDB Atlas
```
mongodb+srv://username:password@cluster.mongodb.net/database_name
mongodb+srv://username:password@cluster.mongodb.net/database_name?retryWrites=true&w=majority
```

### Connection String Parameters
- `retryWrites=true` - Automatic retry on connection failure
- `w=majority` - Write concern for data durability
- `maxPoolSize=10` - Connection pool size
- `serverSelectionTimeoutMS=5000` - Selection timeout

---

## Validation Rules

### Environment Variable Validation
```python
# Application validates:
- All required variables are set
- AWS credentials format is correct
- S3 bucket names follow AWS naming rules
- Port number is within valid range
- MongoDB connection string is valid
- File paths are accessible
```

---

## Troubleshooting Configuration Issues

### Issue: "Environment variable not found"
- **Solution**: Check .env file exists and variable name is correct

### Issue: "Invalid AWS credentials"
- **Solution**: Verify Access Key ID and Secret Key from AWS Console

### Issue: "MongoDB connection timeout"
- **Solution**: Check connection string, firewall rules, and MongoDB is running

### Issue: "S3 bucket access denied"
- **Solution**: Verify IAM user has S3 permissions and bucket exists

---

## Default Values Summary

| Variable | Default | Required |
|----------|---------|----------|
| MONGO_DB_URL | None | Yes* |
| AWS_ACCESS_KEY_ID | None | No** |
| AWS_SECRET_ACCESS_KEY | None | No** |
| APP_HOST | 0.0.0.0 | No |
| APP_PORT | 5000 | No |
| N_CLUSTERS | 3 | No |
| LOG_LEVEL | INFO | No |
| TRAIN_TEST_SPLIT_RATIO | 0.2 | No |

*Required for training; optional for prediction  
**Optional; app works in demo mode without AWS

---

**Last Updated**: November 16, 2025  
**Version**: 1.0
