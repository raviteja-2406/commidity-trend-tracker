import json
import urllib.request
import pandas as pd
import matplotlib.pyplot as plt

print("[STARTING] Launching dynamic real-time data engine...")

# 1. Fetch live cryptocurrency prices using a public API endpoint
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,ripple&vs_currencies=inr"

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        raw_data = json.loads(response.read().decode())
    
    # 2. Extract specific live numbers
    assets = ['Bitcoin', 'Ethereum', 'Ripple (XRP)']
    live_prices = [
        float(raw_data['bitcoin']['inr']),
        float(raw_data['ethereum']['inr']),
        float(raw_data['ripple']['inr'])
    ]
    
    # 3. Process data into a clean structure
    df = pd.DataFrame({'Asset': assets, 'Live_Price_INR': live_prices})
    df['Target_Entry_Limit'] = df['Live_Price_INR'] * 0.95
    
    print("\n--- Live Web-Scraped Analytics DataFrame ---")
    print(df)
    
    # 4. Generate the dynamic dashboard
    plt.figure(figsize=(10, 6))
    x_pos = range(len(df['Asset']))
    
    plt.bar([p - 0.2 for p in x_pos], df['Live_Price_INR'], width=0.4, label='Live Web Price (INR)', color='darkcyan')
    plt.bar([p + 0.2 for p in x_pos], df['Target_Entry_Limit'], width=0.4, label='95% Value Target Limit', color='gold')
    
    plt.xticks(x_pos, df['Asset'], fontsize=11)
    plt.title("Dynamic Real-Time Web Data Monitor Dashboard", fontsize=13, fontweight='bold', pad=15)
    plt.ylabel("Asset Value in INR (₹)", fontsize=12)
    plt.legend(loc='upper right')
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    
    # 5. Save the graphic report
    output_img = 'live_web_report.png'
    plt.savefig(output_img, dpi=300, bbox_inches='tight')
    print(f"\n[SUCCESS] Dynamic report exported as: '{output_img}'")
    
    plt.show()

except Exception as e:
    print(f"\n[NETWORK ERROR] Could not pull live network data: {e}")