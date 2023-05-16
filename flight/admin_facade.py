from .cust_dal import CustomerDal
from .airline_dal import AirlineDal
from .user_dal import UsersDal
from .admin_dal import AdminDal


class AdministratorFacade():
    def get_all_customers():
        customers = CustomerDal.get_all_customers()                                                         # YES
        return customers
        
    def add_airline(name, country_id, user_id):
        AirlineDal.add_airline_company(name, country_id, user_id)                                           # YES

    def add_customer(first_name, last_name, address, phone_number, credit_card_number, user_id):
        CustomerDal.add_customer(first_name, last_name, address, phone_number, credit_card_number, user_id) # YES                       

    def add_administrator(first_name, last_name, user_id):
        AdminDal.add_administrator(first_name, last_name, user_id)                                          # YES

    def remove_airline(airline_company_id):
        AirlineDal.remove_airline_company(airline_company_id)                                               # YES

    def remove_customer(customer_id):
        CustomerDal.remove_customer(customer_id)                                                            # YES

    def remove_administrator(admin_id):
        AdminDal.remove_administrator(admin_id)                                                             # YES
