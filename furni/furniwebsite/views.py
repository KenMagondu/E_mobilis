from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages

# Create your views here.
def edit(request):
    return render(request,'edit.html',)

def index(request):
    return render(request,'index.html',)

def about(request):
    data=Student.objects.all()
    context={"data":data}
    return render(request,'about.html',context)

def insertData(request):
    data= Student.objects.all()
    context = {"data": data}
    if request.method == "Post":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        print(name,email,age,gender)
        query=Student(name=name, email=email, age=age,gender=gender)
        query.save()
        messages.error(request, "Data updated Successfully")
        return redirect("/")
    return render(request,'about.html',context)

def updateData(request,id):
    if request.method=="Post":
        name=request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']
        edit = Student.objects.get(id=id)

        edit.name=name
        edit.email=email
        edit.gender=gender
        edit.age=age
        edit.save()
        messages.warning(request,"Data updated successfully")

        return redirect("/")
    d=Student.objects.get(id=id)
    context={"d":d}
    return render(request,'edit.html',context)

def deleteData(request,id):
    d = Student.objects.get(id=id)
    d.delete()
    return redirect("/")


#def about(request):
#    return render(request,'about.html')

#def blog(request):
#    return render(request,'blog.html')

#def cart(request):
 #   return render(request,'cart.html')

#def checkout(request):
#    return render(request,'checkout.html')

#def contact(request):
#    return render(request,'contact.html')

#    return render(request,'services.html')

#def shop(request):
 #   return render(request,'shop.html')

#def thankyou(request):
#    return render(request,'thankyou.html')