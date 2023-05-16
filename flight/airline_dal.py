from .models import UserRoles, CustomUser, Countries, AirlineCompanies, Flights, Customers, Tickets, Adminstrators
from django.utils import timezone


class AirlineDal():
    def get_airline_by_username(username):
        airline_company = AirlineCompanies.objects.select_related('user_id').get(user_id__username=username)
        return airline_company


    def get_airline_by_country_id(country_id):
        airline_companies = AirlineCompanies.objects.select_related('country_id').filter(country_id__id=country_id)
        return airline_companies


    def get_airline_company_by_id(airline_company_id):
        try:
            airline_company = AirlineCompanies.objects.get(id=airline_company_id)
        except AirlineCompanies.DoesNotExist:
            airline_company = None
        return airline_company


    def get_airline_by_parameters(name, counrty_id):
        try:
            airline_company = AirlineCompanies.objects.get(name=name, id=counrty_id)
        except AirlineCompanies.DoesNotExist:
            airline_company = None
        return airline_company


    def get_all_airline_companies():
        airline_companies = AirlineCompanies.objects.all()
        return airline_companies


    def add_airline_company(name, country_id, user_id):
        try:
            country = Countries.objects.get(id=country_id)
        except ObjectDoesNotExist:
            return f"Country with id {country_id} does not exist."

        try:
            user = CustomUser.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return f"user with id {user_id} does not exist."

        airline_company = AirlineCompanies(name=name, country_id=country, user_id=user)
        airline_company.save()


    def update_airline_company(airline_company_id, parameter, new_value):
        try:
            airline = AirlineCompanies.objects.get(id=airline_company_id)
        except ObjectDoesNotExist:
            return f"airline company with id {airline_company_id} does not exist."

        setattr(airline, parameter, new_value)
        airline.save()


    def get_airline_by_parameters():
        pass


    def remove_airline_company(airline_company_id):
        AirlineCompanies.objects.filter(id=airline_company_id).delete()   