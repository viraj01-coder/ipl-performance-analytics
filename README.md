# 🏏 IPL Performance Analytics (2008-2024)

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

An interactive **Machine Learning** web application that analyzes IPL player statistics from 2008 to 2024 and predicts high-scoring performances.

---

## 🌐 Live Demo
Check out the live application here: **[Deploying on Streamlit... Your URL Here]**

---

## 📖 Project Overview
This application, developed by **Virajbhai Mavani**, serves as a powerful dashboard for IPL fans and data analysts. It processes historical ball-by-ball data to provide career insights and uses a **Random Forest Classifier** to predict if a batsman will score **30 or more runs** in a given match based on their form and the opponent.

## ✨ Key Features

### 📊 Player Stats Dashboard
* **Detailed Metrics**: Real-time display of Total Innings, Balls Faced, and Total Runs.
* **Efficiency Tracking**: Instant calculation of Career Strike Rate and Batting Average.
* **Player Selection**: Dynamic dropdown menu featuring all unique IPL batsmen from 2008-2024.

### 🎯 30+ Runs Predictor
* **ML Engine**: Powered by a Random Forest model with 200 estimators.
* **Smart Features**: The model evaluates **Strike Rate**, **Season Average**, and **Average vs specific Opponent**.
* **Probabilistic Output**: Displays the exact percentage likelihood of a high-scoring innings.

---

## 🛠️ Technical Stack

| Component | Technology |
| :--- | :--- |
| **Frontend** | Streamlit (Python-based UI) |
| **Data Processing** | Pandas, NumPy |
| **Machine Learning** | Scikit-Learn (Random Forest) |
| **Dataset Source** | Kaggle (IPL Complete Dataset 2008-2024) |

---

## 📂 Project Structure
```text
├── app.py                # The main Streamlit application script
├── ipl_career_stats.csv  # Aggregated player career statistics
├── ipl_batting.csv       # Ball-by-ball batting records
├── ipl_features.csv      # Processed features for ML model training
├── IPL_Ball_by_Ball.csv  # Raw ball-by-ball historical data
├── IPL_Matches.csv       # Historical match results and metadata
└── README.md             # Project documentation
