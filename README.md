# README

Credit to the [Data Science Working Group](http://datascience.codeforsanfrancisco.org) for this template. To complete this project, delete all template text (save for the headers) and fill in your own information.

Begin reading `instructions.md` to get started.

## Project Intro/Objective
The purpose of this project is to engineer a Python-based data pipeline for analyzing stock data. The pipeline will be used to restructure large volumes of stock data, which will then be integrated with daily news headline data to measure how reliably sentiment predicts stock prices. This project is being undertaken by the data engineering team at Banking Objects of Portugal (BOofP), a national Portuguese consumer bank (not real, only for the sake of this project.)

### Methods Used
* Inferential Statistics
* Mathematics
* Object-Oriented Programming (OOP)
* Data Processing
* Statistical Analysis

### Technologies
* Python
* NumPy
* Pandas
* Statistics Module
* Datetime
* Jupyter Notebook

## Project Description
This project involves the development of a data engineering pipeline in Python to analyze stock data. The project is divided into three main parts:
1. Finding the Average
  In this part, the task is to compute the average of stock prices from a given list of lists data. The data is initially in the form of strings, and there may be missing data points that need to be accounted for. The average is calculated by iterating over each row of the data, creating a new list of valid numerical stock prices, and computing the average for each row. The result is rounded to the nearest third decimal place.
2. Finding the Median
  Similarly to Part 1, this part focuses on computing the median of each row of the data. The process involves converting strings to numbers, skipping empty values, and using the median function from the statistics module to calculate the median value. The median is not rounded, and the result is stored for each row in the data.
3. Finding the Sample Standard Deviation
  In the final part, the goal is to compute the sample standard deviation for each row of data. The process is similar to Part 2 but involves using the stddev function from the statistics module to calculate the sample standard deviation value. The result is rounded to the nearest third decimal place.

Finally, this project will enable the machine learning team to integrate sentiment analysis with stock data to make predictions about stock prices. The pipeline is designed to handle large volumes of data efficiently.
