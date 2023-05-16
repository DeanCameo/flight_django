from .models import UserRoles, CustomUser, Countries, AirlineCompanies, Flights, Customers, Tickets, Adminstrators
from django.utils import timezone

class AdminDal():

    def add_administrator(first_name, last_name, user_id):
        try:
            user = CustomUser.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return f"user with id {user_id} does not exist."

        admin = Adminstrators(first_name=first_name, last_name=last_name, user_id=user)
        admin.save()

    def remove_administrator(admin_id):
        Adminstrators.objects.filter(id=admin_id).delete()  

