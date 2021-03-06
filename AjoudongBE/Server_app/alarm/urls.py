from django.contrib import admin
from django.urls import path, include, re_path
from django.views.decorators.csrf import csrf_exempt

from rest_framework import routers

from . import alarm


urlpatterns = [
    path('', alarm.UserAlarmState.as_view({"get": "retrieve"})),
    path('/userState/<int:uSchoolID>/', alarm.UserAlarmState.as_view({"get": "retrieve"})),
    path('/alarmChange/<int:uSchoolID>/<int:alarmType>/',csrf_exempt(alarm.ChangeUserAlarm.as_view())),
    path('/unreadevent/',csrf_exempt(alarm.AddUnreadAlarm.as_view())),
    path('/newclubevent/', csrf_exempt(alarm.ClubNewEventAlarm.as_view())),
    path('/managerchange/<int:clubID>/', csrf_exempt(alarm.ClubManagerAlarmStateChange.as_view())),
    path('/managerState/<int:clubID>/', alarm.ClubManagerAlarmState.as_view({"get": "retrieve"})),
]