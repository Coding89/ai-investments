"""
AI Investments Data Pipeline

This script automates the process of loading AI financial market datasets from local CSV files.
The open source data is obtained from Kaggle. It stages and cleans the column schemas and streams
the processed data directly into a local and permanent SQlite database file.

Additionally, the script alo includes verification layers that connect to the final database, executes relational SQL queries
and automates summary statistics.

Note that data from Kaggle is not always accurate, so please keep an eye out on the schema validation if it breaks + how accurate is this data?

Dependencies: pandas, sqlalchemy

"""
import sys
import pandas as pd
from sqlalchemy import create_engine

#Loads the CSV but bails out if it's missing
try:
    df = pd.read_csv('ai_financial_market_data.csv')
except FileNotFoundError:
    print("Missing ai_financial_market_data.csv", file=sys.stderr)
    sys.exit(1)

# Maps raw schema to standardise naming
#TODO: move this to a config file if we have more datasets in the future
df.columns = [
    'date', 'company', 'rd_spending_usd_mn', 'ai_revenue_usd_mn', 'ai_revenue_growth_pct', 'event', 'stock_impact_pct'
]
df['date'] = pd.to_datetime(df['date'], errors='coerce')

if len(df) == 0:
    print("Warning: The Dataframe is empty! Check the .csv file")

engine = create_engine('sqlite:///ai_investments.db')
df.to_sql('ai_financial_data', con=engine, if_exists='replace', index=False)

# Quick Check
print(pd.read_sql("SELECT * FROM ai_financial_data LIMIT 5;", engine))

