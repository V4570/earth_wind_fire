import pandas as pd
import shapely.wkt
from shapely.geometry import mapping, Polygon
import shapefile #PyShp
import fiona
#import arcpy
#from arcpy import env
#import ipdb; ipdb.set_trace()

df=pd.read_csv('../PythonWorkplace/datasets/V_ZONES_APOKLEISMOU_GEO.csv')
data=df.geometry

Vec = []
w = shapefile.Writer('../datasets/test')



for item in data:
	lilVec = shapely.wkt.loads(item)
	Vec.append(lilVec)

# Define a polygon feature geometry with one attribute
schema = {
    'geometry': 'Polygon',
    'properties': {'id': 'int'},
}

# Write a new Shapefile
with fiona.open('my_shp2.shp', 'w', 'ESRI Shapefile', schema) as c:
    ## If there are multiple geometries, put the "for" loop here
    for id, poly in enumerate(Vec):
	    c.write({
	        'geometry': mapping(poly),
	        'properties': {'id': id},
	    })







# for item in data:
# 	lilVec = shapely.wkt.loads(item)
# 	Vec.append(lilVec)
# 	w.record(lilVec)

# w.close()


# env.workspace = "./data"
# arcpy.FeatureToRaster_conversion("test.shp", "CLASS", "../datasets/output/roadsgrid", 25)
