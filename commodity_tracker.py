import os
import pandas as pd
import matplotlib.pyplot as plt

# 1. Initialize the raw tracking dataset
raw_data = [
    {"Asset": "Hindustan Copper", "Base_Price": 270.50, "Avg_Cost": 285.00},
    {"Asset": "NALCO", "Base_Price": 190.25, "Avg_Cost": 180.10},
    {"Asset": "Vedanta", "Base_Price": 440.80, "Avg_Cost": 420.50}
]

# 2. Convert raw data into a structured Pandas DataFrame
df = pd.DataFrame(raw_data)

# 3. Data Engineering: Calculate a 5% lower entry limit buffer target
df['Target_Price'] = (df['Base_Price'] * 0.95).round(2)

print("--- Data Pipeline Engine Initialized ---")
print(df)

# 4. Initialize Matplotlib Figure and Axis positions
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
positions = range(len(df))
bar_width = 0.35

# Plot Side-by-Side Grouped Bars
bars_base = ax.bar([p - bar_width/2 for p in positions], df['Base_Price'], width=bar_width, label='Active Market Base Price', color='#1f77b4')
bars_target = ax.bar([p + bar_width/2 for p in positions], df['Target_Price'], width=bar_width, label='5% Entry Buffer Target', color='#2ca02c')

# Styling and Labels
ax.set_title('Indian Metal Commodities: Active Base vs. Target Entry Price', fontsize=14, fontweight='bold', pad=15)
ax.set_ylabel('Price in INR (₹)', fontsize=12)
ax.set_xticks(positions)
ax.set_xticklabels(df['Asset'], fontsize=11)
ax.legend(loc='upper right')
ax.grid(axis='y', linestyle='--', alpha=0.5)

# Value Labels
for bar in bars_base + bars_target:
    height = bar.get_height()
    ax.annotate(f'₹{height:.2f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9)

plt.tight_layout()

# 5. Export the chart to your actual OneDrive Desktop folder
# This automatically handles the OneDrive path directory structure
desktop_path = os.path.join(os.environ['USERPROFILE'], 'OneDrive', 'Desktop')
output_filename = os.path.join(desktop_path, 'commodity_trend_tracker.png')

# If OneDrive isn't setup exactly this way, fall back to the current directory
if not os.path.exists(desktop_path):
    output_filename = 'commodity_trend_tracker.png'

plt.savefig(output_filename, dpi=300, bbox_inches='tight')
plt.close()

print(f"\n[Success] Portfolio visualization exported successfully!")
print(f"Artifact Location: {os.path.abspath(output_filename)}")