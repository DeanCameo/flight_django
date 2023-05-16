from django.urls import path
from . import views

urlpatterns = [
#------------------------------ ANONYMOS FACADE ------------------------------------------   
    path('', views.base_home, name='base_home'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('client_home/', views.client_home, name='client_home'),
    path('airline_home/', views.airline_home, name='airline_home'),

    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('register/', views.register, name='register'),
    
    path('flight/buy_ticket/<int:flight_id>/', views.buy_ticket, name='buy_ticket'),
    path('flight/add_new_customer/<int:flight_id>', views.add_new_customer, name='add_new_customer'),

#------------------------------ BASE FACADE ------------------------------------------   
    path('all_flights/', views.all_flights, name='all_flights'),
    path('get_flight_by_id/', views.get_flight_by_id, name='get_flight_by_id'),
    path('get_flights_by_parameters/', views.get_flights_by_parameters, name='get_flights_by_parameters'),
    path('all_airline_companies/', views.all_airlines, name='all_airline_companies'),
    path('get_airline_by_id/', views.get_airline_by_id, name='get_airline_by_id'),
    path('get_airline_by_param/', views.get_airline_by_param, name='get_airline_by_param'),
    path('all_countries/', views.all_countries, name='all_countries'),
    path('get_country_by_id/', views.get_country_by_id, name='get_country_by_id'),


#------------------------------ ADMIN FACADE ------------------------------------------   
    path('all_cust/', views.all_customers, name='all_customers'),
    path('add_airline/', views.add_airline_company, name='add_airline'),
    path('add_cust/', views.add_customer, name='add_customers'),
    path('add_admin/', views.add_admin, name='add_admin'),
    path('remove_airline/', views.remove_airline_company, name='remove_airline'),
    path('remove_customer/', views.remove_customer, name='remove_customer'),
    path('remove_admin/', views.remove_admin, name='remove_admin'),


#------------------------------ CUSTOMER FACADE ------------------------------------------   
    path('update_customer/', views.update_customer, name='update_customer'),
    path('add_ticket/', views.add_ticket, name='add_ticket'),
    path('remove_ticket/', views.remove_ticket, name='remove_ticket'),
    path('get_my_tickets/', views.get_my_tickets, name='get_my_tickets'),


#------------------------------ AIRLINE FACADE ------------------------------------------   
    path('update_airline_company/', views.update_airline_company, name='update_airline_company'),
    path('add_flight/', views.add_flight, name='add_flight'),
    path('update_flight/', views.update_flight, name='update_flight'),
    path('remove_flight/', views.remove_flight, name='remove_flight'),

#------------------------------ API ------------------------------------------
    path('api_base/', views.api_base, name='api_base'),
    path('api_admin/', views.api_admin, name='api_admin'),
    path('api_client/', views.api_client, name='api_client'),
    path('api_airline/', views.api_airline, name='api_airline'),

]