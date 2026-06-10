import streamlit as st
import plotly.graph_objects as go

from utils.data_loader import load_data
from utils.helpers import (
    get_price_columns,
    get_coin_column,
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

st.title("📊 Crypto Dashboard")

# ======================================
# LOAD DATA
# ======================================
df = load_data()

coin_col = get_coin_column(df)

price_cols = get_price_columns(df)

date_col = price_cols["date"]
open_col = price_cols["open"]
high_col = price_cols["high"]
low_col = price_cols["low"]
close_col = price_cols["close"]
volume_col = price_cols["volume"]

# ======================================
# VIEW MODE
# ======================================
mode = st.radio(
    "Choose View",
    [
        "Single Coin",
        "Compare Coins"
    ],
    horizontal=True
)

# ======================================
# SINGLE COIN
# ======================================
if mode == "Single Coin":

    coins = sorted(
        df[coin_col]
        .dropna()
        .unique()
    )

    selected_coin = st.selectbox(
        "Select Cryptocurrency",
        coins
    )

    filtered_df = df[
        df[coin_col]
        == selected_coin
    ]

    latest_price = (
        filtered_df[
            close_col
        ].iloc[-1]
    )

    high_price = (
        filtered_df[
            high_col
        ].iloc[-1]
    )

    low_price = (
        filtered_df[
            low_col
        ].iloc[-1]
    )

    change_pct = (
        (
            filtered_df[
                close_col
            ].iloc[-1]
            -
            filtered_df[
                close_col
            ].iloc[-2]
        )
        /
        filtered_df[
            close_col
        ].iloc[-2]
    ) * 100

    # KPI CARDS
    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Current Price",
        format_currency(
            latest_price
        )
    )

    c2.metric(
        "24H Change",
        f"{change_pct:.2f}%"
    )

    c3.metric(
        "High",
        format_currency(
            high_price
        )
    )

    c4.metric(
        "Low",
        format_currency(
            low_price
        )
    )

    # CANDLESTICK
    fig = go.Figure()

    fig.add_trace(
        go.Candlestick(
            x=filtered_df[
                date_col
            ],
            open=filtered_df[
                open_col
            ],
            high=filtered_df[
                high_col
            ],
            low=filtered_df[
                low_col
            ],
            close=filtered_df[
                close_col
            ],
            name=selected_coin
        )
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0E1117",
        plot_bgcolor="#161B22",
        height=700,
        hovermode="x unified",
        xaxis_rangeslider_visible=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ======================================
# COMPARE COINS
# ======================================
else:

    coins = sorted(
        df[coin_col]
        .dropna()
        .unique()
    )

    selected_coins = st.multiselect(
        "Compare up to 3 Coins",
        options=coins,
        default=coins[:3],
        max_selections=3
    )

    fig = go.Figure()

    for coin in selected_coins:

        temp_df = df[
            df[coin_col]
            == coin
        ]

        fig.add_trace(
            go.Scatter(
                x=temp_df[
                    date_col
                ],
                y=temp_df[
                    close_col
                ],
                mode="lines",
                name=coin
            )
        )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0E1117",
        plot_bgcolor="#161B22",
        height=700,
        hovermode="x unified",
        title="Crypto Comparison"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )