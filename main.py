# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from core.geo_utils import haversine_distance


def main():
    #две условные остановки в СПб
    stop_a = (59.9343, 30.3351)
    stop_b = (59.9386, 30.3141)

    distance_km = haversine_distance(*stop_a, *stop_b)
    print(f"Расстояние между остановками: {distance_km:.3f} км")


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
