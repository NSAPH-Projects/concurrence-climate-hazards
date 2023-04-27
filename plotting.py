import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set_style("whitegrid")
sns.set_context("paper")

import plotly.express as px
import matplotlib.pyplot as plt

from mpl_toolkits.axes_grid1 import make_axes_locatable
import contextily as ctx 

from urllib.request import urlopen
import json


def get_counties():
    with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
        counties = json.load(response)
    return counties

def get_hotspopt_dict():
    hsdict = {
        'wfday':{"title":"wildfire", "title_map":"Total days of wildfire", "year_min":'2007', "year_max":'2022'},
        'heatday':{"title":"heat", "title_map":"Total days of heat", "year_min":'2007', "year_max":'2022'},
        'coldday':{"title":"cold", "title_map":"Total cold days", "year_min":'2007', "year_max":'2022'},
        'polluted':{"title":"pollution", "title_map":"Total days of pollution", "year_min":'2007', "year_max":'2021'},
        'smoke_polluted':{"title":"smoke pollution", "title_map":"Total days of smoke pollution", "year_min":'2007', "year_max":'2021'},
        "hwp":{"title":"heat & wildfire & pollution", "title_map":"Total days of heat & wildfire & pollution", "year_min":'2007', "year_max":'2021'},
        "hws":{
            "title":"heat & wildfire & smoke pollution",
            "title_map":"Total days of heat & wildfire & smoke pollution",
            "year_min":'2007',
            "year_max":'2021'},
        "hp":{"title":"heat & pollution", "title_map":"Total days of heat & pollution", "year_min":'2007', "year_max":'2021'},
        "hw":{"title":"heat & wildfire", "title_map":"Total days of heat & wildfire", "year_min":'2007', "year_max":'2022'},
        "ws":{
            "title":"wildfire & smoke pollution", 
            "title_map":"Total days of wildfire & smoke pollution", "year_min":'2007', "year_max":'2021'},      
        'hwps':{
            "title":"heat or wildfire or pollution",  
            "title_map":"Totay days of heat or wildfire or pollution",
            "year_min":'2007',
            "year_max":'2021'}
    }
    return hsdict


def statePlot(df, data, title, cmap, zoom, dpi):
    f,ax = plt.subplots(1,1, figsize=(8,8), 
    sharex=True,sharey=True, dpi=dpi)
    f.tight_layout(pad=0.8)
    ax.set_axis_off()
    plt.title(title,fontsize='large')
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="3%", pad=0.2)
    ux = df.to_crs(epsg=3857).plot(data, ax=ax, 
    edgecolor='k',    cmap=cmap, alpha = 1, linewidth=0.1,
    legend=True, cax=cax)
    #ctx.add_basemap(ux,    zoom=zoom,
    # source=ctx.providers.Stamen.TonerLite);
    plt.ylabel('Days of exposure', fontsize=12)
    # Use savefig to save your map
    plt.tight_layout()
    plt.savefig(
    'figures/zip_hotspots_' + data +'.png')
    plt.show()

    
def trend_plot(trends_df, l, hotspot, title, year_min='2006', year_max='2021'):
    f, ax = plt.subplots(1,1, figsize = (4,3))
    sns.lineplot(data = trends_df, x="time", y=hotspot, ax=ax)

    sns.lineplot(data = trends_df[
        trends_df.COUNTY_CODE.isin(l)], 
                 x="time", 
                 y=hotspot, 
                 hue="COUNTY_CODE", 
                 palette="tab10",
                 ax=ax)

    plt.xlabel("Year")
    plt.ylabel("Number of days of concurrence")
    plt.title(title)
    plt.xlim([pd.to_datetime(year_min), pd.to_datetime(year_max)])
    plt.tight_layout()
    plt.savefig("figures/trends_"+title+".png")


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
    fig.write_image("figures/maps_"+hotspot+"_hotspot.png")
    
    
if __name__ == "__main__":
    pass