from .models import UserRoles, CustomUser, Countries, AirlineCompanies, Flights, Customers, Tickets, Adminstrators
from django.utils import timezone
from django import forms



class CustomerDal():
    def get_customer_by_username(username):
        try:
            user = CustomUser.objects.get(username=username)
            user_id = user.id
            customer = Customers.objects.get(id=user_id)
            return customer
        except Users.DoesNotExist:
            msg = 'User Does Not Exist'
            return msg


    def get_customer_by_id(customer_id):
        try:
            customer = Customers.objects.get(id=customer_id)
            return customer
        except Customers.DoesNotExist:
            msg = 'Customer Does Not Exist'
            return msg


    def get_all_customers():
        customers = Customers.objects.all()
        return customers


    def add_customer(first_name, last_name, address, phone_number, credit_card_number, user_id):
        try:
            user = CustomUser.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return f"user with id {user_id} does not exist."

        customer = Customers(first_name=first_name, last_name=last_name, 
                             address=address, phone_number=phone_number, 
                             credit_card_number=credit_card_number, user_id=user_id)
        customer.save()


    def update_customer(customer_id, parameter, new_value):
        try:
            customer = Customers.objects.get(id=customer_id)
        except ObjectDoesNotExist:
            return f"customer with id {customer_id} does not exist."

        setattr(customer, parameter, new_value)
        customer.save()
            

    def remove_customer(customer_id):
        Customers.objects.filter(id=customer_id).delete()  



    #### ------ CRUD ------- ####
        # def get_by_id(): 
        #     pass
        # def get_All():
        #     pass
        # def add():
        #     pass
        # def update():
        #     pass
        # def add_All():
        #     pass
        # def remove():
        #     pass

   
    

