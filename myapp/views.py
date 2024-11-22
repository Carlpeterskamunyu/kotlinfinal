from django.shortcuts import render, redirect
from .models import Appointments
from .models import Contact
from django.http import HttpResponse
from myapp.forms import AppointmentsForm
def index(request):
    if request.method == 'POST':
        if Member.objects.filter(
                username=request.POST['username'],
                password=request.POST['password']
        ).exists():
            return render(request, 'index.html')  # Redirect to 'index.html' if valid credentials
        else:
            return render(request, 'index.html', {'error': 'Invalid username or password'})  # Error message if invalid credentials

    else:
        return render(request, 'index.html')  # Render the login page if it's a GET request


def service_details(request):
    return render(request, 'service-details.html')

def starter_page(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, 'about.html')

def doctors(request):
    return render(request, 'doctors.html')

def myservice(request):
    return render(request, 'myservice.html')

def make_appointment(request):
    if request.method == 'POST':
        # Get data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        datetime = request.POST.get('datetime')
        department = request.POST.get('department', 'Unassigned')
        doctor = request.POST.get('doctor')
        message = request.POST.get('message')

        # Check if datetime is provided
        if not datetime:
            return render(request, 'appointment.html', {'error': 'Please provide a valid datetime.'})

        # Create and save the appointment
        appointment = Appointments(
            name=name,
            email=email,
            phone=phone,
            datetime=datetime,
            department=department,
            doctor=doctor,
            message=message
        )
        appointment.save()

        return redirect('make_appointment')

    else:
        return render(request, 'appointment.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Check if all the required fields are present
        if not all([name, email, subject, message]):
            return HttpResponse('Missing fields', status=400)

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        return HttpResponse('Your message has been sent. Thank you!')

    return render(request, 'contact.html')
def show(request):
    allappointments = Appointments.objects.all()
    return render(request, 'show.html', {'Appointments': allappointments})

def delete(request,id):
    appoint=Appointments.objects.get(id=id)
    appoint.delete()
    return redirect('/show')
def edit(request, id):
    editappoint = Appointments.objects.get(id=id)
    return render(request, 'edit.html', {'appointment': editappoint})



def update(request, id):
    updateinfo = Appointments.objects.get(id=id)
    if request.method == "POST":
        form = AppointmentsForm(request.POST, instance=updateinfo)  # Use lowercase 'form'
        if form.is_valid():  # Check if form is valid before saving
            form.save()
            return redirect('/show')
    else:
        form = AppointmentsForm(instance=updateinfo)  # Initialize the form for GET requests
    return render(request, 'edit.html', {'form': form})  # Pass the form to the template
from .models import Member  # Ensure you import the Member model

def register(request):
    if request.method == 'POST':
        # Create a new Member instance and save it
        member = Member(
            name=request.POST['name'],
            username=request.POST['username'],
            password=request.POST['password']
        )
        member.save()  # Save the member to the database
        return redirect('/login')  # Redirect to the login page after successful registration
    else:
        return render(request, 'register.html')  # Corrected the template name syntax

def login(request):
    return render(request, 'login.html')