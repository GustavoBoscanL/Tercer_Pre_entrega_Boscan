from django.urls import path
from CarWash_App.views import *
from . import views
from .views import user_create, user_update, UserListView

#We identify the urls of our views and assign them a name
urlpatterns = [
    #HOMEPAGE
    path("", home, name="Home"),
    
    #USERS
    path('user/create/', user_create.as_view(), name='Users'),
    path('users/list/', UserListView.as_view(), name='UserList'),
    path('user/<int:pk>/update/', user_update.as_view(), name='UserUpdate'),
    path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='UserDelete'),
    
    
    #EMPLOYEES
    path("employees", create_employees, name="Employees"), #When the create_employees function runs it will redirect us to the Employees url
    
    
    #PRICES
    path("washing_prices", create_washing_prices, name="Prices"),
    path('Search/', views.search, name='Search'),
]
