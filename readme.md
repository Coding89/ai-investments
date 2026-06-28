# AI Investments Data Pipleline

## An automated Python data pipeline that ingests, cleans and stores open source data (from Kaggle) surrounding AI financial market datasets pertaining to Meta Platforms, Inc (Facebook), Alphabet Inc. (Google), and OpenAI from 2015 to 2014. The primary focus is on R&D and stock market YoY analysis using visuals like PowerBI, Matplotlib and Seaborn.
------
### Built With: ###

- ![python](https://img.shields.io/badge/Python-3.9-3776AB.svg?style=flat&logo=python&logoColor=white)
- ![pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)
- ![Matplotlib](https://img.shields.io/badge/-Matplotlib-000000?style=flat&logo=python)
- ![Power BI](https://img.shields.io/badge/Power_Bi-F2C811?style=flat-square&logo=codeforces&logoColor=black)
- ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-306998?logo=python&logoColor=white)
- ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=SQLite&logoColor=white)
- ![Seaborn](https://img.shields.io/badge/-Seaborn-3776AB?style=flat&logo=python&logoColor=white&size=40x40)
-------

### Overview: ###

This project provides a focused analysis of AI investment spending across three major technology companies: Meta Platforms, Inc (Facebook), Alphabet Inc. (Google) and OpenAI over a 10 year period from January 2015 to Dcember 2024.
The analysis specifically examines R&D spending on AI projects, AI revenue generation and quaterly spending trends to understand how these industry leaders are investing in AI.
-------

### Analysis Scope ### 

Companies Analysed:

| Company  | Ticker | Industry | Focus Area |
| ------------- | ------------- | -------------| -------------|
| Meta Platforms, Inc.  | META  | Social Media/Tech | AI, Metaverse, Social Platforms |
| Alphabet Inc.  | GOOGL  | Technology | AI, Search, Cloud Computing |
| OPEN AI  | N/A  | AI Research | AI Models, Research, LLMs |

--------

  ## Time Period ##

- **Start Date**: 1 January 2015
- **End Date**: 31 December 2024
- **Duration**: 10 years


---------

## Dataset Contents ##

The CSV file (ai_financial_market_data.csv) contains 10,960 lines of AI specific financial data including:

- **Date**: Timeline from 2015 to 2024
- **Company**: Meta (FaceBook), Google and OpenAI
- **R&D_Spending_USD_Mn**: Research &Development spending in millions (USD)
- **AI_Revenue_US_Mn**: AI generated revenue in the millions (USD)
- **AI_Revenue_Growth%**: Percentage growth of AI Revenue
- **Event** - Significant AI related events like "AI Ethics Policy Update"
- **Stock_Impact_%**: Stock price impact percentage

---------

## How to run ##

**Prerequisites**:

- Python 3.8 or newer
- pip package manager
- Power BI Desktop
- Git

**Installation**:

1) Clone the repository:

   git clone https://github.com
   cd ai-investments

2) Set up Python virtual environment:

 python -m venv venv
 source venv/bin/activate

3) Install required package:

  pip intall -r requirements.txt

4) Download the dataset

5) Run the scripts

The ai_investments.py script processes the raw CSV data and creates a SQLite database:

#Activates the virtual environment
source vev/bin/activate

#Runs the data processing script
python ai_investments.py

**Results**:

1) Loads the CSV data.
2) Cleans and prepares the data.
3) Creates an "ai_investments.db" SQLite database.
4) Generates processed tables for analysis.
--------

**PowerBI Dashboards**

The powerbi-visuals/ directory contains interactive PowerBI reports focused on AI investment analysis:

1) **Total Spending by Year and Year** - Aggregate AI investment across all companies (2015 - 2024).
2) **Total Spend per Company** - Individual company breakdown of AI R&D expenditures.
3) **Side by Side Spending** - Direct comparison of spending patterns across Meta, Alphabet and OpenAI.
4) **Quarterly Spending** - Time-series analysis of AI project investments by quarter.

**Matplotlib Visuals**

1) **Graph 1: AI R&D Spending Trend (Line Chart)**: Tracks the annual acceleration and velocity of coporate AI budgets by mapping individual company R&D expenditures from 2015 to 2024.
2) **Graph 2: Annual AI Revenue Comparison (Grouped Bar Chart)**: Compares the financial market performance by clustering individual coporate AI revenues side by side for each year.
3) **Graph 3: Revenue Growth versus Stock Impact (Scatter Plot)**: Analyses market announcements and economic correlation by mapping annual AI revenue growth rates directly against their resulting stock price percentage changes.

---------
## Additional Information: ##

Source:

- **Dataset Name**: AI Financial and Market Data
- **Provider**: Kaggle
- **Author**: Rohit Grewal
- **License**: Open Source
- The open source data can be obtained from: https://www.kaggle.com/code/rohitgrewal/ai-financial-market-data-analysis (relevant as of 20th June 2026).
---------
## Disclaimer: ##

1) No private details or data are shown.
2) The open source data is from Kaggle and its reliability/accuracy must always be questioned.
3) This project is only for personal use.
4) This repository is for educational and personal project purposes only. The data, visualisations and analyses presented here do not constitute financial, investment or legal advice. The stock market data and financial metrics may be simulated, aggregated or delayed. No investment decisions should be made based on the contents of this project.
