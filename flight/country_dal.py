from .models import UserRoles, CustomUser, Countries, AirlineCompanies, Flights, Customers, Tickets, Adminstrators
from django.utils import timezone


class CountryDal():
    def get_country_by_id(country_id):
        try:
            country = Countries.objects.get(id=country_id)
        except Countries.DoesNotExist:
            country = None
        return country

    def get_all_countries():
        countries = Countries.objects.all()
        return countries

    def add_country(country_name):
        country = Countries(name=country_name)
        country.save()

    def remove_country(country_id):
        Countries.objects.filter(id=country_id).delete()  
