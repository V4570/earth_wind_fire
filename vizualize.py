import os
import tarfile
from six.moves import urllib
import pandas as pd
import wind_speed
import wrapper as w
from bokeh.io import output_file, output_notebook, show
from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, LogColorMapper, BasicTicker, ColorBar, Range1d,
    DataRange1d, PanTool, WheelZoomTool, BoxSelectTool
)
from bokeh.models.mappers import ColorMapper, LinearColorMapper
from bokeh.palettes import Viridis5
HOUSING_PATH = "datasets/housing"
#HOUSING_PATH = "datasets/"


def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
   # csv_path = os.path.join(housing_path, "V_ZONES_APOKLEISMOU_GEO.csv")
    return pd.read_csv(csv_path)
housing = load_housing_data()



def vizualize(housing):

    a = w.wrapper()
    import ipdb; ipdb.set_trace()
    map_options = GMapOptions(lat=39.0742, lng=21.8243, map_type="hybrid", zoom=6)

    plot = GMapPlot(
        x_range=Range1d(), y_range=Range1d(), map_options=map_options
    )

    plot.title.text = "Wind turbines"

    # For GMaps to function, Google requires you obtain and enable an API key:
    #
    #     https://developers.google.com/maps/documentation/javascript/get-api-key
    #
    # Replace the value below with your personal API key:
    plot.api_key = " AIzaSyD99ZX7qJDs-VG_PN_3yRKE3Lw1BkPK-Go "

    source = ColumnDataSource(
        data=dict(
            lat=housing.latitude.tolist(),
            lon=housing.longitude.tolist(),
            size=housing.median_income.tolist(),
            color=housing.median_house_value.tolist()
        )
    )
    max_median_house_value = housing.loc[housing['median_house_value'].idxmax()]['median_house_value']
    min_median_house_value = housing.loc[housing['median_house_value'].idxmin()]['median_house_value']

    #color_mapper = CategoricalColorMapper(factors=['hi', 'lo'], palette=[RdBu3[2], RdBu3[0]])
    #color_mapper = LogColorMapper(palette="Viridis5", low=min_median_house_value, high=max_median_house_value)
    color_mapper = LinearColorMapper(palette=Viridis5)

    circle = Circle(x="lon", y="lat", size="size", fill_color={'field': 'color', 'transform': color_mapper}, fill_alpha=0.5, line_color=None )

    plot.add_glyph(source, circle)

    color_bar = ColorBar(color_mapper=color_mapper, ticker=BasicTicker(),
                         label_standoff=12, border_line_color=None, location=(0,0))
    #plot.add_layout(color_bar, 'left')

    #plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
    plot.add_tools(PanTool(), WheelZoomTool())
    show(plot)

vizualize(housing)