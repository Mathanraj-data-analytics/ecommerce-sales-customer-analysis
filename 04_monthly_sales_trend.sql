USE ecommerce_analysis;

-- 1. Monthly revenue trend
SELECT
    DATE_FORMAT(InvoiceDate, '%Y-%m') AS sales_month,
    ROUND(SUM(Revenue), 2) AS monthly_revenue
FROM online_retail
GROUP BY DATE_FORMAT(InvoiceDate, '%Y-%m')
ORDER BY sales_month;


-- 2. Monthly quantity sold
SELECT
    DATE_FORMAT(InvoiceDate, '%Y-%m') AS sales_month,
    SUM(Quantity) AS total_quantity_sold
FROM online_retail
GROUP BY DATE_FORMAT(InvoiceDate, '%Y-%m')
ORDER BY sales_month;


-- 3. Monthly invoice count
SELECT
    DATE_FORMAT(InvoiceDate, '%Y-%m') AS sales_month,
    COUNT(DISTINCT InvoiceNo) AS total_invoices
FROM online_retail
GROUP BY DATE_FORMAT(InvoiceDate, '%Y-%m')
ORDER BY sales_month;