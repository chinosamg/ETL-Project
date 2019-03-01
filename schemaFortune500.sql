-- Create and use ETL_Project
CREATE DATABASE ETL_Project_Fortune500;
USE ETL_Project_Fortune500;

-- Create Tables
CREATE TABLE Fortune500 (
Rank INT PRIMARY KEY,
    Company TEXT,
    Ticker TEXT,
    Revenues INT,
    Profits INT);

CREATE TABLE Fortune100 (
Rank INT PRIMARY KEY,
    Company TEXT,
    Ticker TEXT,
    Revenues INT,
    Profits INT);

CREATE TABLE Fortune50 (
Rank INT PRIMARY KEY,
    Company TEXT,
    Ticker TEXT,
    Revenues INT,
    Profits INT);


