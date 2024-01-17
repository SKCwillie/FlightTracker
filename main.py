from FlightRadar24 import FlightRadar24API
import time

# Downtown Kansas City Airport
LAT = 39.12587
LON = -94.58754
DIST = 16000
PAUSE = 30

fr = FlightRadar24API()


def print_flight_info(last_flight):
    bounds = fr.get_bounds_by_point(LAT, LON, DIST)
    flights = fr.get_flights(bounds=bounds)

    try:
        flight = flights[0]
        flight_details = fr.get_flight_details(flight)
        flight_id = flights[0].id

        if flight_id == last_flight:
            time.sleep(PAUSE)
            return print_flight_info(last_flight)
        else:
            print('')
            try:
                print(f'{flight_details["airline"]["name"]}')
            except IndexError:
                print('Private Flight')
            try:
                print(f'{flight_details["aircraft"]["model"]["text"]}')
                print(f'To: {flight_details["airport"]["origin"]["name"]}')
                print(f'From: {flight_details["airport"]["destination"]["name"]}')
                print(f'{flight.ground_speed}knts @ {flight.altitude}ft')
            except IndexError:
                pass
            last_flight = flight_id
            time.sleep(PAUSE)
            return print_flight_info(last_flight)

    except IndexError:
        time.sleep(PAUSE)
        print_flight_info(last_flight)


print_flight_info('')
