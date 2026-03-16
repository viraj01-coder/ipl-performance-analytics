# 🏏 IPL Performance Analytics (2008–2024) + 30+ Runs Predictor

Interactive web app + data analysis project that lets you explore IPL batting statistics (2008–2024) and **predicts whether a batsman is likely to score 30+ runs** against a specific opponent team.

Built with **Streamlit**, **Pandas**, **Scikit-learn (RandomForest)** and **SQLite**.

Live Demo → (add link when you deploy — Railway / Streamlit Community Cloud / Hugging Face)

<br>

## ✨ Features

- Player career statistics dashboard (runs, strike rate, average, innings, balls faced)
- **30+ Runs Probability Predictor** using Random Forest Classifier (~70% accuracy)
- Historical average vs specific opponent team considered in prediction
- Clean, responsive UI with metrics cards and success/warning messages
- Data cleaning, feature engineering and modeling done in Jupyter notebook

<br>

## 📊 Datasets Used

- `matches.csv` — match-level information (winner, venue, toss, etc.)
- `deliveries.csv` — ball-by-ball data (runs, extras, wickets, etc.)

→ Source: IPL Complete Dataset 2008–2024 (Kaggle)

<br>

## 🛠️ Tech Stack

- **Frontend / App** → Streamlit
- **Data Processing** → Pandas, NumPy
- **Machine Learning** → scikit-learn (RandomForestClassifier)
- **Modeling notebook** → Jupyter Notebook
- **In-memory database** → SQLite (for quick SQL-style analysis)

<br>

## Project Structure

```text
IPL-Performance-Analytics/
├── app.py                      # Streamlit web application
├── ipl_analysis.ipynb          # Complete data cleaning + EDA + feature engineering + modeling
├── ipl_career_stats.csv        # Final player career aggregates
├── ipl_batting.csv             # Batter performance vs each opponent team
├── ipl_features.csv            # Training dataset for the model
├── matches.csv                 # (input) match metadata
├── deliveries.csv              # (input) ball-by-ball data
├── requirements.txt            # dependencies
└── README.md
