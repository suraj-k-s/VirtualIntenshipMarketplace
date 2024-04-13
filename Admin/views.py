from django.shortcuts import render,redirect
from Admin.models import *
# Create your views here.
def Home(request):
    return render(request,"Admin/Homepage.html")
    
def Type_Insert_Select(request):
    if request.method == "POST":
        tbl_type.objects.create(type_name=request.POST.get("type_name"))
        return render(request,"Admin/Type.html")
    else:
        return render(request,"Admin/Type.html")
    
def District_Insert_Select(request):
    districtdata=tbl_district.objects.all()
    if request.method == "POST":
        tbl_district.objects.create(district_name=request.POST.get("txt_district"))
        return render(request,"Admin/District.html",{"data":districtdata})
    else:
        return render(request,"Admin/District.html",{"data":districtdata})
    
def DeleteDistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("webadmin:District_Insert_Select")
    
def Place_Insert_Select(request):
    Placedata=tbl_Place.objects.all()
    district = tbl_district.objects.all()
    if request.method == "POST":
        dis = tbl_district.objects.get(id=request.POST.get("district"))
        tbl_Place.objects.create(Place_name=request.POST.get("PlaceName"),district=dis)
        return render(request,"Admin/Place.html",{"data":Placedata,"districtdata":district})
    else:
        return render(request,"Admin/place.html",{"data":Placedata,"districtdata":district})
    
def DeletePlace(request,did):
    tbl_Place.objects.get(id=did).delete()
    return redirect("webadmin:Place_Insert_Select")    
    
def Course_Insert_Select(request):
    Coursedata=tbl_Course.objects.all()
    if request.method == "POST":
        tbl_Course.objects.create(Course_name=request.POST.get("course_name"))
        return render(request,"Admin/Course.html",{"data":Coursedata})
    else:
        return render(request,"Admin/Course.html",{"data":Coursedata})
    
def DeleteCourse(request,did):
    tbl_Course.objects.get(id=did).delete()
    return redirect("webadmin:Course_Insert_Select")

def EditDistrict(request,did):
    dis = tbl_district.objects.get(id=did)
    if request.method == "POST":
        dis.district_name = request.POST.get("txt_district")
        dis.save()
        return redirect("webadmin:District_Insert_Select")
    else:
        return render(request,"Admin/District.html",{"dis":dis})
    
def EditPlace(request,did):
    district = tbl_district.objects.all()
    dis = tbl_Place.objects.get(id=did)
    if request.method == "POST":
        dis.Place_name = request.POST.get("PlaceName")
        dist = tbl_district.objects.get(id=request.POST.get("district"))
        dis.district = dist
        dis.save()
        return redirect("webadmin:Place_Insert_Select")
    else:
        return render(request,"Admin/Place.html",{"dis":dis,"districtdata":district})
    
def EditCourse(request,did):
    dis = tbl_Course.objects.get(id=did)
    if request.method == "POST":
        dis.Course_name = request.POST.get("course_name")
        dis.save()
        return redirect("webadmin:Course_Insert_Select")
    else:
        return render(request,"Admin/Course.html",{"dis":dis})