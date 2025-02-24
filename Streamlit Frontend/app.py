import streamlit as st
import pandas as pd
import pickle
import xgboost as xgb
import matplotlib.pyplot as plt
import seaborn as sns

# Load the trained model
@st.cache_resource
def load_model():
    with open("xgboost_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()

# Streamlit UI
st.title("🚀 Marketing Prediction & Insights")
st.write("Upload a CSV file to get predictions and graphical insights!")

# File Upload Section
uploaded_file = st.file_uploader("📂 Upload CSV File", type=["csv"])

if uploaded_file:
    # Read CSV
    df = pd.read_csv(uploaded_file)

    # Ensure correct columns
    expected_features = model.get_booster().feature_names
    missing_cols = set(expected_features) - set(df.columns)

    if missing_cols:
        st.error(f"❌ Missing columns: {missing_cols}")
    else:
        df = df[expected_features]

        # Make predictions
        predictions = model.predict(xgb.DMatrix(df))
        df["Predicted_Probability"] = predictions

        # Show predictions
        st.subheader("📌 Predictions")
        st.dataframe(df.head())

        # **1️⃣ Feature Importance**
        st.subheader("📊 Feature Importance")
        fig, ax = plt.subplots(figsize=(8, 6))
        xgb.plot_importance(model, ax=ax)
        st.pyplot(fig)

        # **2️⃣ Prediction Distribution**
        st.subheader("📈 Prediction Distribution")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.histplot(predictions, bins=20, kde=True, color="blue")
        plt.xlabel("Predicted Probability")
        plt.ylabel("Frequency")
        plt.title("Distribution of Predictions")
        st.pyplot(fig)

        # **3️⃣ Sales vs Profit Analysis**
        if "Sales" in df.columns and "Profit" in df.columns:
            st.subheader("📉 Sales vs Profit")
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.scatterplot(x=df["Sales"], y=df["Profit"], alpha=0.7)
            plt.xlabel("Sales")
            plt.ylabel("Profit")
            plt.title("Sales vs Profit Trend")
            st.pyplot(fig)

        # **4️⃣ Category-wise Performance**
        if "Category" in df.columns and "Profit" in df.columns:
            st.subheader("📊 Profit by Category")
            category_profit = df.groupby("Category")["Profit"].sum().reset_index()
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.barplot(x="Category", y="Profit", data=category_profit)
            plt.xlabel("Category")
            plt.ylabel("Total Profit")
            plt.title("Profit by Category")
            st.pyplot(fig)

        # **5️⃣ Monthly Trends**
        if "Order Month" in df.columns and "Sales" in df.columns:
            st.subheader("📅 Monthly Sales Trend")
            monthly_sales = df.groupby("Order Month")["Sales"].sum().reset_index()
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.lineplot(x="Order Month", y="Sales", data=monthly_sales, marker="o")
            plt.xlabel("Month")
            plt.ylabel("Total Sales")
            plt.title("Monthly Sales Trend")
            st.pyplot(fig)

        # **Download Predictions**
        st.download_button(
            label="📥 Download Predictions",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name="predictions.csv",
            mime="text/csv"
        )
