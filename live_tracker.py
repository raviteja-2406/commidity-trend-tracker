import os
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

print("--- Initializing Real-Time Ingestion Pipeline ---")

# 1. Define portfolio config with official NSE symbols
portfolio_config = {
    "HINDCOPPER.NS": {"Asset": "Hindustan Copper", "Avg_Cost": 285.00},
    "NATIONALUM.NS": {"Asset": "NALCO", "Avg_Cost": 180.10},
    "VEDL.NS": {"Asset": "Vedanta", "Avg_Cost": 420.50}
}

tickers_list = list(portfolio_config.keys())

try:
    # 2. Fetch live market data from Yahoo Finance API
    print("Fetching live market data from NSE...")
    live_data = yf.download(tickers=tickers_list, period="1d", interval="1m", progress=False)
    
    processed_rows = []
    for ticker in tickers_list:
        last_price = live_data['Close'][ticker].dropna().iloc[-1]
        processed_rows.append({
            "Asset": portfolio_config[ticker]["Asset"],
            "Base_Price": round(float(last_price), 2),
            "Avg_Cost": portfolio_config[ticker]["Avg_Cost"]
        })
        
    # 3. Structural DataFrame & Data Engineering
    df = pd.DataFrame(processed_rows)
    df['Target_Price'] = (df['Base_Price'] * 0.95).round(2)
    
    print("\n--- Live Engineered Dataframe ---")
    print(df)
    
    # 4. Generate Visualization Matrix
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    positions = range(len(df))
    bar_width = 0.35
    
    bars_base = ax.bar([p - bar_width/2 for p in positions], df['Base_Price'], width=bar_width, label='Live Market Price', color='#1f77b4')
    bars_target = ax.bar([p + bar_width/2 for p in positions], df['Target_Price'], width=bar_width, label='5% Entry Target Buffer', color='#2ca02c')
    
    ax.set_title('Live Indian Metal Commodities Dashboard', fontsize=14, fontweight='bold', pad=15)
    ax.set_ylabel('Price in INR (₹)', fontsize=12)
    ax.set_xticks(positions)
    ax.set_xticklabels(df['Asset'], fontsize=11)
    ax.legend(loc='upper right')
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    
    for bar in bars_base + bars_target:
        height = bar.get_height()
        ax.annotate(f'₹{height:.2f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9)
                    
    plt.tight_layout()
    
    # 5. Export clean output back to your desktop
    desktop_path = os.path.join(os.environ['USERPROFILE'], 'OneDrive', 'Desktop')
    output_filename = os.path.join(desktop_path, 'live_commodity_dashboard.png')
    
    if not os.path.exists(desktop_path):
        output_filename = 'live_commodity_dashboard.png'
        
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\n[Success] Live portfolio visualization exported successfully!")
    print(f"Live Artifact: {os.path.abspath(output_filename)}")

except Exception as e:
    print(f"\n[Pipeline Error] Critical issue fetching live data: {e}")