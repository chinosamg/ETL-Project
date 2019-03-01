-- Table All Elements
SELECT * FROM fortune500

-- Average Profit Average_Profit

SELECT AVG(Profits) AS Average_Profit FROM fortune500;

-- Average Profit Average_Revenue

SELECT AVG(Revenues) AS Average_Revenue FROM fortune500;

-- Profits Greater Than Average
SELECT * FROM fortune500
WHERE Profits > (SELECT AVG(Profits) FROM fortune500);

-- Profits Less Than Average
SELECT * FROM fortune500
WHERE Profits < (SELECT AVG(Profits) FROM fortune500);

-- Revenue Greater Than Average
SELECT * FROM fortune500
WHERE Revenues > (SELECT AVG(Revenues) FROM fortune500);

-- Revenue Less Than Average
SELECT * FROM fortune500
WHERE Revenues < (SELECT AVG(Revenues) FROM fortune500);

-- Lowest Profit Top500
SELECT MIN(Profits) As LowestProfit
FROM fortune500;

-- Highest Profit Top500
SELECT MAX(Profits) As HighestProfit
FROM fortune500;

-- Lowest Profit Top500
SELECT MIN(Revenues) As LowestRevenues
FROM fortune500;

-- Highest Profit Top500
SELECT MAX(Revenues) As HighestRevenues
FROM fortune500;

-- Top10 Companies
SELECT Rank, Company, Ticker, Revenues, Profits
FROM fortune500
GROUP BY Company
HAVING Rank < 11
ORDER BY Rank asc;

-- Top50 Companies
SELECT Rank, Company, Ticker, Revenues, Profits
FROM fortune500
GROUP BY Company
HAVING Rank < 51
ORDER BY Rank asc;

