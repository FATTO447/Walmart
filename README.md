# Walmart
Overview

This project analyzes Walmart sales data using SQL, Python, and machine learning to understand patterns in store-level revenue and forecast weekly sales. It combines data engineering, exploratory data analysis (EDA), predictive modeling, and interactive visualization to provide actionable insights for retail decision-making.

Features

Data Analysis: Cleaned and transformed Walmart sales data; extracted features such as year, month, week of year, day of week, and holiday labels.

SQL Aggregation: Calculated total and holiday-specific sales per store using CTEs and window functions, enabling comparisons across events and stores.

EDA & Visualization: Explored weekly and monthly trends, compared holiday vs. non-holiday sales, and identified seasonal patterns using Matplotlib and Seaborn.

Machine Learning & Forecasting:

Built predictive models using Random Forest and LightGBM.

Performed GridSearch for hyperparameter optimization.

Implemented a pipeline to streamline preprocessing, feature selection, and modeling.

Interactive Dashboard: Developed with Streamlit to allow users to select year, store, and month and view time-series sales plots dynamically.

Key Insights

Holiday Impact: Major holidays (Super Bowl, Labor Day, Thanksgiving, Christmas) significantly boost weekly sales.

Peak Months: November and December consistently show the highest sales.

Top Sales Year: 2011 had the highest overall sales compared to other years in the dataset.

Tech Stack

Languages & Tools: Python, SQL, Jupyter Notebook, Streamlit

Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, LightGBM

Database: MySQL (used for aggregations and queries)

Machine Learning: Random Forest, LightGBM, GridSearchCV

Folder Structure
project/
│── data/                  # Raw and cleaned datasets
│── notebooks/             # EDA and analysis notebooks
│── sql_queries/           # SQL scripts for aggregation and analysis
│── dashboard/             # Streamlit app files
│── model/                 # ML models and pipeline files
│── README.md

Usage

Clone the repository.

Run the Streamlit dashboard:

streamlit run dashboard/app.py


Select year, store, and month to view weekly sales time-series plots.

Objective

Provide Walmart with a reproducible workflow to:

Analyze holiday and seasonal impacts on sales.

Forecast weekly sales at the store level.

Support data-driven retail decisions using ML predictions and visualizations.
