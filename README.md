# 🌧️ Rainfall Prediction using Decision Tree Classifier

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Web%20Application-green.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📖 Project Overview

This project predicts whether rainfall is expected based on historical weather parameters using a **Decision Tree Classifier**. It demonstrates the complete Machine Learning workflow, including data preprocessing, exploratory data analysis (EDA), model training, evaluation, visualization, and deployment through a Flask web application.

The project is designed for educational purposes and showcases the implementation of an end-to-end machine learning pipeline.

---

## ✨ Features

- 📊 Exploratory Data Analysis (EDA)
- 🧹 Data Preprocessing
- 🌳 Decision Tree Classification
- 📈 Model Training & Testing
- 🎯 Prediction using weather parameters
- 📉 Model Evaluation
  - Accuracy Score
  - Classification Report
  - Confusion Matrix
- 📌 Feature Importance Visualization
- 🌲 Decision Tree Visualization
- 💾 Model Saving using Joblib
- 🌐 Flask-based Web Application
- 🎨 User-friendly Prediction Interface

---

## 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Manipulation |
| NumPy | Numerical Computation |
| Scikit-learn | Machine Learning |
| Matplotlib | Data Visualization |
| Flask | Web Deployment |
| Joblib | Model Serialization |

---

## 📂 Project Structure

```text
Rainfall_Prediction/
│
├── Rainfall.csv
├── train_model.py
├── eda.py
├── app.py
├── requirements.txt
├── README.md
│
├── model/
│   └── rainfall_model.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── histograms.png
├── rainfall_distribution.png
├── correlation_matrix.png
├── confusion_matrix.png
├── feature_importance.png
└── decision_tree.png
```

---

## 📊 Dataset

The dataset contains weather-related attributes used for rainfall prediction.

### Features

- Day
- Pressure
- Maximum Temperature
- Temperature
- Minimum Temperature
- Humidity

### Target Variable

- Rainfall
  - Yes
  - No

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/Rainfall_Prediction.git
```

Move into the project directory

```bash
cd Rainfall_Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Step 1: Train the Model

```bash
python train_model.py
```

This will:

- Load the dataset
- Preprocess the data
- Train the Decision Tree model
- Evaluate the model
- Save the trained model as:

```text
model/rainfall_model.pkl
```

---

### Step 2: Run EDA (Optional)

```bash
python eda.py
```

This generates:

- Histograms
- Rainfall Distribution
- Correlation Matrix

---

### Step 3: Start the Flask Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📈 Model Workflow

```text
Weather Dataset
       │
       ▼
Data Preprocessing
       │
       ▼
Train-Test Split
       │
       ▼
Decision Tree Classifier
       │
       ▼
Model Evaluation
       │
       ▼
Save Trained Model
       │
       ▼
Flask Web Application
       │
       ▼
Rainfall Prediction
```

---

## 📊 Evaluation Metrics

The model is evaluated using:

- Accuracy Score
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

## 📷 Project Outputs

The project generates the following visualizations:

- Histogram of Features
- Rainfall Distribution
- Correlation Matrix
- Confusion Matrix
- Feature Importance Graph
- Decision Tree Visualization

---

## 💻 Web Application

The Flask application allows users to:

- Enter weather parameters
- Predict rainfall instantly
- View results through a simple and interactive interface

---

## 🚀 Future Improvements

- Random Forest Classifier
- XGBoost Implementation
- Live Weather API Integration
- Cloud Deployment
- Responsive UI Design
- Prediction Probability
- Model Comparison Dashboard

---

## 📚 Learning Outcomes

This project demonstrates:

- Data Preprocessing
- Exploratory Data Analysis
- Supervised Machine Learning
- Decision Tree Classification
- Model Evaluation Techniques
- Model Deployment with Flask
- GitHub Project Management

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Open a Pull Request.

---

## 👩‍💻 Author

**Purvi**

B.Tech – Artificial Intelligence and Machine Learning 
Ajay Kumar Garg Engineering College

GitHub: https://github.com/Purvikulada

LinkedIn: https://www.linkedin.com/in/purvi-1544a6346

---

## ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.
