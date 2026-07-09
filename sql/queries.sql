-- Total number of users

SELECT COUNT(*) AS TotalUsers
FROM conversion_data;
-- Number of users in each group

SELECT Group,
       COUNT(*) AS TotalUsers
FROM conversion_data
GROUP BY Group;
-- Total conversions in each group

SELECT Group,
       SUM(Converted) AS TotalConversions
FROM conversion_data
GROUP BY Group;
-- Conversion rate for each group

SELECT Group,
       ROUND(AVG(Converted) * 100, 2) AS ConversionRate
FROM conversion_data
GROUP BY Group;
-- Number of users who did not convert

SELECT Group,
       COUNT(*) - SUM(Converted) AS NonConversions
FROM conversion_data
GROUP BY Group;
-- Overall conversion rate

SELECT ROUND(AVG(Converted) * 100, 2) AS OverallConversionRate
FROM conversion_data;