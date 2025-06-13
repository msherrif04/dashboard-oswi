import streamlit as st
import pandas as pd


@st.cache_data
def scr_chloropleth_data():
    df = pd.read_csv("./Data/choropleth.csv", index_col=0)
    return df


@st.cache_data
def dr_chloropleth_data():
    df = pd.read_csv("./Data/dbr_choropleth.csv", index_col=0)
    return df


# Colaborators
@st.cache_data
def scr_colabs():
    df = pd.read_csv("./Data/numCollaborators.csv", index_col=0)
    return df


@st.cache_data
def dr_colabs():
    df = pd.read_csv("./Data/dbr_numCollaborators.csv", index_col=0)
    return df


# Number of Publications
@st.cache_data
def scr_publications():
    df = pd.read_csv("./Data/countries.csv", index_col=0)
    return df


@st.cache_data
def dr_publications():
    df = pd.read_csv("./Data/dbr_countries.csv", index_col=0)
    return df


# Funding data
@st.cache_data
def scr_funding():
    df = pd.read_csv("./data/funded_countries.csv", index_col=0)
    return df


@st.cache_data
def dr_funding():
    df = pd.read_csv("./data/dbr_funded_countries.csv", index_col=0)
    return df


# Journals
@st.cache_data
def scr_journals():
    df = pd.read_csv("./data/journal.csv", index_col=0)
    return df


@st.cache_data
def dr_journals():
    df = pd.read_csv("./data/dbr_journal.csv", index_col=0)
    return df
