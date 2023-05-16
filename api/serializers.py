from rest_framework import serializers
from flight import models

class UserRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserRoles
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = '__all__'

class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Countries
        fields = '__all__'

class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AirlineCompanies
        fields = '__all__'

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Flights
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customers
        fields = '__all__'

class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tickets
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Adminstrators
        fields = '__all__'