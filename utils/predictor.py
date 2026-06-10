from prophet import Prophet
import pandas as pd


def forecast_crypto(
    df,
    date_col,
    close_col,
    future_days=30
):

    forecast_df = df[
        [date_col, close_col]
    ].copy()

    forecast_df.columns = [
        "ds",
        "y"
    ]

    model = Prophet(
        daily_seasonality=True
    )

    model.fit(
        forecast_df
    )

    future = (
        model
        .make_future_dataframe(
            periods=future_days
        )
    )

    forecast = model.predict(
        future
    )

    return forecast