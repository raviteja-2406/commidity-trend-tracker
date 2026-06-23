import pandas as pd
import matplotlib.pyplot as plt

# 1. Load corporate transactions
transactions = {
    'Transaction_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109],
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Home Decor', 'Clothing', 'Home Decor', 'Electronics', 'Clothing', 'Home Decor'],
    'Revenue_INR': [25000, 1200, 45000, 8500, 3500, 1500, 12000, 5800, 9500],
    'Profit_Margin': [0.15, 0.40, 0.12, 0.25, 0.35, 0.20, 0.18, 0.38, 0.22]
}

df = pd.DataFrame(transactions)

# 2. Calculate net profit metrics
df['Net_Profit_INR'] = df['Revenue_INR'] * df['Profit_Margin']
summary = df.groupby('Category')[['Revenue_INR', 'Net_Profit_INR']].sum().reset_index()

print("--- Corporate Summary Table ---")
print(summary)

# 3. Plot Horizontal Layout Dashboard
plt.figure(figsize=(10, 5))
y = range(len(summary['Category']))

plt.barh([p - 0.2 for p in y], summary['Revenue_INR'], height=0.4, label='Gross Revenue', color='royalblue')
plt.barh([p + 0.2 for p in y], summary['Net_Profit_INR'], height=0.4, label='Net Profit', color='mediumseagreen')

plt.yticks(y, summary['Category'])
plt.title('E-Commerce Revenue Dashboard', fontsize=14, fontweight='bold')
plt.xlabel('Value in INR (₹)')
plt.legend()
plt.grid(axis='x', linestyle=':', alpha=0.6)

# 4. Save and Show
plt.savefig('corporate_retail_report.png', dpi=300, bbox_inches='tight')
plt.show()