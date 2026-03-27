
# BB100 Hybrid Strategy — Complete Notebook
# Run each section in Google Colab
# github.com/TusharQLab/bb100-hybrid-strategy

# SECTION 1: Install libraries
# !pip install yfinance pandas numpy matplotlib seaborn tqdm pyarrow

# SECTION 2: Import everything
import os, sys, warnings, json, time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from pathlib import Path
from datetime import datetime, timedelta
from itertools import product
from tqdm import tqdm
warnings.filterwarnings("ignore")

# SECTION 3: Config
# See config.json for all parameters

# SECTION 4-10: All functions are in src/ folder
# Data pipeline    → src/data/
# Indicators       → src/indicators/
# Strategy logic   → src/strategy/
# Backtest engine  → src/backtest/
# Optimization     → src/optimization/
# Reporting        → src/reporting/

# Full walkthrough available in README.md
# Results available in results/ folder
# Charts available in reports/ folder
