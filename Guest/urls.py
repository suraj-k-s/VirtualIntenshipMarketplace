from django.urls import path 
from Guest import views
app_name = "webguest"
urlpatterns = [
 path('Company/',views.Company_Insert_Select,name="Company_Insert_Select"),
 path('User/',views.User_Insert_Select,name="User_Insert_Select"),
 path('ajaxplace/',views.ajaxplace,name="ajaxplace"),
 path('Login/',views.Login_Insert_Select,name="Login_Insert_Select"),
 path('',views.Home,name="Home"),
]