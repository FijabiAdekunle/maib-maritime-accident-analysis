# dashboard.py - MAIB Maritime Accident Dashboard (2010–2024)
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Page config
st.set_page_config(
    page_title="MAIB Maritime Accidents",
    page_icon="anchor",
    layout="wide"
)

# Load data with caching
@st.cache_data
def load_data():
    df = pd.read_csv("processed/maib_dashboard_ready.csv", parse_dates=["Date"])
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.strftime("%b")
    df["YearMonth"] = df["Date"].dt.strftime("%Y-%m")
    return df

df = load_data()

# Title
st.title("MAIB Maritime Accident Interactive Dashboard")
st.markdown("**UK Marine Accident Investigation Branch (2010–2024)**")

# Sidebar
st.sidebar.header("Filters")
years = st.sidebar.multiselect("Year", options=sorted(df["Year"].unique()), default=df["Year"].unique())
vtypes = st.sidebar.multiselect("Vessel Type", options=sorted(df["Vessel Type"].dropna().unique()))
weathers = st.sidebar.multiselect("Weather", options=sorted(df["Weather"].unique()))
locations = st.sidebar.multiselect("Location", options=sorted(df["Location"].dropna().unique()))

# Apply filters
filtered = df.copy()
if years:
    filtered = filtered[filtered["Year"].isin(years)]
if vtypes:
    filtered = filtered[filtered["Vessel Type"].isin(vtypes)]
if weathers:
    filtered = filtered[filtered["Weather"].isin(weathers)]
if locations:
    filtered = filtered[filtered["Location"].isin(locations)]

# KPIs
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Incidents", len(filtered))
c2.metric("Vessel-Related", len(filtered.dropna(subset=["Vessel Type"])))
c3.metric("Total Fatalities", int(filtered["Fatalities"].sum()))
c4.metric("Dominant Weather", filtered["Weather"].mode()[0] if not filtered.empty else "N/A")

# Time trend
st.subheader("Incidents Over Time")
trend = filtered.groupby("YearMonth").size().reset_index(name="Count")
fig_trend = px.line(trend, x="YearMonth", y="Count", markers=True, title="Monthly Trend")
fig_trend.update_xaxes(tickangle=45)
st.plotly_chart(fig_trend, use_container_width=True)

# Vessel Type + Weather
col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 Vessel Types")
    top_vessels = filtered["Vessel Type"].value_counts().head(10)
    fig_v = px.bar(x=top_vessels.index, y=top_vessels.values, color=top_vessels.values,
                   color_continuous_scale="Blues")
    fig_v.update_layout(xaxis_title="Vessel Type", yaxis_title="Count")
    st.plotly_chart(fig_v, use_container_width=True)

with col2:
    st.subheader("Weather Conditions")
    weather_data = filtered["Weather"].value_counts()
    fig_w = px.pie(values=weather_data.values, names=weather_data.index, hole=0.5)
    st.plotly_chart(fig_w, use_container_width=True)

# Location bar
st.subheader("Incidents by Location")
loc_counts = filtered["Location"].value_counts()
fig_loc = px.bar(x=loc_counts.index, y=loc_counts.values, color=loc_counts.values,
                 color_continuous_scale="Viridis")
st.plotly_chart(fig_loc, use_container_width=True)

# Data table
st.subheader("Incident Details")
display_cols = ["Date", "Location", "Vessel Type", "Flag", "Weather", "Injury Type", "Fatalities", "Description"]
st.dataframe(filtered[display_cols].sort_values("Date", ascending=False).head(200), use_container_width=True)

# Footer
st.caption("Data: MAIB | Dashboard built with Streamlit + Plotly by *Fijabi J.Adekunle* | Nigeria, November 11, 2025")