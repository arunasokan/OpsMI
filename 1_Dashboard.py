import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- Page Config ---
st.set_page_config(page_title="OpsMI.ai Dashboard", layout="wide")

# --- Custom Styling ---
st.markdown("""
    <style>
        .big-font {font-size:28px !important; font-weight:600; color:#1E88E5;}
        .metric-card {
            background-color: #f9fafb;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# --- Load Data ---
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data/sample_ops_data.csv")
    except FileNotFoundError:
        # Create sample data if no file found
        data = {
            "Date": pd.date_range(datetime(2025, 9, 1), periods=30, freq="D"),
            "LOB": ["Claims", "Enrollment", "Billing", "Appeals"] * 7 + ["Claims", "Billing"],
            "Volume": [500 + i*10 for i in range(30)],
            "SLA%": [95 - (i % 5) for i in range(30)],
            "AHT": [420 + (i % 10)*5 for i in range(30)],
            "Productivity": [60 + (i % 6)*2 for i in range(30)]
        }
        df = pd.DataFrame(data)
    return df

df = load_data()

# --- Sidebar Filters ---
st.sidebar.header("🔍 Filters")
selected_lob = st.sidebar.multiselect(
    "Line of Business", df["LOB"].unique(), default=df["LOB"].unique()
)
date_range = st.sidebar.date_input(
    "Date Range",
    [df["Date"].min(), df["Date"].max()]
)

filtered = df[
    (df["LOB"].isin(selected_lob)) &
    (df["Date"] >= pd.to_datetime(date_range[0])) &
    (df["Date"] <= pd.to_datetime(date_range[1]))
]

# --- KPIs ---
total_volume = filtered["Volume"].sum()
avg_sla = filtered["SLA%"].mean()
avg_aht = filtered["AHT"].mean()
avg_prod = filtered["Productivity"].mean()

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="metric-card"><div class="big-font">📊</div>'
                f'<h4>Total Volume</h4><h2>{total_volume:,}</h2></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card"><div class="big-font">🎯</div>'
                f'<h4>Avg SLA%</h4><h2>{avg_sla:.1f}%</h2></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card"><div class="big-font">⏱️</div>'
                f'<h4>Avg AHT</h4><h2>{avg_aht:.0f} sec</h2></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="metric-card"><div class="big-font">⚡</div>'
                f'<h4>Productivity</h4><h2>{avg_prod:.1f}%</h2></div>', unsafe_allow_html=True)

st.markdown("---")

# --- Charts ---
tab1, tab2, tab3 = st.tabs(["📈 Volume Trend", "🎯 SLA Performance", "⚙️ Productivity by LOB"])

with tab1:
    fig_vol = px.line(
        filtered, x="Date", y="Volume", color="LOB",
        title="Volume Trend by Date",
        markers=True
    )
    st.plotly_chart(fig_vol, use_container_width=True)

with tab2:
    fig_sla = px.bar(
        filtered, x="Date", y="SLA%", color="LOB",
        title="Daily SLA% Performance",
        barmode="group"
    )
    st.plotly_chart(fig_sla, use_container_width=True)

with tab3:
    avg_by_lob = filtered.groupby("LOB", as_index=False)["Productivity"].mean()
    fig_prod = px.pie(
        avg_by_lob, names="LOB", values="Productivity",
        title="Average Productivity by LOB", hole=0.4
    )
    st.plotly_chart(fig_prod, use_container_width=True)

st.markdown("---")
st.caption("💡 Tip: You can upload your own data in `/data/sample_ops_data.csv` to see real metrics.")
