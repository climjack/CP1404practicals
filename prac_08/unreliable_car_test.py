from prac_08.unreliable_car import UnreliableCar


def main():
    good_car = UnreliableCar("Mostly Good", 100, 90)
    bad_car = UnreliableCar("Dodgy", 100, 9)
    for x in range(1, 12):
        print("Attempting to drive {}km:".format(x))
        print(f"{bad_car.name:12} drove {good_car.drive(x):2}km")
        print(f"{bad_car.name:12} drove {bad_car.drive(x):2}km")
    print(good_car)
    print(bad_car)


main()
