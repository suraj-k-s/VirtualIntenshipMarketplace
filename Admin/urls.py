from django.urls import path 
from Admin import views
app_name="webadmin"
urlpatterns = [
 path('Home/',views.Home,name="Home"),
 path('Type/',views.Type_Insert_Select,name="Type_Insert_Select"),
 path('District/',views.District_Insert_Select,name="District_Insert_Select"),
 path('deletedistrict/<int:did>',views.DeleteDistrict,name="DistrictDelete"),
 path('editdistrict/<int:did>',views.EditDistrict,name="DistrictEdit"),
 path('Place/',views.Place_Insert_Select,name="Place_Insert_Select"),
 path('editplace/<int:did>',views.EditPlace,name="PlaceEdit"),
 path('deleteplace/<int:did>',views.DeletePlace,name="PlaceDelete"),
 path('Course/',views.Course_Insert_Select,name="Course_Insert_Select"),
 path('deletecourse/<int:did>',views.DeleteCourse,name="CourseDelete"),
 path('editcourse/<int:did>',views.EditCourse,name="CourseEdit"),
]