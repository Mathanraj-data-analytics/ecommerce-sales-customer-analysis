
USE ecommerce_analysis;

-- 1. Revenue by country
SELECT
    Country,
    ROUND(SUM(Revenue), 2) AS total_revenue
FROM online_retail
GROUP BY Country
ORDER BY total_revenue DESC;

-- 2. Top 10 countries by revenue
SELECT
    Country,
    ROUND(SUM(Revenue), 2) AS total_revenue
FROM online_retail
GROUP BY Country
ORDER BY total_revenue DESC
LIMIT 10;

-- 3. Country revenue contribution percentage
SELECT
    Country,
    ROUND(SUM(Revenue), 2) AS total_revenue,
    ROUND(
        SUM(Revenue) * 100 /
        (SELECT SUM(Revenue) FROM online_retail),
        2
    ) AS revenue_percentage
FROM online_retail
GROUP BY Country
ORDER BY total_revenue DESC
LIMIT 10;
