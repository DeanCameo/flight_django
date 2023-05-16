
from django.contrib import admin

from .models import UserRoles, CustomUser, Countries, AirlineCompanies, Flights, Customers, Tickets, Adminstrators

admin.site.register(UserRoles)
admin.site.register(CustomUser)
admin.site.register(Countries)
admin.site.register(AirlineCompanies)
admin.site.register(Flights)
admin.site.register(Customers)
admin.site.register(Tickets)
admin.site.register(Adminstrators)