def clean_data(df):
    if df.empty:
        print("No transactions found from PDF")
        return df

    df = df[df["Expense"] > 0]
    return df
