from .user_dal import UsersDal
from .airline_dal import AirlineDal
from .country_dal import CountryDal
from .flight_dal import FlightsDal


class FacadeBase():
    def get_all_flights():
        flights = FlightsDal.get_all_flights()                                                                                  #    DONE
        return flights

    def get_flight_by_id(flight_id):
        flight = FlightsDal.get_flight_by_flight_id(flight_id)                                                                  #    DONE
        return flight

    def get_flights_by_parameters(origin_country_id, destination_country_id, departure_time, landing_time):
        flights = FlightsDal.get_flights_by_parameters(origin_counry_id, detination_country_id, departure_time, landing_time)   #    DONE
        return flights

    def get_all_airlines():
        airlines = AirlineDal.get_all_airline_companies()                                                                       #    DONE
        return airlines

    def get_airline_by_id(airline_company_id):
        airline = AirlineDal.get_airline_company_by_id(airline_company_id)                                                      #    DONE
        return airline

    def get_airline_by_parameters(name, counrty_id):
        airline = AirlineDal.get_airline_by_parameters(name, counrty_id)                                                        #    DONE
        return airline

    def get_all_countries():
        countries = CountryDal.get_all_countries()                                                                              #    DONE
        return countries

    def get_country_by_id(counrty_id):
        country = CountryDal.get_country_by_id(counrty_id)                                                                      #    DONE
        return country

    def create_new_user(username, password, email, role_name): # -------- for internal usage
        UsersDal.add_user(username, password, email, role_name)

    def create_user_role(role_name):
        UsersDal.create_user_role(role_name)                                                                                    #    DONE