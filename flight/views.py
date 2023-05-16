#                    ----- Needs -----
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib import messages

#                    ----- Log-In -----
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .login_form import CustomUserCreationForm

#                   ----- Facade's -----
from .admin_facade import AdministratorFacade
from .base_facade import FacadeBase
from .anon_facade import AnonymousFacade
from .cust_facade import CustomerFacade
from .airline_facade import AirlineFacade

#                    ----- Models -----
from .models import UserRoles, CustomUser, Countries, AirlineCompanies, Flights, Customers, Tickets, Adminstrators

User = get_user_model()

#------------------------------ Permissions ------------------------------------------

def admin_auth(user):
    return user.is_authenticated and user.user_role.role_name == 'admin'
# @user_passes_test(admin_auth)

def client_auth(user):
    return user.is_authenticated and user.user_role.role_name == 'client'
# @user_passes_test(client_auth)

def airline_auth(user):
    return user.is_authenticated and user.user_role.role_name == 'airline company'
# @user_passes_test(airline_auth)


# --------------------------------- Homes ----------------------------------------------

def base_home(request):
    return render(request, 'flight/home.html')

@login_required
@user_passes_test(admin_auth)
def admin_home(request):
    return render(request, 'flight/admin_home.html')

@login_required
@user_passes_test(client_auth)
def client_home(request):
    return render(request, 'flight/client_home.html')

@login_required
@user_passes_test(airline_auth)
def airline_home(request):
    return render(request, 'flight/airline_home.html')

#----------------------------------- ANONYMOS VIEWS FACADE ------------------------------------------
#------------------------------ Log-In, Register and Log-Out ----------------------------------

@csrf_exempt
def log_in(request):
    return AnonymousFacade.log_in(request)

@csrf_exempt
def register(request):
    return AnonymousFacade.register(request)

def log_out(request):
    logout(request)
    return redirect('base_home')


#------------------------------------ BASE VIEWS FACADE ------------------------------------------

def all_flights(request):
    flights = FacadeBase.get_all_flights()
    context = {'flights': flights}
    return render(request, 'flight/all_flights.html', context)


@csrf_exempt
def get_flight_by_id(request):
    if request.method == 'POST':
        flight_id = request.POST['flight_id']
        flight = FacadeBase.get_flight_by_id(flight_id)
        return render(request, 'flight/flight_by_id.html', {'flight': flight})
    else:
        flights = FacadeBase.get_all_flights()
        return render(request, 'flight/get_flight_by_id.html', {'flights':flights})


@csrf_exempt
def get_flights_by_parameters(request):
    if request.method == 'POST': 
        origin_country_id = request.POST['origin_country_id']
        destination_country_id = request.POST['destination_country_id']
        departure_time = request.POST['departure_time']
        landing_time = request.POST['landing_time']
        flight = FacadeBase.get_flights_by_parameters(origin_country_id, destination_country_id, departure_time, landing_time)
        return render(request, 'flight/flight_by_id.html', {'flight': flight})
    else:
        return render(request, 'flight/get_flight_by_param.html')
    

def all_airlines(request):
    companies = FacadeBase.get_all_airlines()
    context = {'companies': companies}
    return render(request, 'flight/all_airlines.html', context)


@csrf_exempt
def get_airline_by_id(request):
    if request.method == 'POST':
        airline_company_id = request.POST['airline_company_id']
        airline = FacadeBase.get_airline_by_id(airline_company_id)
        return render(request, 'flight/airline_by_id.html', {'airline': airline})
    else:
        companies = FacadeBase.get_all_airlines()
        return render(request, 'flight/get_airline_by_id.html', {'companies':companies})


@csrf_exempt
def get_airline_by_param(request):
    if request.method == 'POST': 
        name = request.POST['name']
        country_id = request.POST['country_id']
        airline = FacadeBase.get_airline_by_parameters(name, country_id)
        return render(request, 'flight/airline_by_id.html', {'airline': airline})
    else:
        return render(request, 'flight/get_airline_by_param.html')


def all_countries(request):
    countries = FacadeBase.get_all_countries()
    context = {'countries': countries}
    return render(request, 'flight/all_countries.html', context)


@csrf_exempt
def get_country_by_id(request):
    if request.method == 'POST':
        country_id = request.POST['country_id']
        country = FacadeBase.get_country_by_id(country_id)
        return render(request, 'flight/country_by_id.html', {'country': country})
    else:
        countries = FacadeBase.get_all_countries()
        return render(request, 'flight/get_country_by_id.html', {'countries':countries})


#----------------------------------- ADMIN VIEWS FACADE ------------------------------------------

