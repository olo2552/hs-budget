import json
from datetime import datetime
from decimal import getcontext, Decimal

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from main.models import Income, Expense


def parse_datetime_string(datetime_string):
    return datetime.strptime(datetime_string, "%Y-%m-%dT%H:%M:%S%z")


def format_datetime(dt):
    return datetime.strftime(dt, "%Y-%m-%dT%H:%M:%S%z")


def create_object(raw_payload, obj_cls):
    payload = json.loads(raw_payload.decode("utf-8"))

    getcontext().prec = 2
    payload["amount"] = Decimal(payload["amount"])
    payload["when"] = parse_datetime_string(payload["when"])

    # create object and save
    o = obj_cls(**payload)
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


def show(request, raw_timeframe_start, raw_timeframe_end):
    try:
        timeframe_start, timeframe_end = map(parse_datetime_string, (raw_timeframe_start, raw_timeframe_end))
    except ValueError:
        return HttpResponse("""Those are not the droids you're looking for
        but really..., one of your timeframe boundaries is malformed""", status=404)

    def get_objects_within_timeframe(obj_cls):
        return obj_cls.objects.all().filter(when__gte=timeframe_start, when__lte=timeframe_end)

    def serialize(obj):
        return obj.to_json()

    def serialize_objects(objects):
        return list(map(serialize, objects))

    expenses = serialize_objects(get_objects_within_timeframe(Expense))
    incomes = serialize_objects(get_objects_within_timeframe(Income))

    data = {
        "expenses": expenses,
        "incomes": incomes,
        "timeframe":
            {
                "start": format_datetime(timeframe_start),
                "end": format_datetime(timeframe_end),
            },
    }

    return JsonResponse(data, status=200)
