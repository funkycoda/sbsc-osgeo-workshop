import gdal

base_path = "/Users/funkycoda/projects/tmp/vmdata/"
alaska_path = "Alaska_NDVI"
data_path = "basic_adv_gdalogr"

# open dataset
ds = gdal.Open('input.tif')

print ds.GetMetadata()

# close dataset
ds = None
