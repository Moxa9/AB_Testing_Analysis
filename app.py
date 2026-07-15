import streamlit as st
import pandas as pd
import plotly.express as px
from statsmodels.stats.proportion import proportions_ztest

st.set_page_config(page_title="A/B Testing Dashboard", layout="wide")

st.title("📊 A/B Testing Analysis Dashboard")

# Load data
df = pd.read_csv("data/conversion_data.csv")

# KPIs
total_users = len(df)
total_conversions = df["Converted"].sum()
conversion_rate = df["Converted"].mean() * 100

col1, col2, col3 = st.columns(3)

col1.metric("Total Users", f"{total_users:,}")
col2.metric("Total Conversions", total_conversions)
col3.metric("Conversion Rate", f"{conversion_rate:.2f}%")

st.divider()

# Conversion rate by group
group_conversion = (
    df.groupby("Group")["Converted"]
    .mean()
    .reset_index()
)

group_conversion["Converted"] *= 100

fig = px.bar(
    group_conversion,
    x="Group",
    y="Converted",
    title="Conversion Rate by Group",
    labels={"Converted": "Conversion Rate (%)"}
)

st.plotly_chart(fig, use_container_width=True)

# Pie chart
pie = df["Converted"].replace({0: "Not Converted", 1: "Converted"})
fig2 = px.pie(
    names=pie,
    title="Converted vs Not Converted"
)

st.plotly_chart(fig2, use_container_width=True)

# Statistical test
successes = [
    df[df.Group=="A"]["Converted"].sum(),
    df[df.Group=="B"]["Converted"].sum()
]

observations = [
    len(df[df.Group=="A"]),
    len(df[df.Group=="B"])
]

z, p = proportions_ztest(successes, observations)

st.subheader("Hypothesis Test")

st.write(f"**Z Statistic:** {z:.4f}")
st.write(f"**P Value:** {p:.6f}")

if p < 0.05:
    st.success("Version B performs significantly better than Version A.")
else:
    st.warning("No statistically significant difference was found.")