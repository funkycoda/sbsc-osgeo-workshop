# Example: http://spatial-ecology.net/dokuwiki/doku.php?id=wiki:gdalbasic
# GDAL API: http://gdal.org/gdal_8h.html

import os
import glob
import gdal

# setup base paths
base_path = "/Users/funkycoda/projects/tmp/vmdata/"
alaska_path = "Alaska_NDVI/"
odata_path = "basic_adv_gdalogr/"

# setup data path to work on
data_path = os.path.join(base_path, alaska_path)
print("Data path: %s" % data_path)

def print_metadata(file):
    """Calculate min and max for the given raster"""

    # open the pointer to the file
    ds = gdal.Open(file)

    # print the metadata
    print("---------------------")
    print ds.GetMetadata()
    print("---------------------")

    # close the file pointer
    ds = None

def print_raster_min_max(file):

    # open the pointer to the file
    ds = gdal.Open(file)

    # print the metadata
    print("---------------------")
    print "[ RASTER BAND COUNT ]: ", ds.RasterCount
    print("---------------------")

    # get band
    srcband = ds.GetRasterBand(1)
    if srcband is None:
        print("No band found")
    else:
        print "[ NO DATA VALUE ] = ", srcband.GetNoDataValue()
        print "[ MIN ] = ", srcband.GetMinimum()
        print "[ MAX ] = ", srcband.GetMaximum()
        print "[ SCALE ] = ", srcband.GetScale()
        print "[ UNIT TYPE ] = ", srcband.GetUnitType()

    print("---------------------")

    # close the file pointer
    ds = None


def iterate_files():
    # # display all files
    # filelist = os.listdir(data_path)
    # for file in filelist:
    #     print(" >> %s " % file)

    # display only GeoTIFF files
    tif_files = glob.glob(os.path.join(data_path, 'Band*2007.tif'))
    for file in tif_files:
        print(" >> %s " % file)
        print_raster_min_max(file)
        break

def main():
    # starts everthing
    iterate_files()

main()
