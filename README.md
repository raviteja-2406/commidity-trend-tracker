# Historical & Live Commodity Trend Analytics Pipeline

A 3-tier Python data science pipeline designed to track, engineer, and analyze portfolio risk parameters for major Indian metal commodities (*Hindustan Copper, NALCO, and Vedanta*) listed on the National Stock Exchange (NSE).

## 📊 Project Architecture Overview
The project is structured across three progressive stages to demonstrate core competencies in data ingestion, feature engineering, and high-resolution visualization:

1. *commodity_tracker.py (Static Blueprint):* Validates baseline structure by converting raw hardcoded matrix datasets into structured Pandas DataFrames and mapping them to Matplotlib visualization objects.
2. *live_tracker.py (Dynamic API Ingestion):* Replaces static variables with real-time data ingestion layers connecting directly to the Yahoo Finance API (yfinance) to scrape live NSE market ticks.
3. *analytics_tracker.py (Advanced Risk Engine):* Integrates advanced vectorized feature engineering to compute live Profit & Loss (P&L) margins and percentage return matrices, backed by conditional red/green visualization formatting.

---

## 🛠️ Tech Stack & Concepts Demonstrated
* *Language:* Python 3.14
* *Data Structuring & Engineering:* Pandas (DataFrames, Vectorized Row Math, Precision Rounding)
* *API Connectivity:* Yahoo Finance API (yfinance) for remote market ingestion
* *Data Visualization:* Matplotlib (Dual-metric grouped bar charts, conditional color mapping, annotation positioning)
* *Environment:* Windows Launcher (py), isolated project environments

---

## 📈 Pipeline Analytics & Features Under the Hood

### Feature Engineering Formulas Applied:
* *Target Lower Entry Limit Buffer:* Target Price = Base Price * 0.95
* *Absolute Position Profit/Loss (INR):* P&L = (Live Price - Average Cost) * Quantity
* *Percentage Return on Invested Capital:* Return % = ((Live Price - Average Cost) / Average Cost) * 100
*

---

## 🚀 How To Run the Project

Ensure you have your environment modules ready by launching your terminal and executing:
```cmd
pip install pandas matplotlib yfinance