import json
from datetime import datetime
from decimal import getcontext, Decimal

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from main.models import Income, Expense

def create_object(raw_payload, obj):
    payload = json.loads(raw_payload.decode("utf-8"))

    getcontext().prec = 2
    payload["amount"] = Decimal(payload["amount"])
    payload["when"] = datetime.strptime(payload["when"], "%Y-%m-%dT%H:%M:%S%z")

    #payload.update({"name": "elo", "description": "blE"})
    print(payload)

    # create object and save
    o = obj(**payload) 
    o.save()

@csrf_exempt
def add_expense(request):
    if request.method == "POST":
        create_object(request.body, Expense)
        return HttpResponse("Created", status=201)

@csrf_exempt
def add_income(request):
    if request.method == "POST":
        create_object(request.body, Income)
        return HttpResponse("Created", status=201)

def show(request, timeframe_start, timeframe_end):
    # convert dates from string to dates

    # query data

    # return json
    return HttpResponse("Hello, world. {} {}.".format(timeframe_start, timeframe_end))
