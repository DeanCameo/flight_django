from .models import UserRoles, CustomUser, Countries, AirlineCompanies, Flights, Customers, Tickets, Adminstrators
from django.utils import timezone


class FlightsDal():
    def get_flights_by_parameters(origin_counry_id, detination_country_id, departure_time, landing_time):
        try:
            flights = Flights.objects.get(origin_counry_id= origin_counry_id, 
                                        detination_country_id= detination_country_id, 
                                        departure_time=departure_time, landing_time=landing_time)
        except Flights.DoesNotExist:
            flights = None
        return flights

    def get_flights_by_airline_id(airline_company_id):
        try:
            flights = Flights.objects.get(airline_company_id=airline_company_id)
        except Flights.DoesNotExist:
            flights = None
        return flights

    def get_arrival_flights(country_id):
        pass

    def get_departure_flights(country_id):
        pass

    def get_flights_by_origin_country_id(origin_country_id):
        try:
            flights = Flights.objects.get(origin_country_id=origin_country_id)
        except Flights.DoesNotExist:
            flights = None
        return flights

    def get_flights_by_destination_country_id(destination_country_id):
        try:
            flights = Flights.objects.get(destination_country_id=destination_country_id)
        except Flights.DoesNotExist:
            flights = None
        return flights

    def get_flights_by_departure_date(departure_time):
        try:
            flight = Flights.objects.get(departure_time=departure_time)
        except Flights.DoesNotExist:
            flight = None
        return flight

    def get_flights_by_landing_date(landing_time):
        try:
            flight = Flights.objects.get(landing_time=landing_time)
        except Flights.DoesNotExist:
            flight = None
        return flight

    def get_flights_by_customer_id(customer_id):
        pass

    def get_flight_by_flight_id(flight_id):
        try:
            flight = Flights.objects.get(id=flight_id)
        except Flights.DoesNotExist:
            flight = None
        return flight

    def get_all_flights():
        flights = Flights.objects.all()
        return flights

    def add_flight(airline_company_id, origin_country_id, destination_country_id, departure_time, landing_time, remaining_tickets):
        airline_company = AirlineCompanies.objects.get(user_id=airline_company_id)
        origin_country = Countries.objects.get(id=origin_country_id)
        destination_country = Countries.objects.get(id=destination_country_id)

        flight = Flights(airline_company_id=airline_company, origin_country_id=origin_country, 
                        destination_country_id=destination_country,
                        departure_time=departure_time, landing_time=landing_time, 
                        remaining_tickets=remaining_tickets)
        flight.save()

    def update_flight(flight_id, parameter, new_value):
        try:
            flight = Flights.objects.get(id=flight_id)
        except ObjectDoesNotExist:
            return f"flight with id {flight_id} does not exist."

        setattr(flight, parameter, new_value)
        flight.save()

    def remove_flight(flight_id):
        Flights.objects.filter(id=flight_id).delete()  
