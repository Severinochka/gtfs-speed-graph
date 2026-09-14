import geopandas as gpd
from loguru import logger

METRIC_CRS = "EPSG:3857"


def to_metric_crs(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """Приводит GeoDataFrame к метрической проекции (нужно для буферов в метрах)."""
    if gdf.crs is None:
        logger.warning("У GeoDataFrame не задан CRS, приведение невозможно проверить.")
    return gdf.to_crs(METRIC_CRS)


def build_buffers(houses_gdf: gpd.GeoDataFrame, radius: float) -> gpd.GeoDataFrame:
    """Строит буферы заданного радиуса (в метрах) вокруг домов."""
    projected = to_metric_crs(houses_gdf)
    buffered = projected.copy()
    buffered["geometry"] = projected.buffer(radius)
    return buffered
