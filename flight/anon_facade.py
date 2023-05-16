from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

from .login_form import CustomUserCreationForm
from .cust_dal import CustomerDal
from .user_dal import UsersDal




class AnonymousFacade():

    def log_in(request):
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = UsersDal.get_user_by_username(username)
                if user is not None:
                    login(request, user)
                    user_role = user.user_role
                    if user_role.role_name == 'admin':
                        return redirect('admin_home')
                    elif user_role.role_name == 'client':
                        return redirect('client_home')
                    elif user_role.role_name == 'airline company':
                        return redirect('airline_home')
                else:
                    form.add_error(None, 'Invalid username or password')
        else:
            form = AuthenticationForm()
        return render(request, 'flight/login.html', {'form': form})


    def register(request):
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                password = form.cleaned_data.get('password1')
                user.set_password(password)
                user.save()
                login(request, user)
                user_role = form.cleaned_data.get('user_role')
                if user_role.role_name == 'admin':
                    return redirect('admin_home')
                elif user_role.role_name == 'client':
                    return redirect('client_home')
                elif user_role.role_name == 'airline company':
                    return redirect('airline_home')
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field}: {error}")
        else:
            form = CustomUserCreationForm()
        return render(request, 'flight/regist.html', {'form': form})

    def add_customer(first_name, last_name, address, phone_number, credit_card_number, user_id):
        CustomerDal.add_customer(first_name, last_name, address, phone_number, credit_card_number, user_id)
