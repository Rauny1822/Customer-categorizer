# Customer Categorizer - Customer Segmentation & Clustering System

## 📋 Project Overview

**Customer Categorizer** is an advanced machine learning application that performs automatic customer segmentation and clustering. It analyzes customer behavioral data and categorizes customers into distinct segments (Clusters 0, 1, or 2) based on their purchasing patterns, demographics, and engagement metrics.

This system helps businesses identify different customer types to enable targeted marketing strategies, personalized recommendations, and improved customer relationship management.

---

## 🎯 Key Features

- **Customer Segmentation**: Automatically clusters customers into 3 distinct categories
- **Web-Based Interface**: User-friendly FastAPI frontend for easy interaction
- **Real-time Predictions**: Instant customer cluster predictions based on input data
- **AWS S3 Integration**: Cloud-based model storage and retrieval
- **MongoDB Database**: Scalable data storage for training data
- **Demo Mode**: Works without AWS credentials for testing purposes
- **Data Validation**: Comprehensive data drift detection and schema validation
- **ML Pipeline**: End-to-end training and prediction pipelines

---

## 🏗️ Project Architecture

### Technology Stack

**Backend:**
- **FastAPI** - Modern web framework for building APIs
- **Uvicorn** - ASGI server for running the application
- **Scikit-learn** - Machine learning algorithms
- **XGBoost** - Advanced gradient boosting for clustering
- **Pandas & NumPy** - Data processing and analysis
- **Jinja2** - Template rendering for HTML

**Database & Storage:**
- **MongoDB** - NoSQL database for training data
- **AWS S3** - Cloud storage for trained models
- **Boto3** - AWS SDK for Python

**Data Quality:**
- **Evidently** - Data validation and drift detection
- **PyYAML** - Configuration file management

---

## 📁 Project Structure

```
Customer-Categorizer/
├── app.py                           # Main FastAPI application
├── requirements.txt                 # Python dependencies
├── Dockerfile                       # Docker configuration
├── setup.py                         # Package setup configuration
│
├── src/
│   ├── components/                  # ML pipeline components
│   │   ├── data_ingestion.py       # Load data from MongoDB
│   │   ├── data_validation.py      # Validate schema and detect drift
│   │   ├── data_transformation.py  # Feature engineering
│   │   ├── model_trainer.py        # Train clustering model
│   │   ├── model_evaluation.py     # Evaluate model performance
│   │   └── model_pusher.py         # Push model to S3
│   │
│   ├── pipeline/                    # Training and prediction pipelines
│   │   ├── train_pipeline.py       # End-to-end training pipeline
│   │   └── prediction_pipeline.py  # Real-time prediction pipeline
│   │
│   ├── ml/
│   │   └── model/
│   │       ├── estimator.py        # Customer segmentation model
│   │       └── s3_estimator.py     # S3-based model loading
│   │
│   ├── cloud_storage/               # AWS integration
│   │   └── aws_storage.py          # S3 operations
│   │
│   ├── configuration/               # External service configs
│   │   ├── aws_connection.py       # AWS client setup
│   │   └── mongo_db_connection.py  # MongoDB connection
│   │
│   ├── constant/                    # Configuration constants
│   │   ├── application.py          # App-level constants
│   │   ├── env_variable.py         # Environment variable keys
│   │   ├── database.py             # Database constants
│   │   ├── s3_bucket.py            # S3 bucket names
│   │   └── training_pipeline/      # Training pipeline configs
│   │
│   ├── entity/                      # Data classes and entities
│   │   ├── config_entity.py        # Configuration dataclasses
│   │   └── artifact_entity.py      # Pipeline artifact classes
│   │
│   ├── exception/                   # Custom exception handling
│   │   └── __init__.py             # CustomerException class
│   │
│   ├── logger/                      # Logging configuration
│   │   └── __init__.py             # Logger setup
│   │
│   ├── utils/                       # Utility functions
│   │   └── main_utils.py           # Helper functions
│   │
│   └── data_access/                 # Data access layer
│       └── customer_data.py        # Customer data operations
│
├── config/                          # Configuration files
│   ├── schema.yaml                 # Data schema definition
│   ├── model.yaml                  # Model configuration
│   └── prediction_schema.yaml      # Prediction input schema
│
├── notebooks/                       # Jupyter notebooks
│   ├── EDA.ipynb                   # Exploratory data analysis
│   ├── Feature_engineering_and_clustering.ipynb
│   ├── Feature_Selection_and_classification.ipynb
│   └── data/
│       ├── clustered_data.csv      # Processed data
│       └── marketing_campaign.csv  # Raw customer data
│
├── templates/                       # HTML templates
│   └── customer.html               # Frontend form and results
│
├── static/                          # Static files
│   └── css/
│       └── style.css               # Styling
│
├── scripts/                         # Setup scripts
│   ├── create_initial_setup.sh
│   └── delete_initial_setup.sh
│
├── docs/                            # Documentation
│   ├── manual_setup.md
│   └── automated_setup.md
│
└── README.md                        # This file
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+** installed
- **Git** for version control
- (Optional) **AWS credentials** for cloud storage
- (Optional) **MongoDB Atlas** account for remote database

### Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/Rauny1822/Customer-categorizer.git
cd Customer-categorizer
```

