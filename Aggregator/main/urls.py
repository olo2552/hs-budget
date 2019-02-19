from django.urls import path
from . import views

urlpatterns = [
    path("add_expense/", views.add_expense, name="add_expense"),
    path("add_income/", views.add_income, name="add_income"),
    path("<raw_timeframe_start>/<raw_timeframe_end>", views.show, name="show"),
]
