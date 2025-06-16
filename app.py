import streamlit as st
import datasets
import graphs

import plotly_express as px
from millify import millify


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
    st.subheader("20 Most Prolific Countries on Sickle Cell Retinopathy")
    figure = px.bar(
        scr_countries,
        x="countries",
        y="counts",
        title="Publications per Country on Sickle Cell Retinopathy",
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
    st.subheader("20 Most Prolific Countries on Diabetic Retinopathy")
    figure = px.bar(
        dr_countries,
        x="countries",
        y="counts",
        title="Publications per Country on Diabetic Retinopathy",
    )
    st.plotly_chart(figure, use_container_width=True)


# --COMPARE COUNTRIES--

st.title("Compare The Publication Output of Any Two Countries")
country_list = scr_countries["countries"].tolist()
country_1 = st.selectbox("Country 1", country_list)
country_2 = st.selectbox("Country 2", country_list)

tab1, tab2 = st.tabs(["Sickle Cell Retinopathy", "Diabetic Retinopathy"])
with tab1:
    comparison_plot = graphs.compare_countries(scr_countries, country_1, country_2)
    st.plotly_chart(comparison_plot, use_container_width=True)

with tab2:
    comparison_plot = graphs.compare_countries(dr_countries, country_1, country_2)
    st.plotly_chart(comparison_plot, use_container_width=True)


##--FUNDING MAP--
scr_funding_data = datasets.scr_funding()
dr_funding_data = datasets.dr_funding()

# labels
funding_labels = {"Sources": "Funding Sources", "Total_funding": "Times Funded"}

# Number of Funding entities
num_funding_ents_scr = scr_funding_data["Funding"].count()
num_funding_ents_dr = dr_funding_data["Funding"].count()
delta_ents = millify(0 - (num_funding_ents_dr / num_funding_ents_scr))
delta_funds = millify(
    0 - (dr_funding_data["counts"].sum() / scr_funding_data["counts"].sum())
)

# Times funded
times_funded_scr = scr_funding_data["counts"].sum()
times_funded_dr = dr_funding_data["counts"].sum()

st.title("Number of Reported Funding Sources For Research on SCR and DR")

st.subheader("Number of Funding Sources per Country on Diabetic Retinopathy")
dr_ents, dr_funds = st.columns(2)
dr_ents.metric(
    label=funding_labels["Sources"],
    value=millify(num_funding_ents_dr),
    border=True,
)

dr_funds.metric(
    label=funding_labels["Total_funding"],
    value=millify(times_funded_dr),
    border=True,
)

st.subheader("Number of Funding Sources per Country on Sickle Cell Retinopathy")
scr_ents, scr_funds = st.columns(2)
scr_ents.metric(
    label=funding_labels["Sources"],
    value=millify(num_funding_ents_scr),
    delta=f"{delta_ents} x less",
    border=True,
)

scr_funds.metric(
    label=funding_labels["Total_funding"],
    value=millify(times_funded_scr),
    delta=f"{delta_funds} x less",
    border=True,
)

st.subheader("Distrubtion of Funding Sources per Country")
tab1, tab2 = st.tabs(["Sickle Cell Retinopathy", "Diabetic Retinopathy"])

with tab1:
    st.subheader("Number of Funding Sources per Country on Sickle Cell Retinopathy")
    scr_funding_fig = graphs.funding_map(scr_funding_data, ["countries", "Funding"])
    st.plotly_chart(scr_funding_fig)

    st.write(
        """
    1. The USA secured the majority of declared funding sources for sickle cell retinopathy (SCR) research, with 438 sources.
    2. France, and UK with 46, and 41 declared funding sources, respectively.
    3. Jamaica had 24 reported funding sources.
    4. Nigeria had funding for six SCR research projects, while Ghana had two sources of funding.
                """
    )

with tab2:
    st.subheader("Number of Funding Sources per Country on Diabetic Retinopathy")
    filtered = dr_funding_data.groupby("countries")["counts"].sum().reset_index()
    dr_funding_fig = graphs.funding_map(filtered, ["countries", "counts"])
    st.plotly_chart(dr_funding_fig, use_container_width=True)
    st.write(
        """
    1. The United States obtained the majority of declared funding sources for diabetic retinopathy (DR) research, with 20,800 sources.
    2. The United Kingdom secured 6,143 sources, and China had 4,551 sources of funding.
    3. Ghana received funding for 40 DR research projects, while Nigeria had 145 declared funding sources.
                """
    )


# --Journals
st.header("Which journal has published the most on sickle cell retinopathy?")
scr_journals = datasets.scr_journals()
dr_journals = datasets.dr_journals()
num_journals_scr = scr_journals["Journal"].count()
num_journals_dr = dr_journals["Journal"].count()


col1, col2 = st.columns(2)
col1.metric(
    label="Number of Journals Publishing on Sickle Cell Retinopathy",
    value=num_journals_scr,
    border=True,
)

col2.metric(
    label="Number of Journals Publishing on Diabetic Retinopathy",
    value=num_journals_dr,
    border=True,
)

all_journals = datasets.process_df(scr_journals, dr_journals)
scatter_plot = graphs.scatter_plot(all_journals)
st.plotly_chart(scatter_plot, use_container_width=True)

st.write(
    """
1. Leading scientific journals like the "American Journal of Ophthalmology" and the "British Journal of Ophthalmology" have significantly enriched the publishing landscape on sickle cell retinopathy.
2. "Archives of Ophthalmology" has also been a substantial contributor to this field.
3. The "European Journal of Ophthalmology" and the "Investigative Ophthalmology and Visual Sciences" have consistently published research papers on sickle cell retinopathy.
4. Other ophthalmology-related and haematology-focused publications have also played vital roles in disseminating research on this topic.            

5. The publishing landscape for diabetic retinopathy (DR) is robust, with various scientific journals contributing to research dissemination.
6. Investigative Ophthalmology and Visual Science is the most prolific journal in this field, publishing 1,406 research papers.
7. Other notable journals, such as Retina, Ophthalmology, and the American Journal of Ophthalmology, have made significant contributions.
8. Non-ophthalmology-focused journals like Diabetes Care, Diabetes Medicine, and Diabetes Research and Clinical Practice have also played a role in publishing research on DR .           
                
                """
)

st.divider()

with st.container():
    st.markdown(
        """
    Built with ❤️ by [Mohammed-Sherrif Fuseini][1].   
    Member of the [Sickle Cell Retinopathy Network][4].  
    Connect with me: [LinkedIn][2] | [Email][3].   

    [1]: https://sites.google.com/view/msfuseini
    [2]: https://www.linkedin.com/in/msfuseini/
    [3]: mailto:msherrif04@gmail.com
    [4]: https://www.sicklecellretinopathy.net/
    """
    )
