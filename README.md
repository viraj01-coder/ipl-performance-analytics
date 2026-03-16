# 🏏 IPL Performance Analytics (2008-2024)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-CC2927?style=for-the-badge&logo=postgresql&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

An advanced **Data Science** & **Machine Learning** application that analyzes IPL historical data (2008-2024) and predicts player performance using predictive modeling.

---

## 🌐 Live Demo
Check out the live application here: **[https://ipl-performance-analytics-sfbhakzbyf2hdspvmetmva.streamlit.app/]**

---

## 📖 Project Overview
Developed by **Virajbhai Mavani**, this project integrates **Data Engineering (SQL)**, **Exploratory Data Analysis (Pandas)**, and **Predictive Modeling (Scikit-Learn)**. The app handles large-scale IPL datasets to provide deep player insights and uses a **Random Forest** model to predict the likelihood of a batsman scoring **30+ runs** in a match.

## ✨ Key Features

### 📊 Interactive Player Dashboard
**Career Analytics**: Displays complete career statistics including Total Innings, Balls faced, and Runs scored.
* **Performance Metrics**: Automated calculation of Strike Rate and Batting Average.
* **Dynamic Selection**: Analyze any player from the extensive IPL database (2008-2024).
* **Interactive Charts**: Top 10 Run Scorers, 30+ Scores Count, and Avg Runs vs Each Team.

### 🎯 Machine Learning Predictor
* **Algorithm**: Built with `RandomForestClassifier` (200 estimators) for robust classification.
* **Smart Features**: Uses player's Strike Rate, Season Average, and specific Record against Opponents.
* **Probability Output**: Provides a percentage-based confidence score for each prediction.
* **Fallback Logic**: Uses career average when opponent-specific data is unavailable.

---

## 🛠️ Technical Stack & Libraries
| Category | Tools/Libraries |
| :--- | :--- |
| **Frontend** | Streamlit |
| **Visualization** | Plotly |
| **Database & Logic** | SQL (SQLite) & Python |
| **Machine Learning** | Scikit-Learn (Random Forest, Train-Test Split) |
| **Data Manipulation** | Pandas, NumPy |
| **Dataset Source** | Kaggle (IPL Complete Dataset 2008-2024) |

---

## 📂 Project Structure
```text
├── app.py                # Main Streamlit application script
├── ipl_analysis.ipynb    # Data analysis & model building notebook
├── ipl_career_stats.csv  # Aggregated player career statistics
├── ipl_batting.csv       # Filtered batting performance data
├── ipl_features.csv      # Processed features for ML model training
├── matches.csv           # Historical match-level metadata
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 📦 Dataset
The `deliveries.csv` file (26MB) is not included in this repository due to size limits.

Download it from Kaggle and place it in the root directory to run the notebook:
👉 [IPL Complete Dataset 2008-2024](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020)

---

## ⚙️ Setup & Installation
```bash
git clone https://github.com/viraj01-coder/ipl-performance-analytics
cd ipl-performance-analytics
pip install -r requirements.txt
streamlit run app.py
```
