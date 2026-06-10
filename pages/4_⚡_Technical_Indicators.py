import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from utils.data_loader import load_data
from utils.helpers import (
    get_coin_column,
    get_price_columns
)

from utils.indicators import (
    generate_indicators
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

st.title("⚡ Technical Indicators")

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
].copy()

# ======================================
# GENERATE INDICATORS
# ======================================
df = generate_indicators(
    df,
    close_col
)

# ======================================
# AUTO DETECT COLUMNS
# ======================================
rsi_col = None
macd_col = None
signal_col = None
upper_col = None
lower_col = None

for col in df.columns:

    col_lower = col.lower()

    if "rsi" in col_lower:
        rsi_col = col

    elif (
        "macd" in col_lower
        and "hist" not in col_lower
        and "signal" not in col_lower
    ):
        macd_col = col

    elif "signal" in col_lower:
        signal_col = col

    elif "upper" in col_lower:
        upper_col = col

    elif "lower" in col_lower:
        lower_col = col

# ======================================
# TABS
# ======================================
tab1, tab2, tab3 = st.tabs([
    "📈 RSI",
    "📊 MACD",
    "🎯 Bollinger Bands"
])

# ======================================
# RSI
# ======================================
with tab1:

    st.subheader(
        f"{selected_coin} RSI"
    )

    if rsi_col:

        fig_rsi = go.Figure()

        fig_rsi.add_trace(
            go.Scatter(
                x=df[date_col],
                y=df[rsi_col],
                mode="lines",
                name="RSI"
            )
        )

        fig_rsi.add_hline(
            y=70,
            line_dash="dash"
        )

        fig_rsi.add_hline(
            y=30,
            line_dash="dash"
        )

        fig_rsi.update_layout(
            template="plotly_dark",
            paper_bgcolor="#0E1117",
            plot_bgcolor="#161B22",
            hovermode="x unified",
            height=500
        )

        st.plotly_chart(
            fig_rsi,
            use_container_width=True
        )

    else:
        st.warning(
            "RSI data unavailable."
        )

# ======================================
# MACD
# ======================================
with tab2:

    st.subheader(
        f"{selected_coin} MACD"
    )

    if macd_col and signal_col:

        fig_macd = make_subplots(
            rows=2,
            cols=1,
            shared_xaxes=True
        )

        fig_macd.add_trace(
            go.Scatter(
                x=df[date_col],
                y=df[macd_col],
                mode="lines",
                name="MACD"
            ),
            row=1,
            col=1
        )

        fig_macd.add_trace(
            go.Scatter(
                x=df[date_col],
                y=df[signal_col],
                mode="lines",
                name="Signal"
            ),
            row=1,
            col=1
        )

        histogram = (
            df[macd_col]
            - df[signal_col]
        )

        fig_macd.add_trace(
            go.Bar(
                x=df[date_col],
                y=histogram,
                name="Histogram"
            ),
            row=2,
            col=1
        )

        fig_macd.update_layout(
            template="plotly_dark",
            paper_bgcolor="#0E1117",
            plot_bgcolor="#161B22",
            height=700,
            hovermode="x unified"
        )

        st.plotly_chart(
            fig_macd,
            use_container_width=True
        )

    else:
        st.warning(
            "MACD data unavailable."
        )

# ======================================
# BOLLINGER
# ======================================
with tab3:

    st.subheader(
        f"{selected_coin} Bollinger Bands"
    )

    if upper_col and lower_col:

        fig_bb = go.Figure()

        fig_bb.add_trace(
            go.Scatter(
                x=df[date_col],
                y=df[close_col],
                mode="lines",
                name="Price"
            )
        )

        fig_bb.add_trace(
            go.Scatter(
                x=df[date_col],
                y=df[upper_col],
                mode="lines",
                name="Upper Band"
            )
        )

        fig_bb.add_trace(
            go.Scatter(
                x=df[date_col],
                y=df[lower_col],
                mode="lines",
                fill="tonexty",
                name="Lower Band"
            )
        )

        fig_bb.update_layout(
            template="plotly_dark",
            paper_bgcolor="#0E1117",
            plot_bgcolor="#161B22",
            hovermode="x unified",
            height=600
        )

        st.plotly_chart(
            fig_bb,
            use_container_width=True
        )

    else:
        st.warning(
            "Bollinger Band data unavailable."
        )