import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import streamlit as st


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


def compare_countries(df, country1="United States", country2="Jamaica"):

    # get values of two chosen countries
    comp_list = [country1, country2]
    # create dataframe with values of chosen countries
    temp_df = df[df.countries.isin(comp_list)]

    fig = px.bar(
        temp_df,
        x="countries",
        y="counts",
        text_auto=True,
        color="countries",
        labels={"counts": "Number of publications"},
        template="simple_white",
    )
    fig.update_layout(
        legend=dict(
            xanchor="right",
        )
    )
    return fig


@st.cache_data(
    hash_funcs={dict: lambda _: None}, show_spinner=True
)  # Use st.cache_data for data/figures
def funding_map(dataframe, path):
    funding_fig = px.treemap(
        dataframe,
        path=path,
        values="counts",
        color="counts",
        color_continuous_scale="YlGnBu",
        color_continuous_midpoint=np.average(
            dataframe["counts"], weights=dataframe["counts"]
        ),
        template="seaborn",
        maxdepth=2,
    )
    funding_fig.update_traces(root_color="lightgrey")
    funding_fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

    return funding_fig


def journal_chart(dataframe, number=[0, 10]):
    dataframe = dataframe.iloc[number[0] : number[1]]
    journal_fig = px.bar(
        dataframe,
        x="Journal",
        y="counts",
        text_auto=True,
        # color="Journal",
        labels={"counts": "Number of Publications"},
        template="simple_white",
    )
    journal_fig.update_layout(
        legend=dict(
            xanchor="right",
        )
    )
    return journal_fig


def scatter_plot(dataframe):
    fig = px.scatter(
        dataframe,
        x="SCR",
        y="DR",
        size="SCR+DR",
        color="ratio",
        hover_name="Journal",
        hover_data=["Journal", "SCR", "DR"],
        color_continuous_scale=["red", "green", "blue"],
        template="simple_white",
    )
    fig.update_layout(
        coloraxis_colorbar=dict(
            orientation="v",
            title="SCR : [SCR+DR]",
            thickness=5,
            len=0.8,
            nticks=3,
            yref="paper",
        )
    )

    return fig
