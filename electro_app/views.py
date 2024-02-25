from django.shortcuts import render, redirect
from electro_app.forms import customer_request_form,register_form
from electro_app.models import customer_request,customer_message,subscriber,review
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
    #create api for contact
    #display the reviews in index page
    return render(request, 'index.html')

def bookings(request):
    #create api for booking form
    form = customer_request_form(request.POST)
    if form.is_valid():
        update=form.save(commit=False)
        update.connect=request.user
        update.save()
        return redirect('/appointment')

    return render(request, 'bookings.html', {'form':form})

def appointment(request):
    #create api for displaying appointments/bookings
    form = customer_request.objects.filter(connect=request.user)
    return render(request, 'appointment.html',{'form':form})

def logins(request):
    #create api for login user
    if request.method == "POST":
        username = request.POST['names']
        password = request.POST['pass']
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
    return render(request, 'logins.html')

def regs(request):
    #create api for registering user
    form=register_form(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'reg.html',{'form':form})

def show(request, ID):
    #create api for displaying each appointment in details
    form=customer_request.objects.get(pk=ID)
    return render(request, 'show.html',{'show':form})

def delete_items(request, ID):
    #create api for deleting booking items
    form=customer_request.objects.get(pk=ID)
    form.delete()
    return redirect('/appointment')

def logoutuser(request):
    return redirect('/')

def reviews(request):
    #create api for review form which is in index page
    return redirect('/')
    
def delete_reviews(request, ID):
    #create api for deleting reviews
    return redirect('/')

def subscrib(request):
    #create api for subscrib form which is in index page
    return redirect('/')