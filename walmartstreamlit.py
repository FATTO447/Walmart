import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt

st.title("Walmart Sales Prediction")

df = pd.read_csv("C:\walmart\WalmartSales_cleaned .csv")
df.columns = df.columns.str.strip()

store_list = sorted(df["Store"].unique())
year_list = sorted(df["year"].unique())
month_list = ["No month selected"] + sorted(df['month'].unique())

store = st.selectbox("Select the store", store_list)
year = st.selectbox("Select the year", year_list)
month = st.selectbox("Select the month (optional)", month_list)

# Yearly Comparison
current_year_df = df[(df['Store'] == store) & (df['year'] == year)]
previous_year_df = df[(df['Store'] == store) & (df['year'] == year - 1)]

weekly_current_year = current_year_df.groupby('WeekOfYear')['Weekly_Sales'].sum().reset_index()
weekly_previous_year = previous_year_df.groupby('WeekOfYear')['Weekly_Sales'].sum().reset_index()

fig, ax = plt.subplots(figsize=(12,6))
ax.plot(weekly_current_year['WeekOfYear'], weekly_current_year['Weekly_Sales'], label=f"{year}")
ax.plot(weekly_previous_year['WeekOfYear'], weekly_previous_year['Weekly_Sales'], label=f"{year-1}", linestyle="--")
ax.set_title(f"Weekly Sales – Yearly Comparison (Store {store})")
ax.set_xlabel("Week")
ax.set_ylabel("Sales")
ax.legend()
st.pyplot(fig)

# Monthly Comparison (optional)
if month != "No month selected":
    current_month_df = df[(df['Store'] == store) & (df['year'] == year) & (df['month'] == month)]
    previous_month_df = df[(df['Store'] == store) & (df['year'] == year - 1) & (df['month'] == month)]

    if not current_month_df.empty and not previous_month_df.empty:
        weekly_current_month = current_month_df.groupby('WeekOfYear')['Weekly_Sales'].sum().reset_index()
        weekly_previous_month = previous_month_df.groupby('WeekOfYear')['Weekly_Sales'].sum().reset_index()

        fig, ax = plt.subplots(figsize=(12,6))
        ax.plot(weekly_current_month['WeekOfYear'], weekly_current_month['Weekly_Sales'], label=f"{year}")
        ax.plot(weekly_previous_month['WeekOfYear'], weekly_previous_month['Weekly_Sales'], label=f"{year-1}", linestyle="--")
        ax.set_title(f"Weekly Sales – Monthly Comparison (Store {store}, Month {month})")
        ax.set_xlabel("Week")
        ax.set_ylabel("Sales")
        ax.legend()
        st.pyplot(fig)
    else:
        st.warning("Month not available for both years. Cannot plot comparison.")
