import plotly.graph_objects as go


# ======================================
# THEME
# ======================================
def apply_theme(fig):

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0E1117",
        plot_bgcolor="#161B22",
        hovermode="x unified",
        font=dict(
            family="Poppins",
            size=14
        ),
        margin=dict(
            l=30,
            r=30,
            t=50,
            b=30
        ),
        legend=dict(
            orientation="h",
            y=1.02
        )
    )

    return fig


# ======================================
# LINE CHART
# ======================================
def line_chart(
    x,
    y,
    title,
    name="Value"
):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode="lines",
            name=name
        )
    )

    fig.update_layout(
        title=title,
        height=500
    )

    return apply_theme(fig)


# ======================================
# MULTI LINE
# ======================================
def multi_line_chart(
    df,
    x_col,
    y_cols,
    title
):

    fig = go.Figure()

    for col in y_cols:

        fig.add_trace(
            go.Scatter(
                x=df[x_col],
                y=df[col],
                mode="lines",
                name=col
            )
        )

    fig.update_layout(
        title=title,
        height=600
    )

    return apply_theme(fig)