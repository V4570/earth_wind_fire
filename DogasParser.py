import pandas as pd
import shapely.wkt
import shapefile #PyShp
import arcpy
from arcpy import env

df=pd.read_csv('./Desktop/V_ZONES_APOKLEISMOU_GEO.csv')
data=df.geometry
Vec = shapely.wkt.loads(data)
w = shapefile.Writer('./Desktop/test')
w.record(Vec)
w.close()


env.workspace = "c:/data"
arcpy.FeatureToRaster_conversion("test.shp", "CLASS", "c:/output/roadsgrid", 25)
