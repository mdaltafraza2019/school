from django.shortcuts import render,redirect
from .forms import studentform
from .models import Student

# Create your views here.
def home(request):
    form=studentform(request.POST or None)
    data={
        "student":Student.objects.all(),
        "form":form
    }
    
    if request.method=="POST":

     if form.is_valid():
        form.save()
        return redirect(home)
    return render(request,'home.html',data)
def delete(request,id):
    data=Student.objects.get(pk=id)
    data.delete()
    return redirect(home)
def update(request,id):
   student=Student.objects.get(pk=id)
   form=studentform(request.POST or None,instance=student)
   if request.method=="POST":
    if form.is_valid():
        form.save()
        return redirect(home)
    
   return render(request,'update.html',{'form':form})

def searchstudent(request):
    if request.method=="GET":
        search_query=request.GET.get("search")
        form=studentform(request.POST or None)
        data={
            "student":Student.objects.filter(name__icontains=search_query),
            "form":form
        }
        return render(request,"home.html",data)
    return redirect(home)

def filtercity(request):
    if request.method=="GET":
        search=request.GET.get('city')
        form=studentform()
        data = {
              'form' : form,
              "student":Student.objects.filter(city=search)
        }
        return render(request,'home.html',data)
    return redirect(home)