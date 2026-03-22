import streamlit as st
import pandas as pd
from parser import extract_transactions
from smart_category import final_category

st.title("📊 Smart Bank Expense Analyzer")

uploaded = st.file_uploader("Upload bank statement PDF", type="pdf")

if uploaded:

    # save uploaded file
    with open("temp.pdf", "wb") as f:
        f.write(uploaded.read())

    # extract expenses
    df = extract_transactions("temp.pdf")

    if df.empty:
        st.error("No transactions found")
    else:
        df["Category"] = df["Description"].apply(final_category)

        total = df["Expense"].sum()
        st.metric("Total Spent", f"₹ {total:.2f}")

        st.subheader("Category breakdown")
        cat = df.groupby("Category")["Expense"].sum()
        st.bar_chart(cat)

        st.subheader("Transactions")
        st.dataframe(df)
