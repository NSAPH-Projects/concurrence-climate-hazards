import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set_style("whitegrid")
sns.set_context("paper")

import plotly.express as px
import matplotlib.pyplot as plt

from urllib.request import urlopen
import json


def get_counties():
    with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
        counties = json.load(response)
    return counties
    

def trend_plot(trends_df, l, hotspot, title, year_min='2006', year_max='2021'):
    plt.figure(1, figsize = (4,3))
    sns.lineplot(data = trends_df, x="time", y=hotspot)

    sns.lineplot(data = trends_df[
        trends_df.COUNTY_CODE.isin(l)], 
                 x="time", 
                 y=hotspot, 
                 hue="COUNTY_CODE", 
                 palette="tab10")

    plt.xlabel("Year")
    plt.ylabel("Number of days of concurrence")
    plt.title(title)
    plt.xlim([pd.to_datetime(year_min), pd.to_datetime(year_max)])
    plt.tight_layout()


def draw_map(df, counties, hotspot, title):
    fig = px.choropleth_mapbox(df, 
                                width=400, 
                                height=400,
                                geojson=counties, 
                                locations='COUNTY_CODE', 
                                color = hotspot,
                                color_continuous_scale = "Viridis",
                                mapbox_style="white-bg",
                                zoom=4,
                                title=title,
                                center = {"lat": 36, "lon": -119},
                                labels = {hotspot:"Day count"}
    )
    #fig.update_geos(fitbounds="locations", visible=False)
    #fig.update_layout(width=100, title_text="Side By Side Subplots")
    fig.update_layout(margin={"r":0,"l":0,"b":0})
    fig.show()
    fig.write_image("figures/"+title+".png")
    
    
if __name__ == "__main__":
    pass