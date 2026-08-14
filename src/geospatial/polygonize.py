import geopandas as gpd
import rasterio
from rasterio.features import shapes
from shapely.geometry import shape


def mask_to_polygons(mask_path):
    with rasterio.open(mask_path) as source:
        mask = source.read(1)
        records = [shape(geometry) for geometry, value in shapes(mask, mask=mask.astype(bool), transform=source.transform) if value]
        return gpd.GeoDataFrame(geometry=records, crs=source.crs)
