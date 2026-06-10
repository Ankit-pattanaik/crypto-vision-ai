# 🚀 CryptoVision AI

A premium **multi-cryptocurrency analytics dashboard** built using **Python, Streamlit, Plotly, and Prophet**.

CryptoVision AI provides deep cryptocurrency market insights with an eye-catching fintech-inspired interface, technical indicators, forecasting, correlation analysis, and portfolio simulation.

---

## 🌟 Project Overview

CryptoVision AI is designed to help users analyze and compare multiple cryptocurrencies in one place.

Users can:

* Track individual cryptocurrency prices
* Compare up to **3 cryptocurrencies simultaneously**
* Explore **technical indicators** like RSI, MACD, and Bollinger Bands
* Forecast future prices using **Prophet**
* Analyze feature relationships and market correlations
* Simulate investment growth using a portfolio simulator

The project follows a modern **dark fintech UI** inspired by trading platforms like TradingView and CoinMarketCap Pro.

---

## ✨ Features

### 📊 Multi-Coin Dashboard

* Select any cryptocurrency
* View price movement with interactive charts
* Track market performance
* Premium KPI cards

### 📈 Compare 3 Cryptocurrencies

Compare up to **three cryptocurrencies** side-by-side.

Examples:

* BTC vs ETH vs DOGE
* SOL vs ADA vs XRP
* ETH vs LTC vs BNB

Interactive hover charts make comparison easier.

### 📉 Forecasting

Built using **Facebook Prophet**.

Features:

* Future price prediction
* Adjustable forecast period
* Confidence interval visualization
* Coin-specific forecasting

### ⚡ Technical Indicators

Advanced technical analysis tools:

#### RSI (Relative Strength Index)

Helps identify:

* Overbought conditions
* Oversold conditions

#### MACD

Shows:

* Trend momentum
* Signal line crossover
* Histogram movement

#### Bollinger Bands

Useful for:

* Volatility tracking
* Breakout identification
* Price reversal zones

### 📊 Correlation Analysis

Analyze relationships between market variables.

Includes:

* Correlation heatmaps
* Scatter plots
* Feature relationship analysis

### 💼 Portfolio Simulator

Simulate cryptocurrency investment performance.

Features:

* Investment amount input
* Holding period selection
* ROI calculation
* Portfolio growth chart

---

## 🖼️ Application Pages

```txt
📊 Dashboard
📈 Market Analytics
📉 Forecasting
⚡ Technical Indicators
📊 Correlation Analysis
💼 Portfolio Simulator
```

---

## 🛠️ Tech Stack

### Frontend

* Streamlit
* Custom CSS

### Visualization

* Plotly
* Plotly Graph Objects

### Data Processing

* Pandas
* NumPy

### Machine Learning / Forecasting

* Prophet
* Scikit-learn

---

## 📂 Project Structure

```txt
crypto_vision_ai/
│
├── app.py
│
├── assets/
│   └── style.css
│
├── data/
│   └── crypto_daily.csv
│
├── pages/
│   ├── 1_📊_Dashboard.py
│   ├── 2_📈_Market_Analytics.py
│   ├── 3_📉_Forecasting.py
│   ├── 4_⚡_Technical_Indicators.py
│   ├── 5_📊_Correlation_Analysis.py
│   └── 6_💼_Portfolio_Simulator.py
│
├── utils/
│   ├── data_loader.py
│   ├── helpers.py
│   ├── charts.py
│   ├── indicators.py
│   └── predictor.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation Guide

### 1. Clone Repository

```bash
git clone YOUR_REPOSITORY_LINK
```

Example:

```bash
git clone https://github.com/your-username/crypto-vision-ai.git
```

---

### 2. Move into Project Folder

```bash
cd crypto-vision-ai
```

---

### 3. Create Virtual Environment (Recommended)

Windows:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Run Application

```bash
streamlit run app.py
```
---

## 🚀 Future Improvements

Planned upgrades:

* Live crypto API integration
* Real-time price updates
* News sentiment analysis
* Advanced ML forecasting
* Trading signal alerts
* Mobile responsiveness

---

## 👨‍💻 Author

**Ankit Pattanaik**

Built with Python, Streamlit, and Plotly.

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository on GitHub
