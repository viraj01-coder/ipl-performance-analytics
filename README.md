# 🏏 IPL Performance Analytics (2008-2024)

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-CC2927?style=for-the-badge&logo=postgresql&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

An advanced **Data Science** & **Machine Learning** application that analyzes IPL historical data (2008-2024) and predicts player performance using predictive modeling.

---

## 🌐 Live Demo
Check out the live application here: **[Your Streamlit App URL Here]**

---

## 📖 Project Overview
Developed by **Virajbhai Mavani**, this project integrates **Data Engineering (SQL)**, **Exploratory Data Analysis (Pandas)**, and **Predictive Modeling (Scikit-Learn)**. The app handles large-scale IPL datasets to provide deep player insights and uses a **Random Forest** model to predict the likelihood of a batsman scoring **30+ runs** in a match.

## ✨ Key Features

### 📊 Interactive Player Dashboard
* **Real-time Analytics**: Fetch and display career statistics like Total Innings, Balls, and Runs.
* **Performance Metrics**: Automated calculation of Strike Rate and Batting Average.
* **Dynamic Selection**: Analyze any player from the extensive IPL database (2008-2024).

### 🎯 Machine Learning Predictor
* **Algorithm**: Built with `RandomForestClassifier` (200 estimators) for robust classification.
* **Smart Features**: Uses player's Strike Rate, Season Average, and specific Record against Opponents.
* **Probability Output**: Provides a percentage-based confidence score for each prediction.

---

## 🛠️ Technical Stack & Libraries

| Category | Tools/Libraries |
| :--- | :--- |
| **Frontend** | Streamlit |
| **Database & Logic** | SQL & Python |
| **Machine Learning** | Scikit-Learn (Random Forest, Train-Test Split) |
| **Data Manipulation** | Pandas, NumPy |
| **Dataset Source** | Kaggle (IPL Complete Dataset 2008-2024) |

---

## 📂 Project Structure
```text
├── app.py                # Main Streamlit application script
├── ipl_career_stats.csv  # Aggregated player career statistics
├── ipl_batting.csv       # Filtered batting performance data
├── ipl_features.csv      # Processed features for ML model training
├── matches.csv           # Historical match-level metadata
└── README.md             # Project documentation
