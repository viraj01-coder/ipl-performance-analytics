import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.utils.class_weight import compute_sample_weight

st.set_page_config(page_title="IPL Performance Analytics", page_icon="🏏", layout="wide")

@st.cache_resource
def load_data():
    career = pd.read_csv('ipl_career_stats.csv')
    batting = pd.read_csv('ipl_batting.csv')
    
    # Model train karo
    features = ['strike_rate', 'average_per_innings', 'avg_vs_opponent']
    
    batting['scored_30_plus'] = (batting['runs_scored'] >= 30).astype(int)
    
    data = batting.merge(
        career[['batter', 'strike_rate', 'average_per_innings']], 
        on='batter', how='left'
    ).dropna(subset=features)
    
    X = data[features]
    y = data['scored_30_plus']
    
    weights = compute_sample_weight('balanced', y)
    
    model = GradientBoostingClassifier(
        n_estimators=100, max_depth=4,
        learning_rate=0.1, random_state=42
    )
    model.fit(X, y, sample_weight=weights)
    
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
        st.metric("Batting Average", f"{player_data['batting_average']:.2f}")

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
            st.success(f"✅ {pred_player} ke 30+ runs karne ke chances hain!")
        else:
            st.warning(f"⚠️ {pred_player} ke 30+ runs karne ke chances kam hain!")
        
        st.info(f"**Probability: {probability:.1f}%**")
        st.info(f"**Avg vs {opponent}: {opp_avg:.1f}**")

st.divider()
st.markdown("*Dataset: IPL Complete Dataset 2008-2024 | Kaggle*")
