import pandas as pd


# ======================================
# FIND COLUMN BY KEYWORD
# ======================================
def find_column(df, keyword):

    for col in df.columns:

        if keyword.lower() in col.lower():
            return col

    return None


# ======================================
# GET COIN COLUMN
# ======================================
def get_coin_column(df):

    possible_names = [
        "coin",
        "symbol",
        "crypto",
        "currency",
        "asset",
        "ticker"
    ]

    for col in df.columns:

        if col.lower() in possible_names:
            return col

    return None


# ======================================
# GET PRICE COLUMNS
# ======================================
def get_price_columns(df):

    return {

        "date":
        find_column(df, "date"),

        "open":
        find_column(df, "open"),

        "high":
        find_column(df, "high"),

        "low":
        find_column(df, "low"),

        "close":
        find_column(df, "close"),

        "volume":
        find_column(df, "volume")
    }


# ======================================
# DAILY RETURNS
# ======================================
def calculate_returns(
    df,
    close_col
):

    df["Daily_Return"] = (
        df[close_col]
        .pct_change()
        * 100
    )

    return df


# ======================================
# VOLATILITY
# ======================================
def calculate_volatility(
    df,
    close_col,
    window=30
):

    returns = (
        df[close_col]
        .pct_change()
    )

    df["Volatility"] = (
        returns
        .rolling(window)
        .std()
        * 100
    )

    return df


# ======================================
# FORMATTERS
# ======================================
def format_currency(value):

    return f"${value:,.2f}"


def format_percentage(value):

    return f"{value:.2f}%"