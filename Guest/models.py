from django.db import models
from Admin.models import *
# Create your models here.
#class tbl_Company(models.Model):
   #company_photo=models.FileField(upload_to='Company_photo/')

#class tbl_User(models.Model):
   #user_photo = models.FileField(upload_to='User_photo/')

class tbl_Company(models.Model):
   company_name=models.CharField(max_length=50)
   company_contact=models.CharField(max_length=12)
   company_email=models.CharField(max_length=50)
   company_address=models.CharField(max_length=50)
   place=models.ForeignKey(tbl_Place,on_delete=models.CASCADE,null=True)
   company_proof = models.FileField(upload_to='User_proof/')
   company_photo = models.FileField(upload_to='User_photo/')
   company_password=models.CharField(max_length=50)


class tbl_User(models.Model):
   user_name=models.CharField(max_length=50)
   user_contact=models.CharField(max_length=12)
   user_email=models.CharField(max_length=50)
   user_address=models.CharField(max_length=50)
   place=models.ForeignKey(tbl_Place,on_delete=models.CASCADE,null=True)
   user_proof = models.FileField(upload_to='User_proof/')
   user_photo = models.FileField(upload_to='User_photo/')
   user_password=models.CharField(max_length=50)


