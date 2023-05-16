from .models import UserRoles, CustomUser, Countries, AirlineCompanies, Flights, Customers, Tickets, Adminstrators
from django.utils import timezone


class UsersDal():
    def get_user_by_username(username):
        try:
            user = CustomUser.objects.get(username=username)
            return user
        except CustomUser.DoesNotExist:
            msg = 'User Does Not Exist'
            return msg

    def get_user_by_id(user_id):
        try:
            user = CustomUser.objects.get(id=user_id)
            return user
        except CustomUser.DoesNotExist:
            msg = 'User Does Not Exist'
            return msg
    
    def get_all_users():
        users = CustomUser.objects.all()
        return users
        
    def create_user_role(role_name):
        new_role = UserRoles.objects.create(role_name=role_name)

    def add_user():
        # Register
        pass       

    def update_user(user_id, data):
        pass
    
    def remove_user(data):
        user = get_object_or_404(CustomUser, pk=product_id)
        user.delete()