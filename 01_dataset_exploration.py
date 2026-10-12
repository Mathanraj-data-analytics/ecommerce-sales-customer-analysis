import pandas as pd
from pathlib import Path

# Project folder location
project_folder = Path(__file__).resolve().parent.parent

# Dataset location
file_path = project_folder / "data" / "raw" / "Online Retail.xlsx"

# Load Excel dataset
df = pd.read_excel(file_path)

# Display basic information
print("\n--- FIRST 5 ROWS ---")
print(df.head())

print("\n--- DATASET SHAPE ---")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- DUPLICATE ROWS ---")
print(df.duplicated().sum())
# Investigate missing descriptions
print("\n--- MISSING DESCRIPTION EXAMPLES ---")
print(df[df["Description"].isnull()].head(10))

# Investigate missing customer IDs
print("\n--- MISSING CUSTOMER ID EXAMPLES ---")
print(df[df["CustomerID"].isnull()].head(10))

# Investigate duplicate rows
print("\n--- DUPLICATE ROW EXAMPLES ---")
print(df[df.duplicated(keep=False)].head(10))

# Check quantity statistics
print("\n--- QUANTITY STATISTICS ---")
print(df["Quantity"].describe())

# Check unit price statistics
print("\n--- UNIT PRICE STATISTICS ---")
print(df["UnitPrice"].describe())

# Check invoice numbers starting with C
print("\n--- CANCELLED INVOICE EXAMPLES ---")
print(df[df["InvoiceNo"].astype(str).str.startswith("C")].head(10))