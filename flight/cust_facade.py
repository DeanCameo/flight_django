from .cust_dal import CustomerDal
from .airline_dal import AirlineDal
from .user_dal import UsersDal
from .admin_dal import AdminDal
from .ticket_dal import TicketsDal


class CustomerFacade():
    def update_customer(customer_id, parameter, new_value):
        CustomerDal.update_customer(customer_id, parameter, new_value)

    def add_ticket(flight_id, customer_id):
        TicketsDal.add_ticket(flight_id, customer_id)

    def remove_ticket(ticket_id):
        TicketsDal.remove_ticket(ticket_id)

    def get_my_tickets(customer_id):
        TicketsDal.get_tickets_by_customer_id(customer_id)