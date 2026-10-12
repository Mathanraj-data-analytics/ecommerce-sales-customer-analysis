
USE ecommerce_analysis;

-- 1. Top 10 products by revenue
SELECT
    StockCode,
    MAX(Description) AS product_name,
    SUM(Quantity) AS total_quantity_sold,
    ROUND(SUM(Revenue), 2) AS total_revenue
FROM online_retail
GROUP BY StockCode
ORDER BY total_revenue DESC
LIMIT 10;


-- 2. Top 10 products by quantity sold
SELECT
    StockCode,
    MAX(Description) AS product_name,
    SUM(Quantity) AS total_quantity_sold,
    ROUND(SUM(Revenue), 2) AS total_revenue
FROM online_retail
GROUP BY StockCode
ORDER BY total_quantity_sold DESC
LIMIT 10;


-- 3. Product performance summary
SELECT
    COUNT(DISTINCT StockCode) AS unique_products,
    ROUND(SUM(Quantity), 0) AS total_quantity_sold,
    ROUND(SUM(Revenue), 2) AS total_revenue
FROM online_retail;
