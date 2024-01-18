from models import Flight, fr
import time

# Downtown Kansas City Airport
LAT = 39.12587
LON = -94.58754
DIST = 50000
PAUSE = 30
last_flight = None


def print_flight(last_flight_id):
    bounds = fr.get_bounds_by_point(LAT, LON, DIST)
    response = fr.get_flights(bounds=bounds)

    if len(response) == 0:
        pass
    else:
        flight_id = response[0].id
        if flight_id == last_flight_id:
            time.sleep(PAUSE)
            return print_flight(last_flight_id)
        else:
            print(Flight(response[0]))
            return flight_id


if __name__ == '__main__':
    while True:
        try:
            last_flight = print_flight(last_flight)
        except KeyError:
            pass
        time.sleep(PAUSE)
