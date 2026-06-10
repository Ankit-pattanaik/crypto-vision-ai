import streamlit as st

st.set_page_config(
    page_title="CryptoVision AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================
# LOAD CSS
# ======================================
with open(
    "assets/style.css"
) as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ======================================
# SIDEBAR
# ======================================
st.sidebar.markdown("""
# 🚀 CryptoVision AI

### Premium Analytics

Analyze & compare cryptocurrencies with:

✅ Price tracking  
✅ Coin comparison  
✅ Forecasting  
✅ RSI / MACD  
✅ Portfolio simulation  
""")

# ======================================
# HERO
# ======================================
st.markdown("""
<div class='hero'>

<h1>
🚀 CryptoVision AI
</h1>

<p>
Advanced Multi-Crypto Analytics Platform
</p>

</div>
""", unsafe_allow_html=True)

# ======================================
# FEATURES
# ======================================
st.subheader(
    "Platform Features"
)

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class='metric-card'>
        <h3>📊 Analytics</h3>
        <p>
        Deep market analytics
        with beautiful charts.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class='metric-card'>
        <h3>⚡ Technical</h3>
        <p>
        RSI, MACD,
        Bollinger Bands.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class='metric-card'>
        <h3>📉 Forecasting</h3>
        <p>
        Predict future
        crypto trends.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.subheader(
    "🔥 Why CryptoVision AI?"
)

st.write("""
CryptoVision AI is a lightweight,
premium cryptocurrency analytics platform
built with Python + Streamlit.

### Features Included

- Multi-coin comparison
- Interactive hover charts
- Technical indicators
- Price forecasting
- Portfolio simulation
- Correlation analysis
""")

st.success(
    "Select a page from the sidebar."
)