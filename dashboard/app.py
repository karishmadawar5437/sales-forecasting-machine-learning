# ==========================================================
# SALES FORECAST DASHBOARD
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Sales Forecast Dashboard",
    page_icon="📊",
    layout="wide"
)

# ==========================================================
# TITLE
# ==========================================================

st.title("📊 Sales Forecast Dashboard")

st.markdown(
"""
### AI & Data Science Project

Interactive dashboard for Historical Sales Analysis and
30-Day Sales Forecasting.
"""
)

st.markdown("---")

# ==========================================================
# LOAD DATA
# ==========================================================

daily_sales = pd.read_excel(
    "data/processed/daily_sales.xlsx"
)

future_sales = pd.read_excel(
    "data/processed/future_sales_forecast.xlsx"
)

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("📊 Dashboard")

st.sidebar.markdown("---")

st.sidebar.subheader("Project")

st.sidebar.write("Sales Forecasting")

st.sidebar.subheader("Developer")

st.sidebar.write("Karishma")

st.sidebar.subheader("Course")

st.sidebar.write("B.Tech AI & Data Science")

st.sidebar.markdown("---")

st.sidebar.subheader("Dataset")

st.sidebar.write(f"Historical Records : {len(daily_sales)}")

st.sidebar.write(f"Forecast Records : {len(future_sales)}")

st.sidebar.markdown("---")

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
        "💰 Historical Sales",
        f"₹ {total_historical_sales:,.2f}"
    )

with col2:

    st.metric(
        "📈 Forecast Sales",
        f"₹ {total_forecast_sales:,.2f}"
    )

with col3:

    st.metric(
        "📊 Average Forecast",
        f"₹ {average_forecast:,.2f}"
    )

with col4:

    st.metric(
        "🚀 Highest Forecast",
        f"₹ {maximum_forecast:,.2f}"
    )

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
    height=450,
    title_x=0.35,
    xaxis_title="Date",
    yaxis_title="Sales"
)

st.plotly_chart(fig_history, use_container_width="stretch")

# ==========================================================
# FORECAST SALES TREND
# ==========================================================

st.markdown("---")

st.subheader("🔮 30-Day Sales Forecast")

fig_forecast = px.line(
    future_sales,
    x="Order Date",
    y="Forecasted Sales",
    markers=True,
    title="Future Sales Forecast"
)

fig_forecast.update_layout(
    template="plotly_white",
    height=450,
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
    height=550,
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
    height=450
)

st.plotly_chart(fig_hist, use_container_width="stretch")
# ==========================================================
# FORECAST TABLE
# ==========================================================

st.markdown("---")

st.subheader("📋 30-Day Forecast Table")

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