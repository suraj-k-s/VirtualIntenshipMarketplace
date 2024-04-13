from django.urls import path 
from Company import views
app_name = "webcompany"
urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('myprofile',views.myprofile,name="myprofile"),
    path('intenship',views.Intenship_Insert_Select,name="Intenship_Insert_Select"),
    # path('DeleteIntenship/<int:did>',views.DeleteIntenship,name="IntenshipDelete"),
    ] 
     