#### 2. Create Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. (Optional) Set Environment Variables
```bash
# Create a .env file in the project root
MONGO_DB_URL=your_mongodb_connection_string
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
```

### Running the Application

#### Start the Web Server
```bash
python app.py
```

The application will be available at: **http://localhost:5000**

#### Access the Web Interface
1. Open your browser and navigate to `http://localhost:5000`
2. Fill in customer information in the form
3. Click "Predict Customer Cluster"
4. View the cluster prediction result

---

## 📊 Customer Input Features

The application accepts **21 customer attributes** for prediction:

| Feature | Type | Description |
|---------|------|-------------|
| Age | Integer | Customer age in years |
| Education | Integer | 0=Basic, 1=2nd Cycle, 2=Graduation, 3=Master, 4=PhD |
| Marital Status | Integer | 0=Not Married, 1=Married |
| Parental Status | Integer | 0=No Kids, 1=Has Kids |
| Children | Integer | Number of children |
| Income | Float | Annual income |
| Total Spending | Float | Total amount spent |
| Days as Customer | Integer | Days since customer registration |
| Recency | Integer | Days since last purchase |
| Wines | Integer | Amount spent on wine |
| Fruits | Integer | Amount spent on fruits |
| Meat | Integer | Amount spent on meat |
| Fish | Float | Amount spent on fish |
| Sweets | Integer | Amount spent on sweets |
| Gold | Float | Amount spent on gold products |
| Web | Integer | Number of web purchases |
| Catalog | Integer | Number of catalog purchases |
| Store | Integer | Number of in-store purchases |
| Discount Purchases | Integer | Purchases with discount |
| Total Promo | Integer | Promotion offers accepted |
| NumWebVisitsMonth | Integer | Website visits per month |

---

## 🔄 Data Pipeline

### Training Pipeline

```
1. Data Ingestion
   ↓ (Load from MongoDB)
2. Data Validation
   ↓ (Schema check, Drift detection)
3. Data Transformation
   ↓ (Feature engineering, Preprocessing)
4. Model Training
   ↓ (Apply clustering algorithm)
5. Model Evaluation
   ↓ (Performance metrics)
6. Model Pusher
   ↓ (Upload to S3)
```

### Prediction Pipeline

```
1. Input Data Preparation
   ↓ (Convert to DataFrame)
2. Data Transformation
   ↓ (Apply preprocessing)
3. Model Loading
   ↓ (From S3 or local)
4. Prediction
   ↓ (Cluster assignment)
5. Return Result
```

---

## ⚙️ Configuration

### Application Settings (`src/constant/application.py`)
```python
APP_HOST = "0.0.0.0"
APP_PORT = 5000
```

### Data Schema (`config/prediction_schema.yaml`)
Defines the structure and data types for customer input data.

### Model Configuration (`config/model.yaml`)
Specifies clustering parameters and algorithm settings.

---

## 🐛 Recent Fixes & Improvements

### Version 1.1.0 (Current)

✅ **Fixed Issues:**
1. **Syntax Error in config_entity.py**
   - Removed duplicate `return self.__dict__` statement
   
2. **Evidently API Compatibility**
   - Updated to use statistical drift detection (compatible with v0.7.16)
   - Replaced deprecated `model_profile.Profile` with custom drift detection

3. **AWS Credential Handling**
   - Application now gracefully handles missing AWS credentials
   - Supports demo mode for testing without AWS configuration
   - Proper error logging and warnings

4. **HTML Template Display**
   - Fixed prediction result display in frontend
   - Result now shows only after prediction is made

