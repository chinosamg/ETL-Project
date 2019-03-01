-- Create and use ETL_Project
CREATE DATABASE ETL_Project;
USE ETL_Project;

-- Create Two Tables
CREATE TABLE inc2016 (
ID INT PRIMARY KEY,
    Company2016 TEXT,
    Revenue INT,
    Rank INT);

CREATE TABLE inc2018 (
ID INT PRIMARY KEY,
    Company2018 TEXT,
    Revenue INT,
    Rank INT);

CREATE TABLE combined (
ID INT PRIMARY KEY,
    Company2018 TEXT,
    Company2016 TEXT,
    Rank INT);
