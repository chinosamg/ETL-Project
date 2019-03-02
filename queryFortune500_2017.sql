-- Table All Elements

SELECT * FROM fortune500_2017

-- Lowest Revenue Top500 2017

SELECT MIN(Revenues) As LowestRevenues
FROM fortune500_2017;

-- Highest Revenue Top500 2017

SELECT MAX(Revenues) As HighestRevenues
FROM fortune500_2017;

-- Top10 Companies 2017

SELECT Rank, Company, Ticker, Revenues
FROM fortune500_2017
GROUP BY Company
HAVING Rank < 11
ORDER BY Rank asc;

-- Top50 Companies 2017

SELECT Rank, Company, Ticker, Revenues
FROM fortune500_2017
GROUP BY Company
HAVING Rank < 51
ORDER BY Rank asc;

