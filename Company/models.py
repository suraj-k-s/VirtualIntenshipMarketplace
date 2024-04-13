from django.db import models
from Admin.models import *
from Guest.models import *


# Create your models here.
#class tbl_Changepassword(models.Model):
 #  changepassword_name=models.CharField(max_length=50)

class tbl_Intenship(models.Model):
   Intenship_duration=models.CharField(max_length=50)
   Intenship_details=models.CharField(max_length=50)
   Intenship_poster=models.FileField(upload_to='Company_photo/')
   Company=models.ForeignKey(tbl_Company,on_delete=models.CASCADE,null=True)

   

