import os
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

print("--- Initializing Live Portfolio Analytics Engine ---")

# Disables local cache database to prevent lock errors


# 1. Configuration Map (Adding hypothetical quantities held for real risk math)
portfolio_config = {
    "HINDCOPPER.NS": {"Asset": "Hindustan Copper", "Avg_Cost": 285.00, "Quantity": 100},
    "NATIONALUM.NS": {"Asset": "NALCO", "Avg_Cost": 180.10, "Quantity": 250},
    "VEDL.NS": {"Asset": "Vedanta", "Avg_Cost": 420.50, "Quantity": 50}
}

tickers_list = list(portfolio_config.keys())

try:
    print("Scraping live NSE tickers...")
    live_data = yf.download(tickers=tickers_list, period="1d", interval="1m", progress=False)
    
    processed_rows = []
    for ticker in tickers_list:
        last_price = live_data['Close'][ticker].dropna().iloc[-1]
        cfg = portfolio_config[ticker]
        
        processed_rows.append({
            "Asset": cfg["Asset"],
            "Qty": cfg["Quantity"],
            "Avg_Cost": cfg["Avg_Cost"],
            "Live_Price": round(float(last_price), 2)
        })
        
    # 2. Convert to DataFrame
    df = pd.DataFrame(processed_rows)
    
    # 3. ADVANCED DATA ENGINEERING: Risk & Return Matrix Formulas
    # P&L = (Live Price - Average Cost) * Quantity
    df['PnL_INR'] = ((df['Live_Price'] - df['Avg_Cost']) * df['Qty']).round(2)
    # Return % = ((Live Price - Average Cost) / Average Cost) * 100
    df['Return_Pct'] = (((df['Live_Price'] - df['Avg_Cost']) / df['Avg_Cost']) * 100).round(2)
    
    print("\n--- Live Analytics Risk Sheet ---")
    print(df[['Asset', 'Qty', 'Avg_Cost', 'Live_Price', 'PnL_INR', 'Return_Pct']])
    
    # 4. VISUALIZATION: Creating a dedicated P&L Portfolio Performance Bar Chart
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    
    # Dynamic coloring: Green for Profit, Red for Loss
    colors = ['#2ca02c' if x >= 0 else '#d62728' for x in df['PnL_INR']]
    
    bars = ax.bar(df['Asset'], df['PnL_INR'], color=colors, edgecolor='black', width=0.5)
    
    # Chart Adjustments
    ax.set_title('Real-Time Portfolio Profit / Loss (P&L) Analytics', fontsize=14, fontweight='bold', pad=15)
    ax.set_ylabel('Total P&L in INR (₹)', fontsize=12)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    ax.axhline(0, color='black', linewidth=1.2, linestyle='-') # Base reference zero line
    
    # Value labels with custom coloring and formatting
    for bar in bars:
        height = bar.get_height()
        label_color = '#1e7b1e' if height >= 0 else '#b31c1c'
        prefix = '+' if height >= 0 else ''
        ax.annotate(f'{prefix}₹{height:.2f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3 if height >= 0 else -12), 
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, fontweight='bold', color=label_color)

    plt.tight_layout()
    
    # 5. Export Output to Desktop
    desktop_path = os.path.join(os.environ['USERPROFILE'], 'OneDrive', 'Desktop')
    output_filename = os.path.join(desktop_path, 'live_pnl_analytics.png')
    
    if not os.path.exists(desktop_path):
        output_filename = 'live_pnl_analytics.png'
        
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\n[Success] Risk analysis report compiled!")
    print(f"Analytics Chart Location: {os.path.abspath(output_filename)}")

except Exception as e:
    print(f"\n[Pipeline Analytics Error]: {e}")