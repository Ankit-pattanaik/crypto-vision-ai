import pandas as pd


# ======================================
# RSI
# ======================================
def calculate_rsi(
    close_prices,
    period=14
):

    delta = close_prices.diff()

    gain = delta.clip(lower=0)

    loss = -delta.clip(
        upper=0
    )

    avg_gain = gain.rolling(
        period
    ).mean()

    avg_loss = loss.rolling(
        period
    ).mean()

    rs = avg_gain / avg_loss

    rsi = 100 - (
        100 / (1 + rs)
    )

    return rsi


# ======================================
# MACD
# ======================================
def calculate_macd(
    close_prices
):

    ema12 = close_prices.ewm(
        span=12,
        adjust=False
    ).mean()

    ema26 = close_prices.ewm(
        span=26,
        adjust=False
    ).mean()

    macd = ema12 - ema26

    signal = macd.ewm(
        span=9,
        adjust=False
    ).mean()

    histogram = (
        macd - signal
    )

    return (
        macd,
        signal,
        histogram
    )


# ======================================
# BOLLINGER
# ======================================
def calculate_bollinger(
    close_prices,
    window=20
):

    sma = close_prices.rolling(
        window
    ).mean()

    std = close_prices.rolling(
        window
    ).std()

    upper = sma + (
        std * 2
    )

    lower = sma - (
        std * 2
    )

    return (
        sma,
        upper,
        lower
    )


# ======================================
# GENERATE INDICATORS
# ======================================
def generate_indicators(
    df,
    close_col
):

    columns = [
        c.lower()
        for c in df.columns
    ]

    # RSI
    if not any(
        "rsi" in c
        for c in columns
    ):

        df["RSI"] = calculate_rsi(
            df[close_col]
        )

    # MACD
    if not any(
        "macd" in c
        for c in columns
    ):

        (
            df["MACD"],
            df["Signal_Line"],
            df["MACD_Histogram"]
        ) = calculate_macd(
            df[close_col]
        )

    # Bollinger
    if not any(
        "upper" in c
        for c in columns
    ):

        (
            df["BB_Middle"],
            df["BB_Upper"],
            df["BB_Lower"]
        ) = calculate_bollinger(
            df[close_col]
        )

    return df