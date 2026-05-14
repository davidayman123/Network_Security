# Network Security Project - Phishing Data Detection

## 📋 Project Overview
This is an MLOps project designed to detect phishing attacks using machine learning models. The project implements a complete machine learning pipeline with data ingestion, validation, transformation, and model training components.

---

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.8 or higher
- MongoDB (for data storage)
- pip or conda package manager

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd NetworkSecurity
   ```

2. **Create a Virtual Environment**
   ```bash
   # Using venv
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup Configuration**
   - Update configuration files in `networksecurity/constant/` directory as needed
   - Ensure MongoDB connection is properly configured
   - Check data schema in `data_schema/schema.yaml`

---

## 📁 Project Structure

```
NetworkSecurity/
├── networksecurity/              # Main package
│   ├── components/               # Pipeline components
│   │   ├── Data_ingestion.py     # Data loading & storage
│   │   ├── data_validation.py    # Data quality checks
│   │   ├── data_transformation.py # Feature engineering
│   │   └── model_trainer.py      # Model training
│   ├── pipeline/                 # ML pipeline orchestration
│   │   ├── training_pipeline.py  # Main training workflow
│   │   └── batch_predection.py   # Batch prediction
│   ├── entity/                   # Data models
│   │   ├── config_entity.py      # Configuration classes
│   │   └── artifact_entity.py    # Artifact tracking
│   ├── exception/                # Error handling
│   ├── logging/                  # Logging utilities
│   ├── utils/                    # Helper functions
│   └── cloud/                    # Cloud integration (S3)
│
├── Artifacts/                    # Generated artifacts
│   └── [timestamp]/              # Timestamped runs
│       ├── data_ingestion/       # Ingested raw data
│       ├── data_validation/      # Validation reports
│       ├── data_transformation/  # Transformed features
│       └── model_trainer/        # Trained models
│
├── data_schema/                  # Schema definitions
│   └── schema.yaml               # Data schema configuration
│
├── mlruns/                       # MLflow experiment tracking
├── logs/                         # Application logs
├── Network_Data/                 # Raw data files
├── templates/                    # HTML templates for web UI
├── Notebooks/                    # Jupyter notebooks for exploration
│
├── main.py                       # Entry point for pipeline
├── app.py                        # Flask web application
├── requirements.txt              # Python dependencies
├── Dockerfile                    # Docker configuration
├── setup.py                      # Package setup
└── README.md                     # This file
```

---

## 🔧 How to Run the Project

### Run the Training Pipeline
```bash
python main.py
```
This will:
- Ingest data from `Network_Data/phisingData.csv`
- Validate data quality
- Transform and engineer features
- Train machine learning models
- Generate artifacts with timestamps

### Run Web Application
```bash
python app.py
```
Access the application at `http://localhost:5000`

### Test MongoDB Connection
```bash
python test_mongodb.py
```

### Push Data to Cloud
```bash
python push_data.py
```

---

## 📝 How to Edit & Customize

### Edit Configuration
- **Data Schema**: Modify `data_schema/schema.yaml` to change input data structure
- **Constants**: Update `networksecurity/constant/training_pipeline/` for model parameters
- **Pipeline Config**: Edit entity files in `networksecurity/entity/config_entity.py`

### Edit Components

#### Data Ingestion (`networksecurity/components/Data_ingestion.py`)
- Modify data source paths
- Add new data validation rules
- Change data storage mechanism

#### Data Validation (`networksecurity/components/data_validation.py`)
- Add custom validation checks
- Update drift detection logic
- Modify report generation

#### Data Transformation (`networksecurity/components/data_transformation.py`)
- Add/remove feature engineering steps
- Modify preprocessing pipelines
- Adjust scaling/normalization

#### Model Trainer (`networksecurity/components/model_trainer.py`)
- Change machine learning model
- Adjust hyperparameters
- Modify training strategy

### Add New Features
1. Create new component in `networksecurity/components/`
2. Define entity/config in `networksecurity/entity/`
3. Integrate into pipeline in `networksecurity/pipeline/training_pipeline.py`
4. Update `main.py` if needed

### Logging & Debugging
- Check logs in `logs/` directory
- Use `networksecurity/logging/logger.py` for custom logging
- MLflow tracking results in `mlruns/` folder

---

## 📊 Output & Artifacts

After running the pipeline, artifacts are generated in the `Artifacts/` folder organized by timestamp:

- **Ingested Data**: Raw data after loading
- **Validation Reports**: `drift_report/report.yaml` with data quality metrics
- **Transformed Data**: `.npy` files with engineered features
- **Trained Models**: Model files in `trained_model/` directory

---

## 🐳 Docker Support

Build and run with Docker:
```bash
docker build -t network-security .
docker run network-security
```

---

## 📚 Additional Resources

- **Requirements**: See `requirements.txt` for all dependencies
- **Setup**: Check `setup.py` for package configuration
- **Schema**: Review `data_schema/schema.yaml` for data structure
- **Notebooks**: Explore `Notebooks/` for analysis and experimentation

---

## 🤝 Contributing

To contribute to this project:
1. Create a new branch for your feature
2. Make your changes following the project structure
3. Test thoroughly with `main.py`
4. Ensure all logs are generated correctly
5. Submit your changes

---

## ⚠️ Important Notes

- Ensure MongoDB is running before executing the pipeline
- Check `requirements.txt` and install all dependencies
- Verify data path in components before running
- MLflow tracks all experiments in `mlruns/` for model comparison

---

## 📧 Support

For issues or questions, please refer to the project documentation or create an issue in the repository.