✨ **Features Added:**
- Demo mode when AWS credentials are unavailable
- Better error messages and logging
- Improved template rendering

---

## 🔐 Security & Error Handling

- **Custom Exception Handling**: `CustomerException` class for detailed error messages
- **Logging**: Comprehensive logging to track application flow
- **Data Validation**: Schema validation and drift detection
- **AWS Security**: Credentials handled via environment variables (never hardcoded)

---

## 📈 Performance Metrics

The model is evaluated on:
- **Silhouette Score**: Measures cluster cohesion and separation
- **Davies-Bouldin Index**: Cluster quality metric
- **Within-Cluster Sum of Squares**: Compactness measure

---

## 🐳 Docker Support

Build and run the application in a Docker container:

```bash
# Build Docker image
docker build -t customer-categorizer .

# Run Docker container
docker run -p 5000:5000 -e AWS_ACCESS_KEY_ID=your_key -e AWS_SECRET_ACCESS_KEY=your_secret customer-categorizer
```

---

## 📚 API Endpoints

### GET /
- **Description**: Returns the prediction form page
- **Response**: HTML form with customer input fields

### POST /
- **Description**: Processes customer data and returns cluster prediction
- **Parameters**: Form data with 21 customer attributes
- **Response**: HTML page with prediction result (Cluster 0, 1, or 2)

### GET /train
- **Description**: Triggers the training pipeline
- **Response**: Success or error message

---

## 🧪 Testing

Example prediction test:
```bash
curl -X POST http://localhost:5000/ \
  -d "Age=42&Education=2&Marital_Status=1&Parental_Status=1&Children=2&Income=58000&Total_Spending=1500&Days_as_Customer=1236&Recency=58&Wines=635&Fruits=88&Meat=546&Fish=172&Sweets=88&Gold=88&Web=8&Catalog=10&Store=4&Discount_Purchases=7&Total_Promo=3&NumWebVisitsMonth=7"
```

**Expected Output**: Customer is in Cluster 1

---

## 🌐 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
Recommended platforms:
- **Azure Web App Service** (See `docs/manual_setup.md`)
- **AWS EC2 + Docker**
- **Heroku**
- **Google Cloud Run**

---

## 📝 Environment Variables

Create a `.env` file in the project root:

```env
# MongoDB Configuration
MONGO_DB_URL=mongodb+srv://username:password@cluster.mongodb.net/database

# AWS Configuration
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key

# AWS S3 Buckets
TRAINING_BUCKET_NAME=customer-categorizer-training
PREDICTION_BUCKET_NAME=customer-categorizer-prediction

# Application Configuration
APP_HOST=0.0.0.0
APP_PORT=5000
```

---

## 📖 Documentation

- **Manual Setup**: See `docs/manual_setup.md` for Azure deployment
- **Automated Setup**: See `docs/automated_setup.md` for quick start
- **Assignment**: See `assignment/assignment.md` for project requirements

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👤 Author

**Rauny1822**  
GitHub: [@Rauny1822](https://github.com/Rauny1822)  
Project Repository: [Customer-categorizer](https://github.com/Rauny1822/Customer-categorizer)

---

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on [GitHub Issues](https://github.com/Rauny1822/Customer-categorizer/issues)
- Check existing documentation in the `docs/` folder

---

## 🗂️ Dependencies

Key dependencies (see `requirements.txt` for full list):
- FastAPI 0.115.0
- Uvicorn 0.31.1
- Scikit-learn
- XGBoost 2.1.1
- Pandas
- NumPy
- PyMongo 4.10.1
- Boto3 1.34.0
- Evidently 0.4.27
- Jinja2 3.1.4
- Python-dotenv 1.0.1

---

## 🎓 How It Works

### Customer Clustering Process

1. **Data Collection**: Customer information is collected via the web form
2. **Preprocessing**: Data is cleaned, scaled, and transformed
3. **Feature Selection**: Relevant features are selected for clustering
4. **Model Prediction**: XGBoost clustering model assigns customer to a cluster
5. **Result Display**: Cluster prediction is shown to the user

### Cluster Characteristics

- **Cluster 0**: [High-value customers / Frequent buyers / etc.]
- **Cluster 1**: [Mid-level customers / Occasional buyers / etc.]
- **Cluster 2**: [Low-engagement customers / Inactive customers / etc.]

---

**Last Updated**: November 16, 2025  
**Current Version**: 1.1.0  
**Status**: ✅ Production Ready