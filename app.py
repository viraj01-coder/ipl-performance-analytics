import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="IPL Performance Analytics",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;600;700&family=Inter:wght@300;400;500&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    .stApp {
        background: linear-gradient(135deg, #0a0f1e 0%, #0d1b2a 50%, #0a1628 100%);
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0d1b2a 0%, #0a1628 100%);
        border-right: 1px solid #1e3a5f;
    }
    [data-testid="stSidebar"] .stMarkdown h2,
    [data-testid="stSidebar"] .stMarkdown h3 {
        color: #f97316;
        font-family: 'Rajdhani', sans-serif;
    }
    h1 {
        font-family: 'Rajdhani', sans-serif !important;
        font-size: 2.6rem !important;
        font-weight: 700 !important;
        background: linear-gradient(90deg, #f97316, #facc15);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 1px;
    }
    h2, h3 {
        font-family: 'Rajdhani', sans-serif !important;
        color: #e2e8f0 !important;
    }
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, #1e3a5f22, #1e3a5f44);
        border: 1px solid #1e3a5f;
        border-radius: 12px;
        padding: 16px !important;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    [data-testid="metric-container"]:hover {
        transform: translateY(-2px);
        border-color: #f97316;
    }
    [data-testid="metric-container"] label {
        color: #94a3b8 !important;
        font-size: 0.75rem !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    [data-testid="metric-container"] [data-testid="stMetricValue"] {
        color: #facc15 !important;
        font-family: 'Rajdhani', sans-serif !important;
        font-size: 1.8rem !important;
        font-weight: 700 !important;
    }
    .stTabs [data-baseweb="tab-list"] {
        background: #0d1b2a;
        border-radius: 10px;
        padding: 4px;
        gap: 4px;
        border: 1px solid #1e3a5f;
    }
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        color: #94a3b8;
        border-radius: 8px;
        font-family: 'Rajdhani', sans-serif;
        font-size: 1rem;
        font-weight: 600;
        padding: 8px 20px;
        border: none;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #f97316, #ea580c) !important;
        color: white !important;
    }
    .stSelectbox > div > div {
        background: #0d1b2a;
        border: 1px solid #1e3a5f;
        border-radius: 8px;
        color: #e2e8f0;
    }
    .stButton > button {
        background: linear-gradient(135deg, #f97316, #ea580c) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        font-family: 'Rajdhani', sans-serif !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        letter-spacing: 1px !important;
        padding: 12px 24px !important;
        box-shadow: 0 4px 15px #f9731633 !important;
        transition: all 0.2s ease !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px #f9731655 !important;
    }
    hr { border-color: #1e3a5f !important; margin: 1.5rem 0 !important; }
    .footer-text { color: #475569; font-size: 0.8rem; text-align: center; }
    @media (max-width: 768px) {
        h1 { font-size: 1.8rem !important; }
        [data-testid="metric-container"] { padding: 10px !important; }
    }
</style>
""", unsafe_allow_html=True)

# ─── Load Data & Model ────────────────────────────────────────────────────────
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

    return model, career, batting, final_data

model, career, batting, final_data = load_data()

all_batsmen = sorted(career['batter'].unique())
all_teams = sorted(batting['bowling_team'].dropna().unique())

# ─── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🏏 IPL Analytics")
    st.markdown("---")
    st.markdown("### 🔍 Filters")

    sidebar_player = st.selectbox("🧑 Choose Player", all_batsmen, key='sidebar_player')
    sidebar_team = st.selectbox("🏟️ Opponent Team", all_teams, key='sidebar_team')

    st.markdown("---")
    st.markdown("### 📊 Dataset Info")
    st.metric("Total Players", f"{len(career):,}")
    st.metric("Total Teams", f"{len(all_teams)}")

    st.markdown("---")
    st.markdown('<p class="footer-text">Dataset: IPL 2008–2024 | Kaggle<br>By Virajbhai Mavani</p>', unsafe_allow_html=True)

# ─── Header ───────────────────────────────────────────────────────────────────
st.title("🏏 IPL Performance Analytics")
st.markdown("**Data Science & ML Project &nbsp;|&nbsp; Virajbhai Mavani**")
st.divider()

# ─── Tabs ─────────────────────────────────────────────────────────────────────
tab1, tab2 = st.tabs(["📊 Player Stats", "🎯 30+ Runs Predictor"])

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — Player Stats
# ══════════════════════════════════════════════════════════════════════════════
with tab1:
    st.subheader(f"📋 {sidebar_player} — Career Overview")

    player_data = career[career['batter'] == sidebar_player].iloc[0]

    # Metric Cards
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("🏟️ Total Innings", f"{int(player_data['total_innings']):,}")
    with col2:
        st.metric("🎯 Total Balls", f"{int(player_data['total_balls']):,}")
    with col3:
        st.metric("🏆 Total Runs", f"{int(player_data['total_runs']):,}")
    with col4:
        st.metric("⚡ Strike Rate", f"{player_data['strike_rate']:.2f}")
    with col5:
        st.metric("📈 Avg / Innings", f"{player_data['average_per_innings']:.2f}")

    st.divider()

    col_left, col_right = st.columns(2)

    # Chart 1: Top 10 Run Scorers (selected player highlighted)
    with col_left:
        st.markdown("#### 🏆 Top 10 Run Scorers")
        top10 = career.nlargest(10, 'total_runs')[['batter', 'total_runs']].copy()
        if sidebar_player not in top10['batter'].values:
            player_row = career[career['batter'] == sidebar_player][['batter', 'total_runs']]
            top10 = pd.concat([top10, player_row]).drop_duplicates()
        top10 = top10.sort_values('total_runs', ascending=True)
        colors = ['#f97316' if b == sidebar_player else '#1e3a5f' for b in top10['batter']]

        fig1 = go.Figure(go.Bar(
            x=top10['total_runs'], y=top10['batter'],
            orientation='h', marker_color=colors, marker_line_width=0,
            text=top10['total_runs'].apply(lambda x: f"{x:,}"),
            textposition='outside', textfont=dict(color='#e2e8f0', size=11)
        ))
        max_runs = top10['total_runs'].max()
        fig1.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#e2e8f0', family='Inter'),
            xaxis=dict(showgrid=False, color='#94a3b8',
                       range=[0, max_runs * 1.18]),
            yaxis=dict(showgrid=False, color='#e2e8f0'),
            margin=dict(l=0, r=80, t=10, b=10), height=380,
        )
        st.plotly_chart(fig1, use_container_width=True)

    # Chart 2: 30+ scores — Top 10 + Selected Player highlighted
    with col_right:
        st.markdown("#### 🔥 30+ Scores Count — Top 10 Players")

        # Har player ke 30+ scores count karo
        scores_30 = final_data.groupby('batter')['scored_30_plus'].sum().reset_index()
        scores_30.columns = ['batter', 'count_30_plus']

        top10_30 = scores_30.nlargest(10, 'count_30_plus').copy()

        # Selected player agar top 10 mein nahi hai toh bhi add karo
        if sidebar_player not in top10_30['batter'].values:
            player_30 = scores_30[scores_30['batter'] == sidebar_player]
            if not player_30.empty:
                top10_30 = pd.concat([top10_30, player_30]).drop_duplicates()

        top10_30 = top10_30.sort_values('count_30_plus', ascending=True)
        colors2 = ['#f97316' if b == sidebar_player else '#1e3a5f' for b in top10_30['batter']]

        fig2 = go.Figure(go.Bar(
            x=top10_30['count_30_plus'],
            y=top10_30['batter'],
            orientation='h',
            marker_color=colors2,
            marker_line_width=0,
            text=top10_30['count_30_plus'].astype(int),
            textposition='outside',
            textfont=dict(color='#e2e8f0', size=11)
        ))
        max_30 = top10_30['count_30_plus'].max()
        fig2.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#e2e8f0', family='Inter'),
            xaxis=dict(showgrid=False, color='#94a3b8',
                       title='30+ Score Count', range=[0, max_30 * 1.18]),
            yaxis=dict(showgrid=False, color='#e2e8f0'),
            margin=dict(l=0, r=60, t=10, b=10), height=380, showlegend=False
        )
        st.plotly_chart(fig2, use_container_width=True)

        # Selected player ka 30+ count info
        player_count = scores_30[scores_30['batter'] == sidebar_player]['count_30_plus'].values
        if len(player_count) > 0:
            st.caption(f"🟠 **{sidebar_player}** ne **{int(player_count[0])}** baar 30+ runs score kiye hain")

    # Chart 3: Player avg runs vs each opponent team
    st.markdown(f"#### 🏟️ {sidebar_player} — Avg Runs vs Each Team")
    pvt = batting[batting['batter'] == sidebar_player].groupby('bowling_team')['avg_vs_opponent'].mean().reset_index()
    pvt.columns = ['Team', 'Avg Runs']
    pvt = pvt.sort_values('Avg Runs', ascending=False)

    if not pvt.empty:
        bar_colors = ['#f97316' if t == sidebar_team else '#1e3a5f' for t in pvt['Team']]
        fig3 = go.Figure(go.Bar(
            x=pvt['Team'], y=pvt['Avg Runs'],
            marker_color=bar_colors, marker_line_width=0,
            text=pvt['Avg Runs'].apply(lambda x: f"{x:.1f}"),
            textposition='outside', textfont=dict(color='#e2e8f0', size=10)
        ))
        max_avg = pvt['Avg Runs'].max()
        fig3.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(13,27,42,0.5)',
            font=dict(color='#e2e8f0', family='Inter'),
            xaxis=dict(showgrid=False, color='#94a3b8', tickangle=-35),
            yaxis=dict(showgrid=True, gridcolor='#1e3a5f', color='#94a3b8',
                       title='Avg Runs', range=[0, max_avg * 1.2]),
            margin=dict(l=0, r=0, t=30, b=80), height=350,
        )
        st.plotly_chart(fig3, use_container_width=True)
        st.caption(f"🟠 Highlighted = {sidebar_team}")
    else:
        st.info("Is player ke liye opponent data available nahi hai.")

# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 — 30+ Runs Predictor
# ══════════════════════════════════════════════════════════════════════════════
with tab2:
    st.subheader("🎯 30+ Runs Prediction")

    col1, col2 = st.columns(2)
    with col1:
        pred_player = st.selectbox("🧑 Choose Player", all_batsmen,
                                   index=all_batsmen.index(sidebar_player), key='pred')
    with col2:
        opponent = st.selectbox("🏟️ Opponent Team", all_teams,
                                index=all_teams.index(sidebar_team), key='pred_team')

    if st.button("🎯 Predict Performance", use_container_width=True):
        player_stats = career[career['batter'] == pred_player].iloc[0]
        opp_avg = batting[
            (batting['batter'] == pred_player) &
            (batting['bowling_team'] == opponent)
        ]['avg_vs_opponent'].mean()

        if pd.isna(opp_avg):
            opp_avg = player_stats['average_per_innings']
            no_data = True
        else:
            no_data = False

        input_data = pd.DataFrame({
            'strike_rate': [player_stats['strike_rate']],
            'average_per_innings': [player_stats['average_per_innings']],
            'avg_vs_opponent': [opp_avg]
        })

        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1] * 100

        st.divider()

        if prediction == 1:
            st.success(f"✅ **{pred_player}** is likely to score **30+ runs** vs {opponent}!")
        else:
            st.warning(f"⚠️ **{pred_player}** is unlikely to score **30+ runs** vs {opponent}.")

        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("🎯 Probability", f"{probability:.1f}%")
        with c2:
            st.metric("⚡ Career Strike Rate", f"{player_stats['strike_rate']:.2f}")
        with c3:
            st.metric("📈 Career Avg", f"{player_stats['average_per_innings']:.2f}")

        if no_data:
            st.info(f"ℹ️ **Avg vs {opponent}:** No data — using career average ({opp_avg:.1f})")
        else:
            st.info(f"ℹ️ **Avg vs {opponent}:** {opp_avg:.1f}")

        st.divider()

        # Probability Gauge
        st.markdown("#### 📊 Prediction Confidence")
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=probability,
            number={'suffix': '%', 'font': {'size': 36, 'color': '#facc15', 'family': 'Rajdhani'}},
            gauge={
                'axis': {'range': [0, 100], 'tickcolor': '#94a3b8',
                         'tickfont': {'color': '#94a3b8'}},
                'bar': {'color': '#f97316'},
                'bgcolor': '#0d1b2a',
                'bordercolor': '#1e3a5f',
                'steps': [
                    {'range': [0, 33], 'color': '#1e3a5f'},
                    {'range': [33, 66], 'color': '#1e4a7f'},
                    {'range': [66, 100], 'color': '#1e5a9f'},
                ],
                'threshold': {
                    'line': {'color': '#facc15', 'width': 3},
                    'thickness': 0.75, 'value': 50
                }
            }
        ))
        fig_gauge.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#e2e8f0', family='Inter'),
            height=280, margin=dict(l=20, r=20, t=20, b=20)
        )
        st.plotly_chart(fig_gauge, use_container_width=True)

        # Player vs opponents chart
        st.markdown(f"#### 🏟️ {pred_player} — Historical Avg vs All Teams")
        pvt2 = batting[batting['batter'] == pred_player].groupby('bowling_team')['avg_vs_opponent'].mean().reset_index()
        pvt2.columns = ['Team', 'Avg Runs']
        pvt2 = pvt2.sort_values('Avg Runs', ascending=False)

        if not pvt2.empty:
            colors2 = ['#f97316' if t == opponent else '#1e3a5f' for t in pvt2['Team']]
            fig4 = go.Figure(go.Bar(
                x=pvt2['Team'], y=pvt2['Avg Runs'],
                marker_color=colors2, marker_line_width=0,
                text=pvt2['Avg Runs'].apply(lambda x: f"{x:.1f}"),
                textposition='outside', textfont=dict(color='#e2e8f0', size=10)
            ))
            max_avg2 = pvt2['Avg Runs'].max()
            fig4.update_layout(
                paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(13,27,42,0.5)',
                font=dict(color='#e2e8f0', family='Inter'),
                xaxis=dict(showgrid=False, color='#94a3b8', tickangle=-35),
                yaxis=dict(showgrid=True, gridcolor='#1e3a5f', color='#94a3b8',
                           title='Avg Runs', range=[0, max_avg2 * 1.2]),
                margin=dict(l=0, r=0, t=30, b=80), height=320,
            )
            st.plotly_chart(fig4, use_container_width=True)
            st.caption(f"🟠 Highlighted = {opponent}")
