# 🏏 IPL Performance Analytics (2008-2024)

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-CC2927?style=for-the-badge&logo=postgresql&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

An advanced **Data Science** & **Machine Learning** application that analyzes IPL historical data (2008-2024) and predicts player performance using predictive modeling.

---

## 🌐 Live Demo
Check out the live application here: **[https://ipl-performance-analytics-sfbhakzbyf2hdspvmetmva.streamlit.app/]**

---

## 📖 Project Overview
Developed by **Virajbhai Mavani**, this project combines **Data Engineering (SQL)**, **Exploratory Data Analysis (Pandas)**, and **Predictive Modeling (Scikit-Learn)**. It allows users to dive deep into player statistics and predicts the likelihood of a batsman scoring **30+ runs** against a specific opponent using a trained Machine Learning model.

## ✨ Key Features

### 📊 Player Performance Dashboard
* **Dynamic Analytics**: View career stats including Total Innings, Balls, and Runs.
* **Performance Metrics**: Real-time display of Strike Rate and Batting Average.
* **Player Search**: Filter and analyze data for any batsman in the IPL history.

### 🧠 Machine Learning Predictor
* **Random Forest Model**: Implemented using `sklearn.ensemble.RandomForestClassifier` with 200 estimators.
* **Predictive Insights**: Predicts if a player will cross the 30-run mark based on their strike rate, average, and head-to-head record.
* **Confidence Scoring**: Displays the match-specific probability percentage.

---

## 🛠️ Technical Stack & Libraries

| Category | Tools/Libraries |
| :--- | :--- |
| **Frontend** | Streamlit |
| **Database/Querying** | SQL (Data extraction & transformation) |
| **Machine Learning** | Scikit-Learn (Random Forest, Train-Test Split) |
| **Data Manipulation** | Pandas, NumPy |
| **Dataset Source** | Kaggle (IPL Ball-by-Ball 2008-2024) |

---

## 📂 Project Structure
```text
├── app.py                # Main Streamlit application with ML logic
├── ipl_career_stats.csv  # Aggregated player career statistics
├── ipl_batting.csv       # Filtered batting performance data
├── ipl_features.csv      # Feature-engineered data for ML training
├── IPL_Ball_by_Ball.csv  # Raw ball-by-ball historical records
├── IPL_Matches.csv       # Match-level metadata and results
└── README.md             # Project documentation
