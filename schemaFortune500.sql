-- Create and use ETL_Project
CREATE DATABASE ETL_Project_Fortune500;
USE ETL_Project_Fortune500;

-- Create Two Tables
CREATE TABLE Fortune500 (
Rank INT PRIMARY KEY,
    Company TEXT,
    Ticker TEXT,
    Revenues INT,
    Profits INT);

