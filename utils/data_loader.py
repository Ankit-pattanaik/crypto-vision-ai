import pandas as pd
import streamlit as st

from utils.helpers import (
    find_column,
    get_coin_column,
    calculate_returns,
    calculate_volatility
)

from utils.indicators import (
    generate_indicators
)


@st.cache_data
def load_data():

    df = pd.read_csv(
        "data/crypto_daily.csv"
    )

    # Clean columns
    df.columns = [
        col.strip()
        for col in df.columns
    ]

    # Detect columns
    date_col = find_column(
        df,
        "date"
    )

    close_col = find_column(
        df,
        "close"
    )

    coin_col = get_coin_column(
        df
    )

    # Convert datetime
    if date_col:

        df[date_col] = pd.to_datetime(
            df[date_col],
            errors="coerce"
        )

    # Sort correctly
    if coin_col:

        df = df.sort_values(
            [coin_col, date_col]
        )

    else:

        df = df.sort_values(
            date_col
        )

    # Feature engineering
    if close_col:

        df = calculate_returns(
            df,
            close_col
        )

        df = calculate_volatility(
            df,
            close_col
        )

        df = generate_indicators(
            df,
            close_col
        )

    # Remove missing
    df = df.dropna()

    return df