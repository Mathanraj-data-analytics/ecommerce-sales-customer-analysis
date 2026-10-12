
import pandas as pd
import mysql.connector
from pathlib import Path

# Project CSV file
csv_path = Path(
    r"D:\Data Analyst Project\data\cleaned\online_retail_cleaned.csv"
)

# MySQL connection settings
# Enter your own MySQL password below
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="ecommerce_analysis"
)

cursor = conn.cursor()

# Read CSV in batches
batch_size = 5000
total_imported = 0

try:
    for chunk in pd.read_csv(
        csv_path,
        chunksize=batch_size,
        dtype={"CustomerID": "string"},
        keep_default_na=True
    ):
        # Convert missing values to SQL NULL
        chunk = chunk.astype(object).where(
            pd.notna(chunk), None
        )

        rows = [
            tuple(row)
            for row in chunk.itertuples(index=False, name=None)
        ]

        sql = """
        INSERT INTO online_retail
        (InvoiceNo, StockCode, Description, Quantity,
         InvoiceDate, UnitPrice, CustomerID, Country, Revenue)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.executemany(sql, rows)
        conn.commit()

        total_imported += len(rows)
        print(f"Imported: {total_imported:,} rows")

    print("Import completed successfully!")

except Exception as error:
    conn.rollback()
    print("Import failed:", error)

finally:
    cursor.close()
    conn.close()
