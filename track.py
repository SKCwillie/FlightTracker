from models import Flight, fr
import time

global last_flight
last_flight = None
# Downtown Kansas City Airport
LAT = 39.12587
LON = -94.58754
DIST = 50000
PAUSE = 30



def print_flight(last_flight_id):
    bounds = fr.get_bounds_by_point(LAT, LON, DIST)
    response = fr.get_flights(bounds=bounds)

    if len(response) == 0:
        print('empty list')
        pass
    else:
        flight_id = response[0].id
        if flight_id == last_flight_id:
            print('recursive call')
            return print_flight(last_flight_id)
        else:
            last_flight = flight_id
            print(Flight(response[0]))


while True:
    print('new function call')
    print_flight(last_flight)
    time.sleep(PAUSE)
