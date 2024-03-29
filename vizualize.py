import os
import tarfile
from six.moves import urllib
from bokeh.io import output_file, output_notebook, show
from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, LogColorMapper, BasicTicker, ColorBar, Range1d,
    DataRange1d, PanTool, WheelZoomTool, BoxSelectTool
)
from bokeh.models.mappers import ColorMapper, LinearColorMapper
from bokeh.palettes import Viridis5, RdBu3, RdBu4
from bokeh.plotting import gmap
import numpy as np

HOUSING_PATH = "datasets/"


import pandas as pd

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "V_ZONES_APOKLEISMOU_GEO.csv")
    return pd.read_csv(csv_path)
# housing = load_housing_data()
# housing.head()



def vizualize(data, lons, lats): 
    coord = np.array(np.meshgrid(lons, lats)).T.reshape(-1,2)
    map_options = GMapOptions(lat=39.0742, lng=20.8243, map_type="hybrid", zoom=6)
    #import ipdb;ipdb.set_trace()

    plot = GMapPlot(
        x_range=Range1d(), y_range=Range1d(), map_options=map_options
    )
    plot.title.text = "Hey look! It's a scatter plot on a map!"

    # For GMaps to function, Google requires you obtain and enable an API key:
    #
    #     https://developers.google.com/maps/documentation/javascript/get-api-key
    #
    # Replace the value below with your personal API key:
    plot.api_key = " AIzaSyD99ZX7qJDs-VG_PN_3yRKE3Lw1BkPK-Go "
    # source = ColumnDataSource(
    # data=dict(lat=coord[:,1].tolist(),
    #           lon=coord[:,0].tolist()
    #           )
    # )
    # p = gmap("AIzaSyD99ZX7qJDs-VG_PN_3yRKE3Lw1BkPK-Go ", map_options, title="Austin")

    # p.circle(x="lon", y="lat", size=15, fill_color='blue', fill_alpha=0.8, source=source)

    data = data.reshape(-1,1)


    source = ColumnDataSource(
        data=dict(
            lat=coord[:,1].tolist(),
            lon=coord[:,0].tolist(),
            size=coord[:,1].tolist(),
            color=np.divide(data,200).tolist() 
        )
    )
    max_median_house_value = np.max(data)
    min_median_house_value = np.min(data)
    #import ipdb;ipdb.set_trace()
    #color_mapper = CategoricalColorMapper(factors=['hi', 'lo'], palette=[RdBu3[2], RdBu3[0]])
    color_mapper = LogColorMapper(palette="Viridis5", low=min_median_house_value, high=max_median_house_value)
    #color_mapper = LinearColorMapper(palette=RdBu4,low,high)

    circle = Circle(x="lon", y="lat", size="size", fill_color={'field': 'color', 'transform': color_mapper}, fill_alpha=0.2, line_color=None )

    plot.add_glyph(source, circle)

    color_bar = ColorBar(color_mapper=color_mapper, ticker=BasicTicker(),
                         label_standoff=12, border_line_color=None, location=(0,0))
    plot.add_layout(color_bar, 'left')

    plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())

    show(plot)