# ==========================================================
# SALES FORECAST DASHBOARD
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
from style import load_css

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Sales Forecast Dashboard",
    page_icon="📊",
    layout="wide"
)

load_css()

st.markdown("""
<div class="hero">

<div class="hero-title">
🚀 SalesVision 
</div>

<div class="hero-subtitle">
 Sales Forecasting Platform
</div>

<div class="hero-desc">
Predict • Analyze • Forecast • Optimize
</div>

<br>

<div style="display:flex;
justify-content:center;
gap:12px;
flex-wrap:wrap;">

<span style="
background:#2563EB;
color:white;
padding:8px 18px;
border-radius:25px;
font-size:14px;
font-weight:600;">
🤖 Random Forest
</span>

<span style="
background:#16A34A;
color:white;
padding:8px 18px;
border-radius:25px;
font-size:14px;
font-weight:600;">
📊 Interactive Dashboard
</span>

<span style="
background:#EA580C;
color:white;
padding:8px 18px;
border-radius:25px;
font-size:14px;
font-weight:600;">
📅 {selected_days}-Day Forecast
</span>

</div>

</div>
""", unsafe_allow_html=True)

# ==========================================================
# LOAD DATA
# ==========================================================

daily_sales = pd.read_excel(
    os.path.join(BASE_DIR, "data", "processed", "daily_sales.xlsx")
)

future_sales = pd.read_excel(
     os.path.join(BASE_DIR, "data", "processed","future_sales_forecast.xlsx")
)

future_sales["Order Date"] = pd.to_datetime(
    future_sales["Order Date"]
)

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("🚀 SalesVision ")

st.sidebar.caption("Business Intelligence Platform")

st.sidebar.markdown("---")

st.sidebar.subheader("⚙ Dashboard Settings")

forecast_days = st.sidebar.selectbox(
    "Forecast Horizon",
    ["7 Days", "15 Days", "30 Days"],
    index=2
)

# Convert selection into number of days
forecast_mapping = {
    "7 Days": 7,
    "15 Days": 15,
    "30 Days": 30
}

selected_days = forecast_mapping[forecast_days]

st.sidebar.subheader("🤖 Machine Learning Model")

