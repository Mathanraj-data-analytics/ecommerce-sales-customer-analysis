USE ecommerce_analysis;

-- 1. Check total records
SELECT COUNT(*) AS total_rows
FROM online_retail;

-- 2. Total sales revenue
SELECT
    ROUND(SUM(Revenue), 2) AS total_revenue
FROM online_retail;

-- 3. Total invoices and identified customers
SELECT
    COUNT(DISTINCT InvoiceNo) AS total_invoices,
    COUNT(DISTINCT CustomerID) AS identified_customers
FROM online_retail;
