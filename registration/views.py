from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from registration.models import student

def registration(request):
    return  HttpResponse('Welcome to registration!')

def mypage(request):
    template = loader.get_template('records.html')
    return HttpResponse(template.render())

def records(request):
    data = student.objects.all();
    context = {'data': data}
    return render(request, 'records.html' ,context)


@csrf_exempt
def addstudent(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        age = request.POST.get('age')

        stud={'firstname':firstname,'lastname':lastname,'email':email,'age':age}
        print(stud)

        obj1 = student(firstname=firstname, lastname=lastname, email=email, age=age)
        obj1.save()

        data = student.objects.all()
        context = {'data':data}
        return render(request, 'records.html', context)

def editstudent(request, id):
    data = student.objects.get(id=id)
    context = {'data': data}
    return render(request, 'updatestudent.html', context)

def updatestudent(request, id):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        age = request.POST.get('age')

        editstudent = student.objects.get(id=id)
        editstudent.firstname = firstname
        editstudent.lastname = lastname
        editstudent.email = email
        editstudent.age = age
        editstudent.save()
    return redirect('/')

def deletestudent(request, id):
    deletestudent = student.objects.get(id=id)
    deletestudent.delete()
    return redirect('/')





