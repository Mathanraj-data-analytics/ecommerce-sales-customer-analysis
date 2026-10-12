import pandas as pd
from pathlib import Path

# Project folder
project_folder = Path(__file__).resolve().parent.parent

# Input and output paths
input_file = project_folder / "data" / "raw" / "Online Retail.xlsx"

output_file = project_folder / "data" / "cleaned" / "online_retail_cleaned.csv"

# Load original dataset
df = pd.read_excel(input_file)

print("Original dataset shape:", df.shape)

# 1. Remove exact duplicate rows
df = df.drop_duplicates()

print("After removing duplicates:", df.shape)

# 2. Remove rows with missing product descriptions
df = df.dropna(subset=["Description"])

print("After removing missing descriptions:", df.shape)

# 3. Identify cancelled invoices
df["InvoiceNo"] = df["InvoiceNo"].astype(str)

cancelled_mask = df["InvoiceNo"].str.startswith("C")

print("Cancelled invoice rows:", cancelled_mask.sum())

# 4. Keep non-cancelled transactions
df = df[~cancelled_mask].copy()

print("After excluding cancelled invoices:", df.shape)

# 5. Keep positive quantities and prices for sales analysis
df = df[
    (df["Quantity"] > 0) &
    (df["UnitPrice"] > 0)
].copy()

print("After quantity and price filtering:", df.shape)

# 6. Create revenue column
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# 7. Save cleaned dataset
df.to_csv(output_file, index=False)

print("\nCleaned dataset saved successfully!")
print("Output file:", output_file)

print("\nFinal dataset shape:", df.shape)

print("\nRemaining missing values:")
print(df.isnull().sum())