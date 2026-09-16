# infra_access

Библиотека для оценки обеспеченности жилых домов социальной инфраструктурой (школы, поликлиники, остановки).

## Возможности

- `count_within_radius(houses_gdf, objects_gdf, radius)` — количество объектов инфраструктуры в радиусе от каждого дома
- `unserved_objects(houses_gdf, objects_gdf, radius)` — дома без инфраструктуры в зоне доступности
- `accessibility_ratio(houses_gdf, objects_gdf, radius)` — доля обеспеченных домов

## Пример использования

```python
from infra_access import count_within_radius, accessibility_ratio

result = count_within_radius(houses_gdf, objects_gdf, radius=500)
ratio = accessibility_ratio(houses_gdf, objects_gdf, radius=500)
print(f"Доля обеспеченных домов: {ratio:.2%}")
```

## Требования

- Входные `GeoDataFrame` должны иметь одинаковый CRS.
- При пустых входных данных выбрасывается `EmptyGeoDataFrameError`.


## Установка

```bash
pip install infra-access
```

Пакет опубликован на PyPI: https://pypi.org/project/infra-access/