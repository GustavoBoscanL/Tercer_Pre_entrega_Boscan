from django.urls import path
from CarWash_App.views import *
from . import views
from .views import user_create, user_update

#We identify the urls of our views and assign them a name
urlpatterns = [
    path("", home, name="Home"),
    #path("users", create_user, name= "Users"), #When the create_user function runs it will redirect us to the Users url
    path('user/create/', user_create.as_view(), name='Users'),
    path('user/<int:pk>/update/', user_update.as_view(), name='UsersUpdate'),
    path("employees", create_employees, name="Employees"), #When the create_employees function runs it will redirect us to the Employees url
    path("washing_prices", create_washing_prices, name="Prices"),
    path('Search/', views.search, name='Search'),
]
