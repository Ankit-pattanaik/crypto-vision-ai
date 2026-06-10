import streamlit as st
import plotly.graph_objects as go
import pandas as pd

from utils.data_loader import load_data
from utils.helpers import (
    get_coin_column,
    get_price_columns,
    format_currency
)

st.set_page_config(layout="wide")

# ======================================
# LOAD CSS
# ======================================
with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("💼 Portfolio Simulator")

# ======================================
# LOAD DATA
# ======================================
df = load_data()

coin_col = get_coin_column(df)

price_cols = get_price_columns(df)

date_col = price_cols["date"]
close_col = price_cols["close"]

# ======================================
# SELECT COIN
# ======================================
coins = sorted(
    df[coin_col]
    .dropna()
    .unique()
)

selected_coin = st.selectbox(
    "Choose Cryptocurrency",
    coins
)

df = df[
    df[coin_col]
    == selected_coin
]

# ======================================
# INVESTMENT SETTINGS
# ======================================
st.subheader(
    "Investment Settings"
)

col1, col2 = st.columns(2)

with col1:

    investment = st.number_input(
        "Investment Amount ($)",
        min_value=100,
        value=1000,
        step=100
    )

with col2:

    holding_days = st.slider(
        "Holding Period (Days)",
        min_value=7,
        max_value=365,
        value=30
    )

# ======================================
# SIMULATION
# ======================================
buy_price = df[
    close_col
].iloc[-holding_days]

current_price = df[
    close_col
].iloc[-1]

coins_bought = (
    investment
    / buy_price
)

current_value = (
    coins_bought
    * current_price
)

profit_loss = (
    current_value
    - investment
)

roi = (
    profit_loss
    / investment
) * 100

# ======================================
# KPI CARDS
# ======================================
k1, k2, k3, k4 = st.columns(4)

k1.metric(
    "Buy Price",
    format_currency(
        buy_price
    )
)

k2.metric(
    "Current Price",
    format_currency(
        current_price
    )
)

k3.metric(
    "Profit / Loss",
    format_currency(
        profit_loss
    )
)

k4.metric(
    "ROI",
    f"{roi:.2f}%"
)

# ======================================
# PORTFOLIO GROWTH
# ======================================
st.subheader(
    "📈 Portfolio Growth"
)

price_history = df[
    close_col
].tail(
    holding_days
)

portfolio_values = []

for price in price_history:

    value = (
        coins_bought
        * price
    )

    portfolio_values.append(
        value
    )

growth_df = pd.DataFrame({

    "Day":
    range(
        len(
            portfolio_values
        )
    ),

    "Portfolio":
    portfolio_values
})

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=growth_df["Day"],
        y=growth_df[
            "Portfolio"
        ],
        mode="lines",
        fill="tozeroy",
        name="Portfolio"
    )
)

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="#0E1117",
    plot_bgcolor="#161B22",
    hovermode="x unified",
    height=650,
    title=f"{selected_coin} Portfolio Growth"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ======================================
# RESULT
# ======================================
if roi > 0:

    st.success(
        f"🚀 Your investment "
        f"grew by "
        f"{roi:.2f}%"
    )

else:

    st.error(
        f"📉 Your investment "
        f"decreased by "
        f"{abs(roi):.2f}%"
    )