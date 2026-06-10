import streamlit as st
import plotly.express as px

from utils.data_loader import load_data
from utils.helpers import (
    get_coin_column
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

st.title("📊 Correlation Analysis")

# ======================================
# LOAD DATA
# ======================================
df = load_data()

coin_col = get_coin_column(df)

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
# NUMERIC DATA
# ======================================
numeric_df = df.select_dtypes(
    include="number"
)

# ======================================
# HEATMAP
# ======================================
st.subheader(
    f"{selected_coin} Correlation Heatmap"
)

corr = numeric_df.corr()

fig_heat = px.imshow(
    corr,
    text_auto=".2f",
    aspect="auto",
    color_continuous_scale="Viridis"
)

fig_heat.update_layout(
    template="plotly_dark",
    paper_bgcolor="#0E1117",
    plot_bgcolor="#161B22",
    height=800
)

st.plotly_chart(
    fig_heat,
    use_container_width=True
)

# ======================================
# RELATIONSHIP EXPLORER
# ======================================
st.subheader(
    "📈 Feature Relationship"
)

col1, col2 = st.columns(2)

with col1:

    x_axis = st.selectbox(
        "X Axis",
        numeric_df.columns
    )

with col2:

    y_axis = st.selectbox(
        "Y Axis",
        numeric_df.columns,
        index=1
    )

fig_scatter = px.scatter(
    numeric_df,
    x=x_axis,
    y=y_axis,
    trendline="ols",
    template="plotly_dark"
)

fig_scatter.update_layout(
    paper_bgcolor="#0E1117",
    plot_bgcolor="#161B22",
    hovermode="closest",
    height=600
)

st.plotly_chart(
    fig_scatter,
    use_container_width=True
)

correlation = (
    numeric_df[
        [x_axis, y_axis]
    ]
    .corr()
    .iloc[0, 1]
)

st.info(
    f"Correlation between "
    f"**{x_axis}** and "
    f"**{y_axis}** = "
    f"**{correlation:.2f}**"
)