import plotly.express as px
import plotly.graph_objects as go


def create_choropleth(df, colorscale="Blues"):
    fig = go.Figure(
        data=go.Choropleth(
            locations=df["code"],
            z=df["count"],
            text=df["countries"],
            colorscale="YlGnBu",
            autocolorscale=False,
            reversescale=False,
            marker_line_color="grey",
            marker_line_width=0.5,
            colorbar_tickprefix="",
            colorbar_title="Publications",
        )
    )

    fig.update_layout(
        title_text="Heatmap of number of publications per country",
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type="equirectangular",
            showcountries=True,
            countrycolor="grey",
        ),
    )
    fig.update_traces(colorbar_orientation="h", selector=dict(type="choropleth"))
    fig.update_traces(colorbar=dict(thickness=5), selector=dict(type="choropleth"))

    return fig


def create_colab_chart(df, years):
    bar_chart = px.bar(
        df,
        x="Year",
        y=["1 country", "2 countries", "> 2 countries"],
        barmode="stack",
        template="simple_white",
        labels={
            "value": "Number of Publications",
        },
        title="Total Number of Collaborating Countries per Year",
    )
    # bar_chart.update_xaxes(type="category")
    bar_chart.update_layout(
        legend=dict(orientation="v", yanchor="top", y=1.02, xanchor="center", x=0.5),
        xaxis=dict(range=years),
    )
    return bar_chart
