import streamlit as st
import plotly.graph_objects as go

from utils.data_loader import load_data
from utils.predictor import (
    forecast_crypto
)

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

st.title("📉 Crypto Forecasting")

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
# SETTINGS
# ======================================
st.sidebar.subheader(
    "Forecast Settings"
)

future_days = st.sidebar.slider(
    "Forecast Days",
    min_value=7,
    max_value=90,
    value=30
)

# ======================================
# FORECAST MODEL
# ======================================
with st.spinner(
    "Training forecasting model..."
):

    forecast = forecast_crypto(
        df=df,
        date_col=date_col,
        close_col=close_col,
        future_days=future_days
    )

st.success(
    "Forecast complete!"
)

# ======================================
# CHART
# ======================================
fig = go.Figure()

# Actual
fig.add_trace(
    go.Scatter(
        x=df[date_col],
        y=df[close_col],
        mode="lines",
        name="Actual Price"
    )
)

# Predicted
fig.add_trace(
    go.Scatter(
        x=forecast["ds"],
        y=forecast["yhat"],
        mode="lines",
        name="Predicted Price"
    )
)

# Confidence Upper
fig.add_trace(
    go.Scatter(
        x=forecast["ds"],
        y=forecast["yhat_upper"],
        mode="lines",
        line=dict(width=0),
        showlegend=False
    )
)

# Confidence Lower
fig.add_trace(
    go.Scatter(
        x=forecast["ds"],
        y=forecast["yhat_lower"],
        fill="tonexty",
        mode="lines",
        line=dict(width=0),
        name="Confidence Interval"
    )
)

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="#0E1117",
    plot_bgcolor="#161B22",
    hovermode="x unified",
    height=700,
    title=f"{selected_coin} Forecast"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ======================================
# FORECAST TABLE
# ======================================
st.subheader(
    "📋 Forecast Data"
)

forecast_table = forecast[
    [
        "ds",
        "yhat",
        "yhat_lower",
        "yhat_upper"
    ]
].tail(future_days)

st.dataframe(
    forecast_table,
    use_container_width=True
)