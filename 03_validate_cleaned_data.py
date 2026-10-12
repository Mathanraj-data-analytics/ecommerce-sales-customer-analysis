import pandas as pd
from pathlib import Path

# Project folder
project_folder = Path(__file__).resolve().parent.parent

# Cleaned dataset path
file_path = (
    project_folder
    / "data"
    / "cleaned"
    / "online_retail_cleaned.csv"
)

# Load cleaned dataset
df = pd.read_csv(file_path)

print("--- CLEANED DATA VALIDATION ---")

# 1. Dataset size
print("\nDataset shape:")
print(df.shape)

# 2. Check duplicate rows
print("\nDuplicate rows:")
print(df.duplicated().sum())

# 3. Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# 4. Check invalid quantities
print("\nQuantity <= 0:")
print((df["Quantity"] <= 0).sum())

# 5. Check invalid prices
print("\nUnitPrice <= 0:")
print((df["UnitPrice"] <= 0).sum())

# 6. Check cancelled invoices
print("\nCancelled invoice rows:")
print(
    df["InvoiceNo"]
    .astype(str)
    .str.startswith("C")
    .sum()
)

# 7. Verify revenue calculation
expected_revenue = df["Quantity"] * df["UnitPrice"]

print("\nRevenue calculation correct:")
print(
    (df["Revenue"] - expected_revenue)
    .abs()
    .lt(0.000001)
    .all()
)

print("\nValidation completed!")