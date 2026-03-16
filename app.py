import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.set_page_config(page_title="IPL Performance Analytics", page_icon="🏏", layout="wide")

@st.cache_resource
def load_data():
    career = pd.read_csv('ipl_career_stats.csv')
    batting = pd.read_csv('ipl_batting.csv')

    final_data = pd.read_csv('ipl_features.csv')
    X = final_data[['strike_rate', 'average_per_innings', 'avg_vs_opponent']]
    y = final_data['scored_30_plus']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    return model, career, batting

model, career, batting = load_data()

st.title("🏏 IPL Performance Analytics (2008-2024)")
st.markdown("**Data Science Project | Virajbhai Mavani**")
st.divider()

tab1, tab2 = st.tabs(["📊 Player Stats", "🎯 30+ Runs Predictor"])

with tab1:
    st.subheader("Player Performance Dashboard")
    all_batsmen = sorted(career['batter'].unique())
    selected_player = st.selectbox("Batsman Select Karo", all_batsmen)
    player_data = career[career['batter'] == selected_player].iloc[0]

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Total Innings", f"{int(player_data['total_innings']):,}")
    with col2:
        st.metric("Total Balls", f"{int(player_data['total_balls']):,}")
    with col3:
        st.metric("Total Runs", f"{int(player_data['total_runs']):,}")
    with col4:
        st.metric("Strike Rate", f"{player_data['strike_rate']:.2f}")
    with col5:
        st.metric("Batting Average", f"{player_data['average_per_innings']:.2f}")

with tab2:
    st.subheader("30+ Runs Prediction")
    col1, col2 = st.columns(2)
    with col1:
        pred_player = st.selectbox("Batsman Select Karo", all_batsmen, key='pred')
    with col2:
        all_teams = sorted(batting['bowling_team'].dropna().unique())
        opponent = st.selectbox("Opponent Team", all_teams)

    if st.button("🎯 Predict", use_container_width=True):
        player_stats = career[career['batter'] == pred_player].iloc[0]
        opp_avg = batting[
            (batting['batter'] == pred_player) &
            (batting['bowling_team'] == opponent)
        ]['avg_vs_opponent'].mean()

        if pd.isna(opp_avg):
            opp_avg = 0

        input_data = pd.DataFrame({
            'strike_rate': [player_stats['strike_rate']],
            'average_per_innings': [player_stats['average_per_innings']],
            'avg_vs_opponent': [opp_avg]
        })

        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1] * 100

        if prediction == 1:
            st.success(f"✅ {pred_player} is likely to score 30 or more runs in this match!")
        else:
            st.warning(f"⚠️ {pred_player} is unlikely to score 30 or more runs in this match!")

        st.info(f"**Probability: {probability:.1f}%**")
        st.info(f"**Avg vs {opponent}: {opp_avg:.1f}**")

st.divider()
st.markdown("*Dataset: IPL Complete Dataset 2008-2024 | Kaggle*")
