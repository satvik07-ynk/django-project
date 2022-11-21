from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

#--------------- HOME PAGE---------------------
def home(request):
    return render(request, 'measurements/home.html')

#----------------Measurement Page------------------

def measurement_iv(request):
    return render(request, 'measurements/analysis_i-v.html')

def measurement_stransient(request):
    # list all equipments which can provide measurement
    equipments_list = models.Equipment_Type.objects.filter(equipment_type='both') | models.Equipment_Type.objects.filter(equipment_type='measurement')
    return  render(request, 'measurements/analysis_transient_simple.html',
                   {'equipments_list': equipments_list}
                   )

def measurement_otransient(request):
    return render(request, 'measurements/analysis_transient_optical.html')

#-----------------------------Running measurement------------------------
def run_transient_measurement(request):
    equipment = request.POST.get('equipments')
    y_axis = request.POST.get('parameter')
    sampling_rate = request.POST.get('range_value')

    # obtained equipment to be used for analysis Equipment_Detail
    # obtained y_axis value from the parameter list of equipment Equipment_Parameter

    print(equipment)
    print(y_axis)
    print(sampling_rate)
    return render(request, 'measurements/analysis_transient_simple.html')


#------------------Handling hx-requests-----------------------------------
def hx_parameters(request):
    equipment = request.POST.get('equipments')
    if equipment != 'Select Instrument From The list':
        # first obtaning details from Equipment type using primary key details
        device_name = models.Equipment_Type.objects.get(pk = equipment)
        # second finding parameters in parameter table using equipment name.
        list_of_parameters = models.Equipment_Parameter.objects.filter(name = device_name.name)
    else:
        list_of_parameters = "No parameters to check"

    return render(request, 'measurements/partials/transient_simple_parameters.html',
                  {'equipment': equipment,
                  'list_of_parameters': list_of_parameters
                   })
