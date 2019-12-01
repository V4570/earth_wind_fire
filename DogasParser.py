import pandas as pd
import shapely.wkt
from shapely.geometry import mapping, Polygon
import shapefile #PyShp
import fiona
from PIL import Image
import numpy as np

def get_data():
	im = Image.open('../PythonWorkplace/datasets/rae_status-V_ZONES_APOKLEISMOU_GEO.tif')
	#import ipdb; ipdb.set_trace()


	imarray = np.array(im)

	mask = np.sum(imarray, axis = 2)

	mask2 = np.where((mask.T != 0), 0, 1)


	return mask2

#import arcpy
#from arcpy import env


# df=pd.read_csv('../PythonWorkplace/datasets/V_ZONES_APOKLEISMOU_GEO.csv')
# data=df.geometry


# Vec = []
# w = shapefile.Writer('../datasets/test')



# for item in data:
# 	lilVec = shapely.wkt.loads(item)
# 	Vec.append(lilVec)

# # Define a polygon feature geometry with one attribute
# schema = {
#     'geometry': 'Polygon',
#     'properties': {'id': 'int'},
# }

# # Write a new Shapefile
# with fiona.open('my_shp2.shp', 'w', 'ESRI Shapefile', schema) as c:
#     ## If there are multiple geometries, put the "for" loop here
#     for id, poly in enumerate(Vec):
# 	    c.write({
# 	        'geometry': mapping(poly),
# 	        'properties': {'id': id},
# 	    })






# # 1. Define pixel_size and NoData value of new raster
# NoData_value = -9999
# x_res = 0.25 # assuming these are the cell sizes
# y_res = 0.25 # change as appropriate
# pixel_size = 1

# # 2. Filenames for in- and output
# _in = r"my_shp2.shp.shp"
# _out = r"my_tif2.tif"

# # 3. Open Shapefile
# source_ds = ogr.Open(_in)
# source_layer = source_ds.GetLayer()
# x_min, x_max, y_min, y_max = source_layer.GetExtent()

# # 4. Create Target - TIFF
# cols = int( (x_max - x_min) / x_res )
# rows = int( (y_max - y_min) / y_res )

# _raster = gdal.GetDriverByName('GTiff').Create(_out, cols, rows, 1, gdal.GDT_Byte)
# _raster.SetGeoTransform((x_min, x_res, 0, y_max, 0, -y_res))
# _band = _raster.GetRasterBand(1)
# _band.SetNoDataValue(NoData_value)


# # 5. Rasterize why is the burn value 0... isn't that the same as the background?
# gdal.RasterizeLayer(_raster, [1], source_layer, burn_values=[0])















# for item in data:
# 	lilVec = shapely.wkt.loads(item)
# 	Vec.append(lilVec)
# 	w.record(lilVec)

# w.close()


# env.workspace = "./data"
# arcpy.FeatureToRaster_conversion("test.shp", "CLASS", "../datasets/output/roadsgrid", 25)
