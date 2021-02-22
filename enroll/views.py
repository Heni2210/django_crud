from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentDetails
from .models import User
# Create your views here.
def add_show(request): #add & show function
    if request.method == 'POST':
        fm = StudentDetails(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentDetails()
    else:
        fm = StudentDetails()
    stud = User.objects.all()
    return render(request, 'enroll/addshow.html', {'form':fm, 'stu':stud})


#delete function
def delete_data(request, id):
    if request.method == "POST":
        d = User.objects.get(pk=id)#pk = primary key
        d.delete()
    return HttpResponseRedirect('/')
    
#update function
def update_data(request,id):
    if request.method == "POST":
        u = User.objects.get(pk=id)
        fm = StudentDetails(request.POST, instance=u)
        if fm.is_valid():
            fm.save()
    else:
        u = User.objects.get(pk=id)
        fm = StudentDetails(instance=u)

    return render(request, 'enroll/update.html', {'form':fm})