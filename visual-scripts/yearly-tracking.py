"""
Summary:

This scripts takes the raw 'ai_financial_market_data.csv' file, cleans it up (especially date formatting), 
and builds three core charts to tell a story about how companies are handling the AI boom:

1)R&D Spending Trend (Line plot): 
    Tracks who is pumping the most money into AI R&D.
    
2) Annual AI Revenue Comparison: 
    Compares their actual year to year AI revenues side by side.
    
3) Revenue Growth versus Stock Impact (Scatter Plot): 
    Charts the revenue growth directly against stock market
    movement to see if the AI hype actually translates to higher share prices.
    
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# makes the whitegrid look cleaner
plt.rcParams['figure.figsize'] = [10, 5.5]
sns.set_style("whitegrid")

# Loads the file and hope the encoding is fine
df = pd.read_csv('ai_financial_market_data.csv')

# Cleans up the column names - usually the data is messed up in the source file
df.columns = df.columns.str.strip()

#Date parsing and assumes UK format (dd/mm/yyyy) and removes any rows missing years
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y', errors='coerce')
df['Year'] = df['Date'].dt.year
df = df.dropna(subset=['Year'])
df['Year'] = df['Year'].astype('int')


#The beginning of the pretty visualisations 1: R&D Spending Trend (Line plot)

yearly_spending = df.groupby(['Year', 'Company'])['R&D_Spending_USD_Mn'].sum().reset_index()

# line plot shows the growth over time
plt.figure(figsize=(10, 5.5))
sns.lineplot(
    data=yearly_spending,
    x='Year',
    y='R&D_Spending_USD_Mn',
    hue='Company',
    marker='o',
    linewidth=2.5
)

#Formats the layout and scale markers
plt.title('Annual AI Investment Growth Tracker (R&D Spend Over the Years)',  fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Total Annual R&D Spend (USD Millions)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)

#Ensures that the X-Axis matches the exact calendar years instead of decimals
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(integer=True))
plt.tight_layout()

plt.show()

#Visualisation 2: Annual AI Revenue Comparison

#Aggregates AI revenue by year and company
yearly_revenue = df.groupby(['Year', 'Company'])['AI_Revenue_USD_Mn'].sum().reset_index()

#bar chart for clarity
plt.figure(figsize=(10, 5.5))
sns.barplot(
    data=yearly_revenue, x='Year', y='AI_Revenue_USD_Mn',
    hue='Company', palette='muted')
plt.title('Annual AI Revenue Performance by Company', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Total AI Revenue (USD Millions)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

#Visualisation 3: Revenue Growth versus Stock Impact (Scatter Plot)
yearly_market_impact = df.groupby(['Year', 'Company'])[[
    'AI_Revenue_Growth_%',
    'Stock_Impact_%'
]].mean().reset_index()

plt.figure(figsize=(10, 5.5))

#plots scatterplot and added a cleaner look as data looked all compressed
sns.scatterplot(
    data=yearly_market_impact, 
    x='AI_Revenue_Growth_%',
    y='Stock_Impact_%',
    hue='Company',
    style='Company',
    s=100, 
    palette='deep'
)

#Zero lines for reference
plt.axhline(0, color='blue', linestyle='--', alpha=0.5)
plt.axvline(0, color='blue', linestyle='--', alpha=0.5)

plt.title('AI Revenue Growth % versus Market Stock Impact %', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('AI Revenue Growth (%)', fontsize=12)
plt.ylabel('Stock Impact (%)', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()
