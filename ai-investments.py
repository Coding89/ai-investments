import pandas as pd
from sqlalchemy import create_engine

#Initialise SQLite Database Engine
engine = create_engine('sqlite:///:memory:', echo=False)

#Loads CSV files
df_prices = pd.read_csv('ai_financial_market_data.csv')

df_companies = pd.read_csv('ai_financial_market_data.csv')

#cleans the data by converting data strings to datetime etc
df_prices.column = [
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