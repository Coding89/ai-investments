"""
AI Investments Data Pipeline
---------------------------
This script automates the process of loading AI financial market datasets from local CSV files.
The open source data is obtained from Kaggle. It stages and cleans the column schemas and streams
the processed data directly into a local and permamnent SQlite database file.

Additionally, the script alo includes verification layers that connect to the final databse, executes relational SQL queries
and automates summary statistics.

Script uses:
- pandas, sqlalchemy

"""
import pandas as pd
from sqlalchemy import create_engine, text

#Initialise SQLite Database Engine and creates a permanent SQLite Database file
engine = create_engine('sqlite:///ai_investments.db', echo=False)

#Loads CSV files
df_prices = pd.read_csv(r'C:\Users\Mamiko\Desktop\Github\ai-investments\ai_financial_market_data.csv')

df_companies = pd.read_csv(r'C:\Users\Mamiko\Desktop\Github\ai-investments\ai_financial_market_data.csv')

#cleans the data by converting data strings to datetime etc
df_prices.columns = [
    'date',
    'company',
    'rd_spending_usd_mn',
    'ai_revenue_usd_mn',
    'ai_revenue_growth_pct',
    'event',
    'stock_impact_pct'
]

#Streams Dataframe into SQL table
df_prices.to_sql(
    'ai_financial_data',
    con=engine,
    if_exists='replace',
    index=False
)

print("SQL Database successfully created. Table created called 'ai_financial_data'.")

#This queires and displays the results to verify they saved correctly
print("--- Fetching the first 10 rows from SQL ---")
with engine.connect() as connection:
    query = text("SELECT * FROM ai_financial_data LIMIT 10;")
    results = connection.execute(query)
    
    #formats and prints out each row
    for row in results:
        print(row)