from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import user_form, employees_form, washing_price_form
from CarWash_App.models import User, Employees, Washing_prices

def home(request): #home page
    return render(request, "CarWash_App/home.html")

def users(request): #user page
    return render(request, "CarWash_App/users.html")

def employees(request): #employyes page 
    return render(request, "CarWash_App/employees.html")

def whashing_prices(request): #Prices page
    return render(request, "CarWash_App/washing_prices.html")


#We make the form to create the users
def create_user(request): 

    if request.method == "POST":

        form_user = user_form(request.POST)

        if form_user.is_valid():

            form_user.save()
        
            return redirect("Users")
         
    else:
        form_user = user_form()


    return render(request, 'CarWash_App/users.html', {'form': form_user})

#We make the form to create the employees
def create_employees(request): 

    if request.method == "POST":

        form_employees = employees_form(request.POST)

        if form_employees.is_valid():

            form_employees.save()
        
            return redirect("Employees")
         
    else:
        form_employees = employees_form()


    return render(request, 'CarWash_App/employees.html', {'form': form_employees})

#We make the form to create the Prices
def create_washing_prices(request): 

    if request.method == "POST":

        form_washing_prices = washing_price_form(request.POST)

        if form_washing_prices.is_valid():

            form_washing_prices.save()
        
            return redirect("Prices")
         
    else:
        form_washing_prices = washing_price_form()


    return render(request, 'CarWash_App/washing_prices.html', {'form': form_washing_prices})

#Now we are going to create a function to search the information in our database

def search(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')
        users = User.objects.filter(name__icontains=query)
        employees = Employees.objects.filter(name__icontains=query)
        prices = Washing_prices.objects.filter(car_type__icontains=query)
        
        return render(request, 'CarWash_App/show_search.html', {
            'query': query,
            'users': users,
            'employees': employees,
            'prices': prices,
        })
    return render(request, 'CarWash_App/show_search.html',)
