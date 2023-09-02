from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Doctor, Appointment

def home(request):
    appointments = Appointment.objects.all()
    return render(request, 'rdv/hom.html', {'appointments': appointments})

def add_appointment(request):
    if request.method == 'POST':
        doctor_id = request.POST['doctor']
        date = request.POST['date']
        time = request.POST['time']
        weight = request.POST['weight']
        notes = request.POST['notes']

        appointment = Appointment(doctor_id=doctor_id, date=date, time=time, weight=weight, notes=notes)
        appointment.save()

        return HttpResponseRedirect('/')

    doctors = Doctor.objects.all()
    return render(request, 'rdv/add_appointment.html', {'doctors': doctors})
