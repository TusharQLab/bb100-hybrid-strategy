# BB100 Reversion + EMA Breakout Hybrid Strategy

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Status](https://img.shields.io/badge/Status-Research-orange)
![Market](https://img.shields.io/badge/Market-NSE%20India-green)

## Overview
A professional intraday quantitative trading research system for Indian F&O stocks.
Combines mean reversion and breakout strategies using Bollinger Bands (100 period)
with EMA confirmation and smart volume filters.

## Strategy Logic

### Strategy 1 — Mean Reversion
- Candle closes below BB Lower (touch)
- Next candle closes back inside BB (re-entry)
- Confirmation candle closes above EMA (momentum)
- Volume above SMA filter (participation)

### Strategy 2 — Filtered Breakout
- Price closes above BB Upper
- EMA 5 also above BB Upper (confirmation)
- Volume above SMA filter (participation)

### Conflict Resolution
- If both signals appear → Breakout wins if EMA 5 confirms
- Otherwise → Mean Reversion takes priority

## Key Findings
| Metric | Value |
|--------|-------|
| Universe | 10 Indian F&O stocks |
| Timeframe | 5-minute |
| Total Trades | 147 (filtered) |
| Win Rate | 25.85% |
| Beats Random | 7/8 stocks |
| Sensitivity | STABLE |
| Data Limitation | 55 days (yfinance limit) |

## Project Structure
```
bb100-hybrid-strategy/
├── data/
│   ├── cache/          ← cached OHLCV parquet files
│   └── processed/      ← feature engineered data
├── src/
│   ├── indicators/     ← BB, EMA, VWAP, Volume
│   ├── strategy/       ← signal logic + conflict resolver
│   ├── backtest/       ← execution engine + cost model
│   └── reporting/      ← metrics + charts
├── results/            ← CSV outputs
├── reports/            ← charts + final report
└── notebooks/          ← research notebooks
```

## Indicators Used
- **Bollinger Bands** — Length 100, Std 2.0/2.5
- **EMA** — 5, 7, 9, 15, 20 periods
- **Volume SMA** — 15, 20, 50, 100, 200 periods
- **VWAP** — resets daily

## Realistic Cost Model (India)
- Brokerage: ₹20 flat per side
- STT: 0.025% on sell side
- Transaction charges: 0.00345%
- GST: 18% on brokerage + charges
- Slippage: 0.05% per side

## Robustness Testing
- Monte Carlo: 1000 simulations
- Random baseline comparison
- Parameter sensitivity analysis
- Result: STABLE across parameter variations

## Key Discoveries
1. BB std 2.5 outperforms 2.0 consistently
2. Max 1 trade per day is optimal
3. 9:20-11:00 IST is best trading window
4. SBIN, INFY, HDFCBANK show strongest edge
5. Strategy beats random on 7/8 stocks

## Limitations
- Only 55 days of data (yfinance 5-min limit)
- Needs 1-2 years data for proper validation
- Framework is complete — plug in better data anytime

## Next Steps
- Connect Zerodha/Upstox API for historical data
- Run full optimization with 1000+ combinations
- Add portfolio-level position sizing
- Implement walk-forward optimization

## Tech Stack
- Python 3.10
- pandas, numpy, matplotlib
- yfinance for data
- Google Colab for development

## Author
**TusharQLab** — Quantitative Research
