import streamlit as st

def load_css():
    st.markdown("""
    <style>

    /* =========================
       APP
    ========================== */

    .stApp{
        background:#F8FAFC;
    }

    .block-container{
        padding-top:1.5rem;
        padding-bottom:1rem;
    }

    /* =========================
       SIDEBAR
    ========================== */

    section[data-testid="stSidebar"]{
        background:#EEF2FF;
        border-right:1px solid #E5E7EB;
    }

    /* =========================
       HERO
    ========================== */

    .hero{
        background:white;
        border-radius:20px;
        padding:28px;
        box-shadow:0 8px 30px rgba(0,0,0,.08);
        margin-bottom:18px;
    }

    .hero-title{
        font-size:34px;
        font-weight:800;
        color:#1E3A8A;
    }

    .hero-subtitle{
        font-size:22px;
        font-weight:600;
        color:#374151;
        margin-top:6px;
    }

    .hero-desc{
        color:#6B7280;
        margin-top:10px;
        font-size:17px;
    }

    /* =========================
       METRIC CARDS
    ========================== */

    div[data-testid="stMetric"]{

        background:white;

        border-radius:18px;

        padding:20px;

        border-left:6px solid #2563EB;

        box-shadow:0 8px 20px rgba(0,0,0,.08);

        transition:.3s;

    }

    div[data-testid="stMetric"]:hover{

        transform:translateY(-6px);

        box-shadow:0 16px 30px rgba(0,0,0,.15);

    }

    div[data-testid="stMetricLabel"]{

        font-size:15px;

        font-weight:600;

    }

    div[data-testid="stMetricValue"]{

        font-size:34px;

        font-weight:800;

        color:#111827;

    }

    /* =========================
       HEADINGS
    ========================== */

    h1,h2,h3{
        color:#1F2937;
        font-weight:700;
    }

    /* =========================
       CHARTS
    ========================== */

    div[data-testid="stPlotlyChart"]{

        background:white;

        padding:18px;

        border-radius:18px;

        box-shadow:0 8px 24px rgba(0,0,0,.07);

    }

    /* =========================
       TABLE
    ========================== */

    div[data-testid="stDataFrame"]{

        background:white;

        border-radius:18px;

        padding:15px;

        box-shadow:0 8px 24px rgba(0,0,0,.08);

    }

    </style>
    """, unsafe_allow_html=True)

    