from django.shortcuts import render, HttpResponse
from .models import User
import json



# Create your views here.



def create_user_info(request):

    request_data = json.loads(request.body.decode('utf-8'))

    user_data = {"first_name": request_data['first_name'],
                 "last_name": request_data['last_name'],
                 "address": request_data['address'],
                 "city": request_data['city'],
                 "state": request_data['state']}



    User(**user_data).save()

    return HttpResponse(request)

