from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from flight import models
from .serializers import UserRolesSerializer, UserSerializer, CountriesSerializer, AirlineSerializer, FlightSerializer, CustomerSerializer, TicketsSerializer, AdminSerializer

# ----------------------------- User Roles --------------------------------

@api_view(['GET'])
def get_role_data(request):
    roles = models.UserRoles.objects.all()
    serializer = UserRolesSerializer(roles, many=True) 
    return Response(serializer.data)

@api_view(['POST'])
def add_role(request):
    serializer = UserRolesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ----------------------------- User --------------------------------

@api_view(['GET'])
def get_user_data(request):
    users = models.CustomUser.objects.all()
    serializer = UserSerializer(users, many=True) 
    return Response(serializer.data)

@api_view(['POST'])
def add_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ----------------------------- Countries --------------------------------

@api_view(['GET'])
def get_country_data(request):
    countries = models.Countries.objects.all()
    serializer = CountriesSerializer(countries, many=True) 
    return Response(serializer.data)

@api_view(['GET'])
def get_country_by_id(request, pk):
    try:
        country = models.Countries.objects.get(id=pk)
    except models.Countries.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CountriesSerializer(country)
    return Response(serializer.data)

@api_view(['POST'])
def add_country(request):
    serializer = CountriesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ----------------------------- Airline --------------------------------

@api_view(['GET'])
def get_airline_data(request):
    airlines = models.AirlineCompanies.objects.all()
    serializer = AirlineSerializer(airlines, many=True) 
    return Response(serializer.data)

@api_view(['GET'])
def get_airline_by_id(request, pk):
    try:
        airline = models.AirlineCompanies.objects.get(id=pk)
    except models.AirlineCompanies().DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = AirlineSerializer(airline)
    return Response(serializer.data)

@api_view(['GET'])
def get_airline_by_params(request):
    try:
        name = request.GET.get('name', None)
        country_id = request.GET.get('country_id', None)
        if not name or not country_id:
            raise ValueError('Missing required query parameters')

        airline = models.AirlineCompanies.objects.get(name=name, country_id=country_id)
        serializer = AirlineSerializer(airline)
        return Response(serializer.data)

    except models.AirlineCompanies.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    except ValueError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def add_airline(request):
    serializer = AirlineSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_airline(request, pk):
    try:
        airline = models.AirlineCompanies.objects.get(id=pk)
    except models.AirlineCompanies.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AirlineSerializer(airline, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_airline(request, pk):
    try:
        airline = models.AirlineCompanies.objects.get(id=pk)
    except models.AirlineCompanies.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    airline.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------------------- Flight --------------------------------

@api_view(['GET'])
def get_flight_data(request):
    flights = models.Flights.objects.all()
    serializer = FlightSerializer(flights, many=True) 
    return Response(serializer.data)

@api_view(['GET'])
def get_flight_by_id(request, pk):
    try:
        flight = models.Flights.objects.get(id=pk)
    except models.Flights.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = FlightSerializer(flight)
    return Response(serializer.data)

@api_view(['GET'])
def get_flight_by_params(request):
    try:
        origin_country_id = request.GET.get('origin_country_id', None)
        destination_country_id = request.GET.get('destination_country_id', None)
        departure_time = request.GET.get('departure_time', None)
        landing_time = request.GET.get('landing_time', None)
        if not origin_country_id or not destination_country_id or not departure_time or not landing_time:
            raise ValueError('Missing required query parameters')

        flight = models.Flights.objects.get(
            origin_country_id=origin_country_id,
            destination_country_id=destination_country_id,
            departure_time=departure_time,
            landing_time=landing_time
        )
        serializer = FlightSerializer(flight)
        return Response(serializer.data)

    except models.Flights.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    except ValueError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def add_flight(request):
    serializer = FlightSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_flight(request, pk):
    try:
        flight = models.Flights.objects.get(id=pk)
    except models.Flights.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = FlightSerializer(flight, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_flight(request, pk):
    try:
        flight = models.Flights.objects.get(id=pk)
    except models.Flights.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    flight.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# ----------------------------- Customer --------------------------------

@api_view(['GET'])
def get_customer_data(request):
    customers = models.Customers.objects.all()
    serializer = CustomerSerializer(customers, many=True) 
    return Response(serializer.data)

@api_view(['GET'])
def get_customer_by_id(request, pk):
    try:
        customer = models.Customers.objects.get(id=pk)
    except models.Customers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CustomerSerializer(customer)
    return Response(serializer.data)

@api_view(['POST'])
def add_customer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_customer(request, pk):
    try:
        customer = models.Customers.objects.get(id=pk)
    except models.Customers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CustomerSerializer(customer, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_customer(request, pk):
    try:
        customer = models.Customers.objects.get(id=pk)
    except models.Customers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    customer.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# ----------------------------- Tickets --------------------------------

@api_view(['GET'])
def get_tickets_data(request):
    tickets = models.Tickets.objects.all()
    serializer = TicketsSerializer(tickets, many=True) 
    return Response(serializer.data)

@api_view(['POST'])
def add_ticket(request):
    serializer = TicketsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_tickets(request, pk):
    try:
        ticket = models.Tickets.objects.get(id=pk)
    except models.Tickets.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    ticket.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# ----------------------------- Admin --------------------------------

@api_view(['GET'])
def get_admin_data(request):
    admins = models.Adminstrators.objects.all()
    serializer = AdminSerializer(admins, many=True) 
    return Response(serializer.data)

@api_view(['POST'])
def add_admin(request):
    serializer = AdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_admin(request, pk):
    try:
        admin = models.Adminstrators.objects.get(id=pk)
    except models.Adminstrators.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    admin.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)