from FlightRadar24 import FlightRadar24API

fr = FlightRadar24API()


def round_alt(alt):
    if alt < 7000:
        return alt
    else:
        return round(alt, -3)


class Flight:

    def __init__(self, api_flight):
        details = fr.get_flight_details(api_flight)
        self.id = api_flight.id
        self.details = fr.get_flight_details(api_flight)
        self.callsign = details['identification']['callsign']
        self.model = details['aircraft']['model']['text']
        self.ground_speed = api_flight.ground_speed
        self.altitude = api_flight.altitude

        try:
            self.airline = details['airline']['name']
        except TypeError:
            self.airline = 'Privately Operated'

        try:
            self.from_name = details['airport']['origin']['name']
            self.from_icao = details['airport']['origin']['code']['icao']
            self.from_region = details['airport']['origin']['position']['region']['city']
            self.to_name = details['airport']['origin']['name']
            self.to_icao = details['airport']['destination']['code']['icao']
            self.to_region = details['airport']['destination']['position']['region']['city']
        except TypeError:
            self.from_name = None
            self.from_icao = None
            self.from_region = None
            self.to_name = None
            self.to_icao = None
            self.to_region = None

    def __repr__(self):
        if self.from_name:
            rep = f"""


            
            
            
{self.model}
{self.airline}
From: {self.from_icao} -- {self.from_region}
To: {self.to_icao} -- {self.to_region}
{self.ground_speed}kts @ {round_alt(self.altitude):,}ft


        """
            return rep
        else:
            rep = f"""


            
            
{self.model}
{self.airline}
{self.ground_speed}kts @ {self.altitude:,}ft



"""
            return rep
