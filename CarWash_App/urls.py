from django.urls import path
from CarWash_App.views import *
from . import views

#We identify the urls of our views and assign them a name
urlpatterns = [
    path("", home, name="Home"),
    path("users", create_user, name= "Users"), #When the create_user function runs it will redirect us to the Users url
    path("employees", create_employees, name="Employees"), #When the create_employees function runs it will redirect us to the Employees url
    path("washing_prices", create_washing_prices, name="Prices"),
    path('Search/', views.search, name='Search'),
]
