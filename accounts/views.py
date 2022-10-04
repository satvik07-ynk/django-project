from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import RegistrationForm
from django.shortcuts import render
import random as rd
import numpy as np
import csv
import matplotlib.pyplot as plt
import pandas as pd
from django.http import HttpRequest
import subprocess as sp

class Home(TemplateView):
    template_name = "home.html"


class SignUpView(CreateView):
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    form_class = RegistrationForm
    success_message = "Your profile was created successfully"

def Equipments(request):
    return render(request,'Equipments.html')


def test(request):
    print("Hello")
    start_value= int(request.POST.get('r1') or 1)
    end_value= int(request.POST.get('r2')or 1)
    no_step= int(request.POST.get('nv')or 1) 
    #return render(request,'test.html')
#     st2 = int (r2)
#     st3 = int (nv)
    val=abs(start_value) + abs(end_value)
    stepsize = val/no_step
    print(start_value)
    #print(stepsize)
    vals={}#Empty dictionary for values
                                        ##-----CSV FILE-----
    path=open("Readings(x,y).csv","w")#open csv file

    for i in np.arange(start_value,end_value+stepsize,stepsize):
        output = rd.random()
        vals[i]=output
#print(vals)

    z=csv.writer(path)
    for x,y in vals.items():#write data into csv file
        z.writerow([x,y])

    path.close()
    df = pd.read_csv('Readings(x,y).csv', header=None)
    df.rename(columns={0: 'X', 1: 'Y'}, inplace=True)#header names
    df.to_csv('Readings(x,y).csv', index=False)
                                    #----PLOTTING----
    # plt.rcParams["figure.figsize"] = [7.00, 3.50]
    # plt.rcParams["figure.autolayout"] = True
    columns = ["X", "Y"]
    df = pd.read_csv("Readings(x,y).csv", usecols=columns)
    print("Contents in csv file:\n", df)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Random Generated Graph")
    plt.plot(df.X, df.Y)
    plt.savefig('RGG.png')  
    plt.show()

    submitbutton= request.POST.get('Submit')
    
    context= {'Start': start_value, 'Stop':end_value,
              'number': no_step,
            #    'state': state,
              'submitbutton': submitbutton}
        
    return render(request, 'test.html', context)
# 	response = HttpResponse(content_type='text/csv')
# 	response['Content-Disposition'] = 'attachment; filename=venues.csv'
	
# 	# Create a csv writer
# 	writer = csv.writer(response)

# 	# Designate The Model
# 	# venues = Venue.objects.all()

# 	# Add column headings to the csv file
# 	writer.writerow(['Venue Name', 'Address', 'Zip Code', 'Phone', 'Web Address', 'Email'])
#     return render(request)

	# Loop Thu and output
	# for venue in venues:
		# writer.writerow([venue.name, venue.address, venue.zip_code, venue.phone])

# def Measurements(request):
#     r1=int(input('Enter starting point'))
#     r2=int(input('Enter ending point'))
#     nv=float(input("Enter the number of values"))
#     val=abs(r1)+abs(r2)
#     stepsize=val/nv;
#     vals={}#Empty dictionary for values
#                                         ##-----CSV FILE-----
#     path=open("Readings(x,y).csv","w")#open csv file

#     for i in np.arange(r1,r2+stepsize,stepsize):
#         output = rd.random()
#         vals[i]=output
# #print(vals)

#     z=csv.writer(path)
#     for x,y in vals.items():#write data into csv file
#         z.writerow([x,y])

#     path.close()
#     df = pd.read_csv('Readings(x,y).csv', header=None)
#     df.rename(columns={0: 'X', 1: 'Y'}, inplace=True)#header names
#     df.to_csv('Readings(x,y).csv', index=False)
#                                     #----PLOTTING----
#     # plt.rcParams["figure.figsize"] = [7.00, 3.50]
#     # plt.rcParams["figure.autolayout"] = True
#     columns = ["X", "Y"]
#     df = pd.read_csv("Readings(x,y).csv", usecols=columns)
#     print("Contents in csv file:\n", df)
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.title("Random Generated Graph")
#     plt.plot(df.X, df.Y)
#     plt.savefig('RGG.png')  
    # plt.show()

# def basic(request):

#     if request.method =='POST':
#         name = request.POST.get('start','')
#         print(name)
#         return HTTPResponse("hello")
    # else:
    #     return render(request,'basic.html')

def Basics():
    r1=int(input('Enter starting point'))
    r2=int(input('Enter ending point'))
    nv=float(input("Enter the number of values"))
    val=abs(r1)+abs(r2)
    stepsize=val/nv;
    vals={}#Empty dictionary for values
                                        ##-----CSV FILE-----
    path=open("Readings(x,y).csv","w")#open csv file

    for i in np.arange(r1,r2+stepsize,stepsize):
        output = rd.random()
        vals[i]=output
#print(vals)

    z=csv.writer(path)
    for x,y in vals.items():#write data into csv file
        z.writerow([x,y])

    path.close()
    df = pd.read_csv('Readings(x,y).csv', header=None)
    df.rename(columns={0: 'X', 1: 'Y'}, inplace=True)#header names
    df.to_csv('Readings(x,y).csv', index=False)
                                    #----PLOTTING----
    # plt.rcParams["figure.figsize"] = [7.00, 3.50]
    # plt.rcParams["figure.autolayout"] = True
    columns = ["X", "Y"]
    df = pd.read_csv("Readings(x,y).csv", usecols=columns)
    print("Contents in csv file:\n", df)
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.title("Random Generated Graph")
    # plt.plot(df.X, df.Y)
    # plt.savefig('RGG.png') 

def Measurements(request):
    if request.POST:
        context = {}
        reader=csv.DictReader((request.FILES['file']))
        for row in reader:
            header = list(row.keys())
            break
        data = {}
        for row in reader:
            for i in header:
                values = []
                values.append(row.get(i))
                if i not in data:
                    data[i] = values
                data[i].extend(values)
        context['header'] = header
        context['data'] = data
        return render(request, 'Measurements.html', context)
    return(render(request, 'Measurements.html'))




