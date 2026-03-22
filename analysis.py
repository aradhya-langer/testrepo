import pandas as pd
from smart_category import final_category   # this uses rules + memory + ML

# load extracted expenses
df = pd.read_csv("expenses.csv")

# apply smart categorization
df["Category"] = df["Description"].apply(final_category)

# show category totals
print("\nCategory totals:\n")
print(df.groupby("Category")["Expense"].sum())

# save final file
df.to_csv("final.csv", index=False)
print("\nfinal.csv created")
