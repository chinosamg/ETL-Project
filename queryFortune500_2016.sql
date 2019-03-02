-- Table All Elements

SELECT * FROM fortune500_2016

-- Lowest Revenue Top500 2016

SELECT MIN(Revenues) As LowestRevenues
FROM fortune500_2016;

-- Highest Revenue Top500 2016

SELECT MAX(Revenues) As HighestRevenues
FROM fortune500_2016;

-- Top10 Companies 2016

SELECT Rank, Company, Ticker, Revenues
FROM fortune500_2016
GROUP BY Company
HAVING Rank < 11
ORDER BY Rank asc;

-- Top50 Companies 2016

SELECT Rank, Company, Ticker, Revenues
FROM fortune500_2016
GROUP BY Company
HAVING Rank < 51
ORDER BY Rank asc;

