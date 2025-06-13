import streamlit as st
import datasets
import graphs

import plotly_express as px

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Disparities in Research",
    page_icon="📊",
    layout="centered",
)

# --- PAGE LOGO ---
LOGO_URL_LARGE = "./Images/logo.PNG"
st.logo(
    LOGO_URL_LARGE,
    size="large",
    link="https://sicklecellretinopathy.net",
)

# --- PAGE TITLE ---
st.title(
    "Investigating publication trends in Sickle Cell Retinopathy(SCR) and Diabetic Retinopathy (DR) over the years"
)

# --- CHOROPLETH MAP ---
st.title("Global Publication Heatmap")
tab1, tab2 = st.tabs(["Sickle Cell Retinopathy", "Diabetic Retinopathy"])

with tab1:
    st.subheader("Global Heatmap of Publications on Sickle Cell Retinopathy")
    scr_choropleth_df = datasets.scr_chloropleth_data()
    scr_choropleth_chart = graphs.create_choropleth(scr_choropleth_df)
    st.plotly_chart(scr_choropleth_chart, use_container_width=True)

    st.write(
        """
    1. The United States played a significant role in leading research on sickle cell retinopathy (SCR).
    2. European Union member countries and the United Kingdom made substantial contributions to SCR research.
    3. African countries, specifically Nigeria and Ghana, had limited involvement in SCR research.
    4. Jamaica had the most significant contribution among Caribbean islands.
    5. The top 20 contributors to SCR research encompassed diverse nations from various regions."""
    )


with tab2:
    st.subheader("Global Heatmap of Publications on Diabetic Retinopathy")
    dr_choropleth_df = datasets.dr_chloropleth_data()
    dr_choropleth_chart = graphs.create_choropleth(dr_choropleth_df)
    st.plotly_chart(dr_choropleth_chart, use_container_width=True)

    st.write(
        """
    1. The United States was the major driving force behind diabetic retinopathy (DR) research.
    2. The United Kingdom also played a substantial role in contributing to DR research.
    3. Ghana, Nigeria, Jamaica, and Cuba had noteworthy contributions to DR research.
    4. The top 20 contributors to DR research included the United States, Australia, Canada, and the United Kingdom.
    5. These statistics highlight the significant global disparity in research efforts for sickle cell retinopathy (SCR) and DR, predominantly led by high-income countries from the global North."""
    )

# --COLLABORATION EXTENT--
st.title("Extent of Internation Collaboration")

tab1, tab2 = st.tabs(["Sickle Cell Retinopathy", "Diabetic Retinopathy"])

with tab1:
    st.subheader(
        "Number of Collaborating Countries on Sickle Cell Retinopathy Research"
    )
    scr_colab_data = datasets.scr_colabs()
    scr_colab_chart = graphs.create_colab_chart(scr_colab_data, [1966, 2024])
    st.plotly_chart(scr_colab_chart, use_container_width=True)
    st.write(
        """
    1. Approximately 80% of published manuscripts on sickle cell retinopathy (SCR) had authors from a single country, with 20% involving authors from at least two countries.
    2. Conversely, in diabetic retinopathy (DR), approximately 74% of published manuscripts had authors from a single country, while about 25% included authors from at least two countries.
    3. International collaboration in research is on the rise, with an increasing number of publications featuring authors from different countries over the years.
                """
    )

with tab2:
    st.subheader("Number of Collaborating Countries on Diabetic Retinopathy Research")
    dr_colab_data = datasets.dr_colabs()
    dr_colab_chart = graphs.create_colab_chart(dr_colab_data, [1960, 2025])
    st.plotly_chart(dr_colab_chart, use_container_width=True)
    st.write(
        """
    1. Approximately 80% of published manuscripts on sickle cell retinopathy (SCR) had authors from a single country, with 20% involving authors from at least two countries.
    2. Conversely, in diabetic retinopathy (DR), approximately 74% of published manuscripts had authors from a single country, while about 25% included authors from at least two countries.
    3. International collaboration in research is on the rise, with an increasing number of publications featuring authors from different countries over the years.
                """
    )


# --PUBLICATIONS PER COUNTRY--
st.title("Number of Publications per Country")

tab1, tab2 = st.tabs(["Sickle Cell Retinopathy", "Diabetic Retinopathy"])
with tab1:
    st.subheader("Number of Publications per Country on Sickle Cell Retinopathy")
    scr_countries = datasets.scr_publications()

    st.dataframe(
        scr_countries,
        column_config={
            "_index": None,
            "countries": "Country",
            "counts": "Number of Publications",
        },
        hide_index=True,
    )
    st.subheader("Number of Publications per Country on Sickle Cell Retinopathy")
    figure = px.bar(
        scr_countries,
        x="countries",
        y="counts",
        title="20 Most Prolific Countries in DR Research",
    )
    st.plotly_chart(figure, use_container_width=True)

with tab2:
    st.subheader("Number of Publications per Country on Diabetic Retinopathy")
    dr_countries = datasets.dr_publications()

    st.dataframe(
        dr_countries,
        column_config={
            "_index": None,
            "countries": "Country",
            "counts": "Number of Publications",
        },
        hide_index=True,
    )
    st.subheader("Number of Publications per Country on Diabetic Retinopathy")
    figure = px.bar(
        dr_countries,
        x="countries",
        y="counts",
        title="20 Most Prolific Countries in DR Research",
    )
    st.plotly_chart(figure, use_container_width=True)
