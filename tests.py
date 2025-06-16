import pandas as pd
import datasets
import plotly_express as px
import plotly.graph_objects as go

scr_journals = datasets.scr_journals()
dr_journals = datasets.dr_journals()

all_journals = pd.merge(dr_journals, scr_journals, on="Journal", how="outer")
all_journals.rename(columns={"counts_x": "DR", "counts_y": "SCR"}, inplace=True)
all_journals
all_journals.fillna(0, inplace=True)
all_journals["SCR+DR"] = all_journals["SCR"] + all_journals["DR"]
all_journals["ratio"] = all_journals["SCR"] / all_journals["SCR+DR"]
all_journals["ratio"].describe()

fig = px.scatter(
    all_journals,
    x="SCR",
    y="DR",
    size="SCR+DR",
    color="ratio",
    hover_name="Journal",
    color_continuous_scale="Viridis",
    log_x=False,
    log_y=False,
)
fig.show()
