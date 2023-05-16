from .flight_dal import FlightsDal
from .airline_dal import AirlineDal


class AirlineFacade():
    def get_my_flights():
        pass

    def update_airline(airline_company_id, parameter, new_value):
        AirlineDal.update_airline_company(airline_company_id, parameter, new_value)

    def add_flight(airline_company_id, origin_country_id, destination_country_id, departure_time, landing_time, remaining_tickets):
        FlightsDal.add_flight(airline_company_id, origin_country_id, destination_country_id, departure_time, landing_time, remaining_tickets)

    def update_flight(flight_id, parameter, new_value):
        FlightsDal.update_flight(flight_id, parameter, new_value)

    def remove_flight(flight_id):
        FlightsDal.remove_flight(flight_id)
