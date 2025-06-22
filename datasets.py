import streamlit as st
import pandas as pd


@st.cache_data
def scr_chloropleth_data():
    df = pd.read_csv("data/choropleth.csv", index_col=0)
    return df


@st.cache_data
def dr_chloropleth_data():
    df = pd.read_csv("data/dbr_choropleth.csv", index_col=0)
    return df


# Colaborators
@st.cache_data
def scr_colabs():
    df = pd.read_csv("data/numCollaborators.csv", index_col=0)
    return df


@st.cache_data
def dr_colabs():
    df = pd.read_csv("data/dbr_numCollaborators.csv", index_col=0)
    return df


# Number of Publications
@st.cache_data
def scr_publications():
    df = pd.read_csv("data/countries.csv", index_col=0)
    return df


@st.cache_data
def dr_publications():
    df = pd.read_csv("data/dbr_countries.csv", index_col=0)
    return df


# Funding data
@st.cache_data
def scr_funding():
    df = pd.read_csv("data/funded_countries.csv", index_col=0)
    return df


@st.cache_data
def dr_funding():
    df = pd.read_csv("data/dbr_funded_countries.csv", index_col=0)
    return df


# Journals
@st.cache_data
def scr_journals():
    df = pd.read_csv("data/journal.csv", index_col=0)
    return df


@st.cache_data
def dr_journals():
    df = pd.read_csv("data/dbr_journal.csv", index_col=0)
    return df


@st.cache_data
def process_df(scr_df, dr_df, on="Journal"):
    all_journals = pd.merge(dr_df, scr_df, on=on, how="outer")
    all_journals.rename(columns={"counts_x": "DR", "counts_y": "SCR"}, inplace=True)
    all_journals.fillna(0, inplace=True)
    all_journals["SCR+DR"] = all_journals["SCR"] + all_journals["DR"]
    all_journals["ratio"] = all_journals["SCR"] / all_journals["SCR+DR"]
    return all_journals