st.sidebar.markdown("""
<div style="
background:white;
padding:15px;
border-radius:12px;
box-shadow:0 3px 10px rgba(0,0,0,.08);
border-left:5px solid #2563EB;
">

<b>Random Forest Regressor</b><br><br>

🌳 Estimator: Random Forest<br>
📈 Type: Regression<br>
⚡ Status: Production Ready

</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

st.sidebar.subheader("📌 Dashboard Modules")

st.sidebar.write("✅ Historical Analysis")
st.sidebar.write("✅ Sales Forecast")
st.sidebar.write("✅ Business Insights")
st.sidebar.write("✅ Download Forecast")

st.sidebar.markdown("---")

st.sidebar.info("""
**Developer**

Karishma Dawar

B.Tech AI & Data Science
""")
# ==========================================================
# FILTER FORECAST DATA
# ==========================================================

future_sales = future_sales.head(selected_days)

# ==========================================================
# KPI CALCULATIONS
# ==========================================================

total_historical_sales = daily_sales["Sales"].sum()

total_forecast_sales = future_sales["Forecasted Sales"].sum()

average_forecast = future_sales["Forecasted Sales"].mean()

maximum_forecast = future_sales["Forecasted Sales"].max()

# ==========================================================
# KPI CARDS
# ==========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "💰 Total Historical Sales",
        f"₹ {total_historical_sales:,.0f}"
    )

with col2:

    st.metric(
        "🔮 Predicted Sales",
        f"₹ {total_forecast_sales:,.0f}"
    )

with col3:

    st.metric(
        "📊 Average Daily Forecast",
        f"₹ {average_forecast:,.0f}"
    )

with col4:

    st.metric(
        "🚀 Peak Forecast",
        f"₹ {maximum_forecast:,.0f}"
    )

st.markdown("---")

# ==========================================================
# EXECUTIVE SUMMARY
# ==========================================================

st.markdown("### 📊 Executive Summary")

growth = (
    (total_forecast_sales / total_historical_sales) * 100
)

peak_date = future_sales.loc[
    future_sales["Forecasted Sales"].idxmax(),
    "Order Date"
]

highest_day = daily_sales.loc[
    daily_sales["Sales"].idxmax(),
    "index"
]

summary1, summary2 = st.columns(2)

with summary1:

    st.success(f"""
### 📈 Historical Performance

**Total Historical Sales**

₹ {total_historical_sales:,.0f}

**Highest Sales Day**

{pd.to_datetime(highest_day).strftime("%d %b %Y")}

**Average Daily Sales**

₹ {daily_sales['Sales'].mean():,.0f}
""")

with summary2:

    st.info(f"""
### 🔮 Forecast Insights

**30-Day Forecast**

₹ {total_forecast_sales:,.0f}

**Peak Forecast Date**

{peak_date.strftime("%d %b %Y")}

**Peak Forecast**

₹ {maximum_forecast:,.0f}
""")

st.warning(f"""
### 💼 Business Recommendation

• Maintain sufficient inventory for the upcoming demand.

• Prepare additional stock before **{peak_date.strftime("%d %b %Y")}**.

• The forecasted sales represent **{growth:.1f}%** of the historical sales dataset.

• Continue monitoring sales trends to optimize inventory planning and promotional campaigns.
""")

st.markdown("---")

# ==========================================================
# HISTORICAL SALES TREND
# ==========================================================

st.subheader("📈 Historical Sales Trend")

fig_history = px.line(
    daily_sales,
    x="index",
    y="Sales",
    markers=True,
    title="Historical Daily Sales"
)

fig_history.update_layout(
    template="plotly_white",
    height=400,
    title_x=0.35,
    xaxis_title="Date",
    yaxis_title="Sales"
)

st.plotly_chart(fig_history, use_container_width="stretch")

# ==========================================================
# FORECAST SALES TREND
# ==========================================================

st.markdown("---")

st.subheader(f"🔮 {selected_days}-Day Sales Forecast")

fig_forecast = px.line(
    future_sales,
    x="Order Date",
    y="Forecasted Sales",
    markers=True,
    title=f"{selected_days}-Day Sales Forecast"
)

fig_forecast.update_layout(
    template="plotly_white",
    height=400,
    title_x=0.35,
    xaxis_title="Date",
    yaxis_title="Forecast Sales"
)

st.plotly_chart(fig_forecast, use_container_width="stretch")

# ==========================================================
# COMBINED SALES TREND
# ==========================================================

st.markdown("---")

st.subheader("📊 Historical vs Forecast Comparison")

history = daily_sales.rename(
    columns={
        "index": "Date",
        "Sales": "Sales"
    }
)

history["Type"] = "Historical"

forecast = future_sales.rename(
    columns={
        "Order Date": "Date",
        "Forecasted Sales": "Sales"
    }
)

forecast["Type"] = "Forecast"

combined = pd.concat(
    [
        history[["Date", "Sales", "Type"]],
        forecast[["Date", "Sales", "Type"]]
    ],
    ignore_index=True
)

fig_combined = px.line(
    combined,
    x="Date",
    y="Sales",
    color="Type",
    markers=True,
    title="Historical vs Forecast Sales"
)

fig_combined.update_layout(
    template="plotly_white",
    height=450,
    title_x=0.35,
    xaxis_title="Date",
    yaxis_title="Sales"
)

st.plotly_chart(fig_combined, use_container_width="stretch")
# ==========================================================
# MONTHLY SALES ANALYSIS
# ==========================================================

st.markdown("---")

st.subheader("📅 Monthly Sales Analysis")

daily_sales["Month"] = pd.to_datetime(daily_sales["index"]).dt.strftime("%b")

monthly_sales = (
    daily_sales
    .groupby("Month")["Sales"]
    .sum()
    .reset_index()
)

fig_month = px.bar(
    monthly_sales,
    x="Month",
    y="Sales",
    text_auto=".2s",
    color="Sales",
    title="Monthly Sales"
)

fig_month.update_layout(
    template="plotly_white",
    height=500
)

st.plotly_chart(fig_month, use_container_width="stretch")
# ==========================================================
# SALES DISTRIBUTION
# ==========================================================

st.markdown("---")

st.subheader("📊 Sales Distribution")

fig_hist = px.histogram(
    daily_sales,
    x="Sales",
    nbins=30,
    title="Distribution of Historical Sales"
)

fig_hist.update_layout(
    template="plotly_white",
    height=400
)

st.plotly_chart(fig_hist, use_container_width="stretch")
# ==========================================================
# FORECAST TABLE
# ==========================================================

st.markdown("---")

st.subheader(f"📋 {selected_days}-Day Forecast Table")

st.dataframe(
    future_sales,
    use_container_width=True
)
# ==========================================================
# DOWNLOAD BUTTON
# ==========================================================

st.download_button(
    label="📥 Download Forecast CSV",
    data=future_sales.to_csv(index=False),
    file_name="future_sales_forecast.csv",
    mime="text/csv"
)
# ==========================================================
# BUSINESS INSIGHTS
# ==========================================================

st.markdown("---")

st.subheader("📌 Business Insights")

col1, col2 = st.columns(2)

with col1:
    st.success(f"""
    **Historical Sales**

    • Total Sales: ₹ {total_historical_sales:,.2f}

    • Average Daily Sales: ₹ {daily_sales['Sales'].mean():,.2f}

    • Maximum Sale: ₹ {daily_sales['Sales'].max():,.2f}

    • Minimum Sale: ₹ {daily_sales['Sales'].min():,.2f}
    """)

with col2:
    st.info(f"""
    **Forecast Summary**

    • Total Forecast: ₹ {total_forecast_sales:,.2f}

    • Average Forecast: ₹ {average_forecast:,.2f}

    • Maximum Forecast: ₹ {maximum_forecast:,.2f}

    • Forecast Days: {len(future_sales)}
    """)
    # ==========================================================
# PROJECT SUMMARY
# ==========================================================

st.markdown("---")

st.subheader("📖 Project Summary")

st.write("""
This dashboard was developed as part of a Sales Forecasting Machine Learning project.

The workflow included:

• Data Understanding

• Data Cleaning

• Exploratory Data Analysis

• Feature Engineering

• Model Building

• Model Evaluation

• 30-Day Sales Forecast

• Interactive Dashboard using Streamlit
""")
# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.caption(
"""
Developed by **Karishma**

B.Tech Artificial Intelligence & Data Science

Guru Jambheshwar University of Science and Technology
"""
)