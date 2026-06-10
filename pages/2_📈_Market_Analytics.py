import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from utils.data_loader import load_data
from utils.helpers import (
    get_coin_column,
    get_price_columns
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

st.title("📈 Market Analytics")

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
    "Select Coin",
    coins
)

df = df[
    df[coin_col]
    == selected_coin
]

# ======================================
# VOLATILITY
# ======================================
st.subheader(
    "📊 Volatility Trend"
)

fig_vol = px.line(
    df,
    x=date_col,
    y="Volatility",
    template="plotly_dark"
)

fig_vol.update_layout(
    paper_bgcolor="#0E1117",
    plot_bgcolor="#161B22",
    hovermode="x unified",
    height=500
)

st.plotly_chart(
    fig_vol,
    use_container_width=True
)

# ======================================
# RETURN DISTRIBUTION
# ======================================
st.subheader(
    "📉 Daily Return Distribution"
)

fig_hist = px.histogram(
    df,
    x="Daily_Return",
    nbins=50,
    template="plotly_dark"
)

fig_hist.update_layout(
    paper_bgcolor="#0E1117",
    plot_bgcolor="#161B22",
    height=500
)

st.plotly_chart(
    fig_hist,
    use_container_width=True
)

# ======================================
# EXTERNAL MARKET
# ======================================
comparison_cols = []

keywords = [
    "gold",
    "nasdaq",
    "oil",
    "vix"
]

for col in df.columns:

    for word in keywords:

        if word in col.lower():
            comparison_cols.append(col)

st.subheader(
    "🌍 Market Comparison"
)

if comparison_cols:

    fig_compare = go.Figure()

    for col in comparison_cols:

        fig_compare.add_trace(
            go.Scatter(
                x=df[date_col],
                y=df[col],
                mode="lines",
                name=col
            )
        )

    fig_compare.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0E1117",
        plot_bgcolor="#161B22",
        height=600,
        hovermode="x unified"
    )

    st.plotly_chart(
        fig_compare,
        use_container_width=True
    )

st.success(
    f"{selected_coin} analytics loaded."
)