@user_passes_test(admin_auth)
def all_customers(request):
    customers = AdministratorFacade.get_all_customers()
    context = {'customers': customers}
    return render(request, 'flight/all_cust.html', context)


@user_passes_test(admin_auth)
@csrf_exempt
def add_airline_company(request):
    if request.method == 'POST':
        name = request.POST['name']
        country_id = request.POST['country_id']
        user_id = request.POST['user_id']
        AdministratorFacade.add_airline(name, country_id, user_id)
        messages.success(request, 'Airline company added successfully.')
        return redirect(reverse('admin_home'))
    else:
        countries = FacadeBase.get_all_countries()
        users = CustomUser.objects.all()
        return render(request, 'flight/add_airline.html', {'countries': countries, 'users': users})


@user_passes_test(admin_auth)
@csrf_exempt
def add_customer(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        phone_number = request.POST['phone_number']
        credit_card_number = request.POST['credit_card_number']
        user_id = request.POST['user_id']
        AdministratorFacade.add_customer(first_name, last_name, address, phone_number, credit_card_number, user_id)

        messages.success(request, 'Customer added successfully.')
        return redirect(reverse('admin_home'))
    else:
        users = CustomUser.objects.all()
        return render(request, 'flight/add_cust.html', {'users': users})


@user_passes_test(admin_auth)
@csrf_exempt
def add_admin(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_id = request.POST['user_id']
        AdministratorFacade.add_administrator(first_name, last_name, user_id)
        messages.success(request, 'administrator added successfully.')
        return redirect(reverse('home'))
    else:
        users = CustomUser.objects.all()
        return render(request, 'flight/add_admin.html', {'users': users})


@user_passes_test(admin_auth)
@csrf_exempt
def remove_airline_company(request):
    if request.method == 'POST':
        airline_company_id = request.POST['airline_company_id']
        AdministratorFacade.remove_airline(airline_company_id)
        messages.success(request, 'airline company removed successfully.')
        return redirect(reverse('home'))
    else:
        companies = FacadeBase.get_all_airlines()
        return render(request, 'flight/remove_airline.html', {'companies': companies})


@user_passes_test(admin_auth)
@csrf_exempt
def remove_customer(request):
    if request.method == 'POST':
        customer_id = request.POST['customer_id']
        AdministratorFacade.remove_customer(customer_id)
        messages.success(request, 'customer removed successfully.')
        return redirect(reverse('home'))
    else:
        customers = AdministratorFacade.get_all_customers()
        return render(request, 'flight/remove_customer.html', {'customers': customers})


@user_passes_test(admin_auth)
@csrf_exempt
def remove_admin(request):
    if request.method == 'POST':
        admin_id = request.POST['admin_id']
        AdministratorFacade.remove_administrator(admin_id)
        messages.success(request, 'administrator removed successfully.')
        return redirect(reverse('home'))
    else:
        admins = Adminstrators.objects.all()
        return render(request, 'flight/remove_admin.html', {'admins': admins})


#----------------------------------- CUSTOMER VIEWS FACADE ------------------------------------------

@user_passes_test(client_auth)
@csrf_exempt
def update_customer(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer')
        parameter = request.POST.get('parameter')
        new_value = request.POST.get('new_value')
        CustomerFacade.update_customer(customer_id, parameter, new_value)
        messages.success(request, 'customer updated successfully.')
        return redirect('home')

    customers = Customers.objects.all()
    return render(request, 'flight/update_customer.html', {'customers': customers})


@user_passes_test(client_auth)
@csrf_exempt
def add_ticket(request):
    if request.method == 'POST':
        flight_id = request.POST.get('flight_id')
        customer_id = request.POST.get('customer_id')

        CustomerFacade.add_ticket(flight_id, customer_id)
        messages.success(request, 'ticket added successfully.')
        return redirect(reverse('home'))
    else:
        flights = FacadeBase.get_all_flights()
        customers = Customers.objects.all()
        return render(request, 'flight/add_ticket.html', {'flights': flights, 'customers':customers})


@user_passes_test(client_auth)
@csrf_exempt
def remove_ticket(request):
    if request.method == 'POST':
        ticket_id = request.POST['ticket_id']
        CustomerFacade.remove_ticket(ticket_id)
        messages.success(request, 'ticket removed successfully.')
        return redirect(reverse('home'))
    else:
        tickets = Tickets.objects.all()
        return render(request, 'flight/remove_ticket.html', {'tickets': tickets})


@user_passes_test(client_auth)
@csrf_exempt
def get_my_tickets(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        tickets = CustomerFacade.get_my_tickets(customer_id)
        return render(request, 'flight/my_tickets.html', tickets)
    else:
        customers = Customers.objects.all()
        return render(request, 'flight/get_ticket_customer_id.html', customers)


#----------------------------------- AIRLINE VIEWS FACADE ------------------------------------------

@user_passes_test(airline_auth)
@csrf_exempt
def update_airline_company(request):
    if request.method == 'POST':
        airline_company_id = request.POST.get('airline_company_id')
        parameter = request.POST.get('parameter')
        new_value = request.POST.get('new_value')
        AirlineFacade.update_airline(airline_company_id, parameter, new_value)
        messages.success(request, 'airline company updated successfully.')
        return redirect('home')

    companies = FacadeBase.get_all_airlines()
    return render(request, 'flight/update_airline.html', {'companies': companies})


@user_passes_test(airline_auth)
@csrf_exempt
def add_flight(request):
    if request.method == 'POST':
        airline_company_id = request.user.id
        origin_country_id = request.POST['origin_country_id']
        destination_country_id = request.POST['destination_country_id']
        departure_time = request.POST['departure_time']
        landing_time = request.POST['landing_time']
        remaining_tickets = request.POST['remaining_tickets']
        AirlineFacade.add_flight(airline_company_id, origin_country_id, destination_country_id, departure_time, landing_time, remaining_tickets)

        messages.success(request, 'Tickets added successfully.')
        return redirect('airline_home')
    else:
        countries = FacadeBase.get_all_countries()
        return render(request, 'flight/add_flight.html', {'countries':countries})


@user_passes_test(airline_auth)
@csrf_exempt
def update_flight(request):
    if request.method == 'POST':
        flight_id = request.POST.get('flight_id')
        parameter = request.POST.get('parameter')
        new_value = request.POST.get('new_value')
        AirlineFacade.update_flight(flight_id, parameter, new_value)
        messages.success(request, 'flight updated successfully.')
        return redirect('home')

    flights = FacadeBase.get_all_flights()
    return render(request, 'flight/update_flight.html', {'flights': flights})


@user_passes_test(airline_auth)
@csrf_exempt
def remove_flight(request):
    if request.method == 'POST':
        flight_id = request.POST['flight_id']
        AirlineFacade.remove_flight(flight_id)
        messages.success(request, 'Flight removed successfully.')
        return redirect(reverse('home'))
    else:
        flights = FacadeBase.get_all_flights()
        return render(request, 'flight/remove_flight.html', {'flights': flights})


#----------------------------------- Fuctionalety ---------------------------------------

@csrf_exempt
def buy_ticket(request, flight_id):
    if not request.user.is_authenticated:
        return redirect('login')

    try:
        flight = Flights.objects.get(id=flight_id)
    except Flights.DoesNotExist:
        return HttpResponse("Flight not found", status=404)

    try:
        customer = Customers.objects.get(user_id=request.user.id)
    except Customers.DoesNotExist:
        return redirect('add_new_customer', flight_id=flight_id)

    if flight.remaining_tickets <= 0:
        return HttpResponse("No tickets available for this flight", status=403)

    ticket = customer.tickets_set.create(flight_id=flight)
    flight.remaining_tickets -= 1
    flight.save()

    return messages.success(request, 'ticket bought successfully.')


def add_new_customer(request, flight_id):
    try:
        flight = Flights.objects.get(id=flight_id)
    except Flights.DoesNotExist:
        return HttpResponse("Flight not found", status=404)
        
    if hasattr(request.user, 'customer'):
        return redirect('buy_ticket', flight_id=flight_id, customer_id=customer.id)

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        phone_number = request.POST['phone_number']
        credit_card_number = request.POST['credit_card_number']
        user_id = CustomUser.objects.get(id=request.user.id)
        
        customer = Customers(first_name=first_name, last_name=last_name, 
                            address=address, phone_number=phone_number, 
                            credit_card_number=credit_card_number, user_id=user_id)
        customer.save()

        return redirect('buy_ticket', flight_id=flight_id)
    else:
        context = {'flight': flight}
        return render(request, 'flight/add_new_customer.html', context)


#----------------------------------- API ------------------------------------------------

def api_base(request):
    return render(request, 'flight/api_base.html')

@user_passes_test(admin_auth)
def api_admin(request):
    return render(request, 'flight/api_admin.html')

@user_passes_test(client_auth)
def api_client(request):
    return render(request, 'flight/api_client.html')

@user_passes_test(airline_auth)
def api_airline(request):
    return render(request, 'flight/api_airline.html')