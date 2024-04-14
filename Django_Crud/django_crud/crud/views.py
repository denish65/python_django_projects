from django.shortcuts import render,redirect
from .models import Student

# Create your views here.
def home(request):

    crud = Student.objects.all()
    return render(request,"home.html",{"crud":crud})


def crud_add(request):
    if request.method =="POST":
        crud_name=request.POST.get("name")
        crud_email=request.POST.get("email")
        crud_phone=request.POST.get("phone")
        crud_address=request.POST.get("address")


        s=Student()
        s.name=crud_name
        s.email=crud_email
        s.phone=crud_phone
        s.address=crud_address

        s.save()


    return redirect("/crud/home")

def crud_delete(request,id):
        s=Student.objects.get(pk=id)
        s.delete()
        return redirect("/crud/home")

def crud_edit(request,id):
    crud_edit=Student.objects.get(pk=id)
     
    return render(request,"edit.html",{"crud_edit":crud_edit})

def crud_update(request,id):

        crud_name=request.POST.get("name")
        crud_email=request.POST.get("email")
        crud_phone=request.POST.get("phone")
        crud_address=request.POST.get("address")

        s=Student.objects.get(pk=id)
        s.name=crud_name
        s.email=crud_email
        s.phone=crud_phone
        s.address=crud_address

        s.save()


        return redirect("/crud/home")

          