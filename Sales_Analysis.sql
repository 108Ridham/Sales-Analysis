-- Top 5 products by total sales
SELECT Product_line, SUM(Sales) AS TotalSales 
FROM Sales 
GROUP BY Product_line 
ORDER BY TotalSales DESC 
LIMIT 5;

-- City with the highest revenue
SELECT City, SUM(Sales) AS Revenue 
FROM Sales 
GROUP BY City 
ORDER BY Revenue DESC 
LIMIT 1;

-- Average rating by gender
SELECT Gender, AVG(Rating) AS AverageRating 
FROM Sales 
GROUP BY Gender;

-- Most popular payment method
SELECT Payment, COUNT(*) AS Count 
FROM Sales 
GROUP BY Payment 
ORDER BY Count DESC 
LIMIT 1;

-- Monthly revenue trend (using SUBSTR on DD-MM-YYYY)
SELECT SUBSTR(Date, 4, 2) AS Month, SUM(Sales) AS MonthlyRevenue 
FROM Sales 
GROUP BY Month 
ORDER BY Month;

-- Branch-wise performance – Sales and customer count per branch
SELECT Branch, COUNT(Invoice_ID) AS CustomerCount, SUM(Sales) AS TotalSales 
FROM Sales 
GROUP BY Branch;

-- Who gives higher ratings on average – males or females
SELECT Gender, AVG(Rating) AS AverageRating 
FROM Sales 
GROUP BY Gender 
ORDER BY AverageRating DESC 
LIMIT 1;

-- Product line with the highest average unit price
SELECT Product_line, AVG(Unit_price) AS AvgUnitPrice 
FROM Sales 
GROUP BY Product_line 
ORDER BY AvgUnitPrice DESC 
LIMIT 1;

-- Peak sales hours (Time is in HH:MM format)
SELECT CAST(SUBSTR(Time, 1, INSTR(Time, ':') - 1) AS INTEGER) AS Hour, 
       SUM(Sales) AS TotalSales 
FROM Sales 
GROUP BY Hour 
ORDER BY TotalSales DESC;