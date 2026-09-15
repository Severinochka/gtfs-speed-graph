import geopandas as gpd
from infra_access.services.geo_service import build_buffers, to_metric_crs
from infra_access.utils.validators import check_not_empty, check_same_crs
from loguru import logger


def count_within_radius(
    houses_gdf: gpd.GeoDataFrame,
    objects_gdf: gpd.GeoDataFrame,
    radius: float,
) -> gpd.GeoDataFrame:
    """
    Считает количество объектов инфраструктуры в заданном радиусе (в метрах)
    от каждого дома.

    Возвращает копию houses_gdf с добавленной колонкой 'objects_count'.
    """
    check_not_empty(houses_gdf, "houses_gdf")
    check_not_empty(objects_gdf, "objects_gdf")
    check_same_crs(houses_gdf, objects_gdf)

    buffers = build_buffers(houses_gdf, radius)
    objects_projected = to_metric_crs(objects_gdf)

    joined = gpd.sjoin(buffers, objects_projected, how="inner", predicate="intersects")
    counts = joined.groupby(joined.index).size()

    result = houses_gdf.copy()
    result["objects_count"] = counts.reindex(result.index, fill_value=0)

    logger.info(f"Посчитана обеспеченность для {len(result)} домов, радиус={radius} м.")
    return result


def unserved_objects(
    houses_gdf: gpd.GeoDataFrame,
    objects_gdf: gpd.GeoDataFrame,
    radius: float,
) -> gpd.GeoDataFrame:
    """
    Возвращает дома, у которых нет ни одного объекта инфраструктуры
    в заданном радиусе доступности.
    """
    counted = count_within_radius(houses_gdf, objects_gdf, radius)
    unserved = counted[counted["objects_count"] == 0]

    logger.info(
        f"Найдено {len(unserved)} домов без инфраструктуры в радиусе {radius} м."
    )
    return unserved


def accessibility_ratio(
    houses_gdf: gpd.GeoDataFrame,
    objects_gdf: gpd.GeoDataFrame,
    radius: float,
) -> float:
    """
    Возвращает долю домов (от 0 до 1), обеспеченных инфраструктурой
    в заданном радиусе.
    """
    counted = count_within_radius(houses_gdf, objects_gdf, radius)
    served_count = (counted["objects_count"] > 0).sum()
    ratio = served_count / len(counted)

    logger.info(f"Доля обеспеченных домов: {ratio:.2%}")
    return ratio
