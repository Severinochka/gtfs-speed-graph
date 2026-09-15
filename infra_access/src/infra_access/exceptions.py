class InfraAccessError(Exception):
    """Базовое исключение библиотеки."""


class EmptyGeoDataFrameError(InfraAccessError):
    """Выбрасывается, если на вход передан пустой GeoDataFrame."""


class CRSMismatchError(InfraAccessError):
    """Выбрасывается, если CRS домов и объектов не совпадают."""
