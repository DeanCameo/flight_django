from django.urls import path
from . import views

urlpatterns = [
    path('get_role_data/', views.get_role_data, name='get_role_data'),                            # TO DO
    path('add_role/', views.add_role, name='add_role'),                                           # TO DO

    path('get_user_data/', views.get_user_data, name='get_user_data'),                            # TO DO
    path('add_user/', views.add_user, name='add_user'),                                           # TO DO 

    path('get_country_data/', views.get_country_data, name='get_country_data'),                                # DID
    path('get_country_data/<int:pk>/', views.get_country_by_id, name='get_country_by_id'),                     # DID
    path('add_country/', views.add_country, name='add_country'),                                  # TO DO

    path('get_airline_data/', views.get_airline_data, name='get_airline_data'),                                # DID
    path('get_airline_data/<int:pk>/', views.get_airline_by_id, name='get_airline_by_id'),                     # DID
    path('get_airline_data/params/', views.get_airline_by_params, name='get_airline_by_params'),               # DID
    path('add_airline/', views.add_airline, name='add_airline'),                                               # DID
    path('update_airline/<int:pk>/', views.update_airline, name='update_airline'),                             # DID
    path('delete_airline/<int:pk>/', views.delete_airline, name='delete_airline'),                             # DID

    path('get_flight_data/', views.get_flight_data, name='get_flight_data'),                                   # DID
    path('get_flight_data/<int:pk>/', views.get_flight_by_id, name='get_flight_by_id'),                        # DID
    path('get_flight_data/params/', views.get_flight_by_params, name='get_flight_by_params'),                  # DID
    path('add_flight/', views.add_flight, name='add_flight'),                                                  # DID
    path('update_flight/<int:pk>/', views.update_flight, name='update_flight'),                                # DID
    path('delete_flight/<int:pk>/', views.delete_flight, name='delete_flight'),                                # DID

    path('get_customer_data/', views.get_customer_data, name='get_customer_data'),                             # DID
    path('get_customer_data/<int:pk>/', views.get_customer_by_id, name='get_customer_by_id'),     # TO DO      
    path('add_customer/', views.add_customer, name='add_customer'),                                            # DID
    path('update_customer/<int:pk>/', views.update_customer, name='update_customer'),                          # DID             
    path('delete_customer/<int:pk>/', views.delete_customer, name='delete_customer'),                          # DID

    path('get_tickets_data/', views.get_tickets_data, name='get_tickets_data'),                                # DID
    path('add_ticket/', views.add_ticket, name='add_ticket'),                                                  # DID
    path('delete_tickets/<int:pk>/', views.delete_tickets, name='delete_tickets'),                             # DID

    path('get_admin_data/', views.get_admin_data, name='get_admin_data'),                         # TO DO
    path('add_admin/', views.add_admin, name='add_admin'),                                                     # DID
    path('delete_admin/<int:pk>/', views.delete_admin, name='delete_admin'),                               # TO DO

]