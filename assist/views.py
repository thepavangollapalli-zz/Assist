from django.views.generic.base import View
from django.shortcuts import render
from django.http import *
from backend.models import *
from django.core import serializers
from django.utils import timezone
import datetime
import copy
import csv
from django.views.decorators.csrf import csrf_exempt

class HomePageView(View):#inherits from View to override specific things
    def get(self, request): #this is called when client makes a get request to homepage
        all_vets = Veteran.objects.all() #returns all queues as list 
        vet_data = []
        for v in all_vets:
            v_obj = {}
            v_obj["name"] = v.name
            v_obj["gender"] = v.gender
            v_obj["age"] = v.age
            v_obj["bday"] = v.bday
            # v_obj["ssn"] = v.ssn
            v_obj["problem"] = v.problem
            v_obj["time"] = v.time
            vet_data.append(v_obj)
        context = {}
        context["vet_data"] = vet_data
        return render(request, 'homepage.html', context) #returns render(a template) of the homepage
    
    # def post(self, request):
    #     post_data = dict(request.POST)
    #     v_name = post_data["name"][0]
    #     v_gender = post_data["gender"][0]
    #     v_bday = post_data["bday"][0]
    #     v_ssn = post_data["ssn"][0]
    #     v_age = post_data["age"][0]
    #     v_problem = post_data["problem"][0]
    #     # checks to see if veteran already in database
    #     vets = Veteran.objects.all()
    #     updated = False
    #     for v in vets:
    #         if(v_name==v.name):
    #             updated = True
    #             v.gender = v_gender
    #             v.age = v_age
    #             v.ssn = v_ssn
    #             v.bday = v_bday
    #             v.problem = v_problem
    #             v.time = v.time
    #             v.save()
    #             break
    #     if(not updated):
    #         v_entry = Veteran(name=v_name, gender=v_gender, age=v_age, bday=v_bday, ssn=v_ssn, problem=v_problem)
    #         v_entry.save()
    #     return HttpResponseRedirect("/")

@csrf_exempt
def post(request):
    post_data = dict(request.POST)
    print(post_data)
    v_name = post_data["name"][0]
    v_gender = post_data["gender"][0]
    v_bday = post_data["bday"][0]
    # v_ssn = post_data["ssn"][0]
    v_age = post_data["age"][0]
    v_problem = post_data["problem"][0]
    # checks to see if veteran already in database
    vets = Veteran.objects.all()
    updated = False
    for v in vets:
        if(v_name==v.name):
            updated = True
            v.gender = v_gender
            v.age = v_age
            # v.ssn = v_ssn
            v.bday = v_bday
            v.problem = v_problem
            v.time = v.time
            v.save()
            break
    if(not updated):
        v_entry = Veteran(name=v_name, gender=v_gender, age=v_age, bday=v_bday, problem=v_problem, time=timezone.now() - datetime.timedelta(hours = 5))
        v_entry.save()
    return HttpResponseRedirect("/")

class UpdateFormView(View):
    def get(self, request):
        return render(request, 'updateform.html')

class VeteranAPIView(View):
    def get(self, request):
        vets = Veteran.objects.all()
        now = timezone.now()
        #calculate scores as an array
        # scores=dict()#[None for i in range(len(vets))]
        for i in vets:
            delta = now - i.time - datetime.timedelta(hours=5) #datetime.datetime.now()
            d = delta.total_seconds()//60
            if(i.problem=="Depression"):
                d+=25
            elif(i.problem=="Anxiety"):
                d+=16
            elif(i.problem=="Injury"):
                d+=9
            else:
                d+=4
            i.score = d
            # scores[i.name] = d
            i.save()
        data = serializers.serialize('json', vets)
        return HttpResponse(data, content_type='application/json')

class GenerateCSVView(View):
    def get(self, request):
        response = HttpResponse(content_type="text/csv")
        response['Content-Disposition'] = 'attachment; filename="appointment_order.csv"'
        # backup = copy.deepcopy(Veteran.objects.all())
        vets = Veteran.objects.all()
        now = timezone.now()
        #calculate scores as an array
        # scores=dict()#[None for i in range(len(vets))]
        for i in vets:
            delta = now - i.time - datetime.timedelta(hours=5) #datetime.datetime.now()
            d = delta.total_seconds()//60
            if(i.problem=="Depression"):
                d+=25
            elif(i.problem=="Anxiety"):
                d+=16
            elif(i.problem=="Injury"):
                d+=9
            else:
                d+=4
            i.score = d
            # scores[i.name] = d
            i.save()
            # print(i.score)
        # print(vets)
        writer = csv.writer(response)
        writer.writerow(['Name', 'Gender', 'Age', 'Birthday', 'Problem', 'Time', 'Score'])
        # writer.writerow([scores])
        # print()
        # while(len(vets)>1):
        #     lowest = max(scores, key=scores.get)
        #     vet = vets.pop(lowest)
        #     # delta = vet.time-now #datetime.datetime.now()
        #     # writer.writerow([delta.seconds//3600, "minutes"])
        #     writer.writerow([vet.name, vet.gender, vet.age, vet.bday, vet.problem, vet.time])
        # vets = vets.order_by('score')
        for vet in vets:
            # print(vet.score)
            writer.writerow([vet.name, vet.gender, vet.age, vet.bday, vet.problem, vet.time, vet.score])
        # while(len(vets)>0):
        #     vet = None
        #     min_value = 1000000
        #     for v in vets:
        #         print(v.score)
        #         if(v.score < min_value):
        #             print("yes")
        #             min_value = v.score
        #             vet = v
        #             print(vet)
        #     writer.writerow([vet.name, vet.gender, vet.age, vet.bday, vet.problem, vet.time, vet.score])
        #     if(vet != None):
        #         vet.delete()
        # vets  = backup
        return response

    