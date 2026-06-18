import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loads the ai_financial_market_data.csv file
df = pd.read_csv('ai_financial_market_data.csv')

#Converts date strings from dd/mm/yyyy and pulls out the year
df = df.dropna(subset=['Year'])
df['Year'] = df['Year'].astype(int)

yearly_spending = df.groupby(['Year', 'Company'])['R&D_spending_USD_Mn'].sum().reset_index()

# Generates a multo year trend line visualisation
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