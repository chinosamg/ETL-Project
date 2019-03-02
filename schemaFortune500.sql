-- Create and use ETL_Project
CREATE DATABASE ETL_Project_Fortune500;
USE ETL_Project_Fortune500;

-- Create Tables
CREATE TABLE Fortune500_2017 (
Rank INT PRIMARY KEY,
    Company TEXT,
    Ticker TEXT,
    Revenues INT);

CREATE TABLE Fortune500_2016 (
Rank INT PRIMARY KEY,
    Company TEXT,
    Ticker TEXT,
    Revenues INT);




