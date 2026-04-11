# 🏏 IPL Performance Analytics (2008-2024)

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-CC2927?style=for-the-badge&logo=postgresql&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge&logo=python&logoColor=white)

An advanced **Data Science** & **Machine Learning** application that analyzes IPL historical data (2008-2024) and predicts player performance using predictive modeling.

---

## 🌐 Live Demo

Check out the live application here:

**[Launch App](https://ipl-performance-analytics-sfbhakzbyf2hdspvmetmva.streamlit.app/)**

---

## 📖 Project Overview

Developed by **Virajbhai Mavani**, this project follows the complete Data Science lifecycle — from data loading and cleaning, SQL-based analysis using SQLite, exploratory data analysis with Matplotlib and Seaborn, feature engineering, to building a Random Forest ML model. The app handles large-scale IPL datasets to provide deep player insights and predicts the likelihood of a batsman scoring **30+ runs** in a match.

---

## 📊 Table of Contents

- [Live Demo](#-live-demo)
- [Project Overview](#-project-overview)
- [Dataset](#-dataset)
- [Tools & Libraries](#️-tools--libraries)
- [Project Structure](#-project-structure)
- [Key Features](#-key-features)
- [Key Findings](#-key-findings)
- [Model Performance](#-model-performance)
- [How to Run Locally](#️-setup--installation)

---

## 📦 Dataset

- **Source:** Kaggle — IPL Complete Dataset 2008-2024
- **Matches:** 1,095 matches
- **Deliveries:** 2,60,920 ball-by-ball records
- **Period:** 2008 – 2024
- **Link:** [IPL Complete Dataset](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020)

> **Note:** `deliveries.csv` (26MB) is not included due to GitHub size limits. Download from Kaggle and place in root directory.

---

## 🛠️ Tools & Libraries

| Category | Tools / Libraries |
| :--- | :--- |
| **Language** | Python 3.8+ |
| **Data Manipulation** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn, Plotly |
| **Database & SQL** | SQLite |
| **Machine Learning** | Scikit-Learn (Random Forest, Train-Test Split) |
| **Frontend** | Streamlit |
| **Dataset Source** | Kaggle (IPL Complete Dataset 2008-2024) |

---

## 📂 Project Structure

```text
ipl-performance-analytics/
│
├── app.py                  # Main Streamlit application
├── ipl_analysis.ipynb      # Data analysis & model building notebook
├── ipl_career_stats.csv    # Aggregated player career statistics
├── ipl_batting.csv         # Filtered batting performance data
├── ipl_features.csv        # Processed features for ML model training
├── matches.csv             # Historical match-level metadata
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## ✨ Key Features

### 📊 Interactive Player Dashboard
- **Career Analytics** — Total Innings, Balls faced, Runs scored
- **Performance Metrics** — Automated Strike Rate and Batting Average calculation
- **Dynamic Selection** — Analyze any player from the 2008-2024 IPL database
- **Interactive Charts** — Top 10 Run Scorers, 30+ Scores Count, Avg Runs vs Each Team

### 🎯 Machine Learning Predictor
- **Algorithm** — RandomForestClassifier (200 estimators)
- **Smart Features** — Strike Rate, Season Average, Opponent-specific records
- **Confidence Score** — Percentage-based probability output
- **Fallback Logic** — Uses career average when opponent-specific data unavailable

---

## ✅ What I Did

- 🔹 Loaded and explored 1,095 matches and 2,60,920 ball-by-ball delivery records
- 🔹 Performed Data Cleaning — handled missing values in city, winner, player_of_match columns
- 🔹 Built SQLite database and ran 6 SQL queries for team and player insights
- 🔹 Performed EDA using Matplotlib and Seaborn — top scorers, team performance, season trends
- 🔹 Engineered 3 ML features — Strike Rate, Batting Average, Avg vs Opponent
- 🔹 Trained Random Forest Classifier (200 estimators) to predict 30+ run probability
- 🔹 Deployed interactive Streamlit app with player dashboard and ML predictor

---

## 🔍 Key Findings

1. **`avg_vs_opponent`** (rolling last 5 matches) is the most context-aware feature
2. **Career stats alone** are not enough — recent opponent-specific form matters in T20
3. **Strike Rate + Batting Average + Opponent Record** are the 3 strongest predictors
4. **Mumbai Indians** and **Chennai Super Kings** have the most consistent performers
5. Dataset covers **16 years** of IPL data — 2008 to 2024

---

## 🤖 Model Performance

| Stage | Tool | Output |
|---|---|---|
| Data Loading | Pandas | 1,095 matches, 2,60,920 deliveries |
| Data Cleaning | Pandas | Handled missing values |
| SQL Analysis | SQLite | 6 business queries answered |
| EDA | Matplotlib, Seaborn | Player & match insights |
| Feature Engineering | Pandas | 3 ML-ready features |
| ML Model | Scikit-Learn | **69.66% accuracy** |
| Deployment | Streamlit | Live interactive dashboard |

---

## ⚙️ Setup & Installation

1. Clone this repository
   ```bash
   git clone https://github.com/viraj01-coder/ipl-performance-analytics
   cd ipl-performance-analytics
   ```

2. Install required libraries
   ```bash
   pip install -r requirements.txt
   ```

3. Download `deliveries.csv` from Kaggle and place in root directory

4. Run the Streamlit app
   ```bash
   streamlit run app.py
   ```

5. Open the notebook
   ```bash
   jupyter notebook ipl_analysis.ipynb
   ```

---

*Dataset: Kaggle IPL Complete Dataset 2008-2024 | Author: Virajbhai Mavani*
