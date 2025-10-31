import streamlit as st
from streamlit_option_menu import option_menu

# --- Page Config ---
st.set_page_config(
    page_title="OpsMI.ai - Your Operations, Explained by AI",
    page_icon="📊",
    layout="wide",
)

# --- Custom CSS (shadcn-inspired aesthetic) ---
st.markdown("""
    <style>
    :root {
        --accent-color: #007aff;
        --bg-color: #f8f9fb;
        --card-bg: #ffffff;
        --text-color: #1a1a1a;
        --muted-text: #6b7280;
    }

    body {
        background-color: var(--bg-color);
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background-color: var(--bg-color);
    }

    h1, h2, h3 {
        color: var(--text-color);
        font-weight: 700;
    }

    p {
        color: var(--muted-text);
    }

    .hero {
        text-align: center;
        padding: 3rem 0;
        background-color: var(--card-bg);
        border-radius: 20px;
        box-shadow: 0 3px 12px rgba(0,0,0,0.05);
        margin-bottom: 2rem;
    }

    .hero h1 {
        font-size: 2.8rem;
        margin-bottom: 0.5rem;
        color: var(--text-color);
    }

    .hero h3 {
        color: var(--muted-text);
        font-weight: 400;
    }

    .feature-card {
        background-color: var(--card-bg);
        padding: 1.5rem;
        border-radius: 16px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        transition: all 0.2s ease;
    }

    .feature-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    }

    .cta {
        text-align: center;
        padding: 2rem;
        background-color: var(--accent-color);
        color: white;
        border-radius: 16px;
        margin-top: 2rem;
    }

    .cta h3 {
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
with st.sidebar:
    selected = option_menu(
        "OpsMI.ai",
        ["🏠 Home", "📊 Dashboard", "🧠 AI Insights", "🎙 Voice Briefing", "⚙️ Settings"],
        icons=["house", "bar-chart", "cpu", "mic", "gear"],
        menu_icon="diagram-3",
        default_index=0,
    )

# --- Home Page ---
if selected == "🏠 Home":
    st.markdown('<div class="hero">', unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/906/906175.png", width=100)
    st.markdown("## **OpsMI.ai**")
    st.markdown("### *Your operations, explained by AI.*")
    st.write(
        "Get real-time performance insights, AI-generated summaries, and voice briefings that help you stay ahead of SLAs, productivity goals, and client expectations."
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # --- Features Section ---
    st.subheader("✨ Why OpsMI.ai?")
    cols = st.columns(3)
    with cols[0]:
        st.markdown(
            """
            <div class='feature-card'>
                <h4>📊 Unified Dashboard</h4>
                <p>Monitor KPIs across LOBs and geographies — no manual aggregation needed.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with cols[1]:
        st.markdown(
            """
            <div class='feature-card'>
                <h4>🧠 AI-Powered Insights</h4>
                <p>Spot anomalies, SLA risks, and trend shifts automatically, explained in plain English.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with cols[2]:
        st.markdown(
            """
            <div class='feature-card'>
                <h4>🎙 Executive Voice Briefing</h4>
                <p>Get a 2-minute spoken summary of your daily operations, powered by AI voice.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # --- CTA ---
    st.markdown(
        """
        <div class='cta'>
            <h3>💡 See your operations like never before.</h3>
            <p>Start with a free pilot and experience AI-driven insights in action.</p>
            <a href="#" style="text-decoration:none;">
                <button style="background:white; color:#007aff; border:none; padding:10px 25px; border-radius:10px; font-weight:600; cursor:pointer;">
                    🚀 Request a Demo
                </button>
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# --- Placeholder for other pages ---
else:
    st.info("This page is under development. Coming soon!")

