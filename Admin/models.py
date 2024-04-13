from django.db import models

# Create your models here.

class tbl_type(models.Model):
   type_name=models.CharField(max_length=50)
class tbl_district(models.Model):
    district_name = models.CharField(max_length=50)
class tbl_Place(models.Model):
     Place_name=models.CharField(max_length=50)
     district = models.ForeignKey(tbl_district,on_delete=models.CASCADE)
class tbl_Course(models.Model):
     Course_name=models.CharField(max_length=50)