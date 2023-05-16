from .models import UserRoles, CustomUser, Countries, AirlineCompanies, Flights, Customers, Tickets, Adminstrators
from django.utils import timezone

class TicketsDal():
    def get_tickets_by_customer_id(customer_id):
        try:
            tickets = Tickets.objects.get(customer_id=customer_id)
        except Tickets.DoesNotExist:
            ticket = None
        return ticket

    def get_ticket_by_id(ticket_id):
        try:
            ticket = Tickets.objects.get(id=ticket_id)
        except Tickets.DoesNotExist:
            ticket = None
        return ticket

    def get_all_tickets():
        tickets = Tickets.objects.all()
        return tickets

    def add_ticket(data):
        flight = Flights.objects.get(id=flight_id)
        customer = Customers.objects.get(id=customer_id)

        ticket = Tickets(flight_id=flight, customer_id=customer)
        ticket.save()

    def update_ticket(ticket_id, data):
        pass

    def remove_ticket(ticket_id):
        Tickets.objects.filter(id=ticket_id).delete()  
