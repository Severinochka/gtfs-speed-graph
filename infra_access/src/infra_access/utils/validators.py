import geopandas as gpd
from infra_access.exceptions import CRSMismatchError, EmptyGeoDataFrameError


def check_not_empty(gdf: gpd.GeoDataFrame, name: str) -> None:
    """Проверяет, что GeoDataFrame не пустой."""
    if gdf.empty:
        raise EmptyGeoDataFrameError(f"GeoDataFrame '{name}' пуст.")


def check_same_crs(gdf_a: gpd.GeoDataFrame, gdf_b: gpd.GeoDataFrame) -> None:
    """Проверяет совпадение систем координат двух GeoDataFrame."""
    if gdf_a.crs != gdf_b.crs:
        raise CRSMismatchError(f"CRS не совпадают: {gdf_a.crs} != {gdf_b.crs}")
