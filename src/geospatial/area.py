def total_area_m2(polygons, projected_crs=None):
    if polygons.crs is None:
        raise ValueError("Polygons need a CRS before area can be calculated.")
    if projected_crs:
        polygons = polygons.to_crs(projected_crs)
    elif polygons.crs.is_geographic:
        polygons = polygons.to_crs(polygons.estimate_utm_crs())
    return float(polygons.area.sum())
