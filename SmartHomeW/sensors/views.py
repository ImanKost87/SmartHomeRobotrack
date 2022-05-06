from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.utils import timezone
import json
from .forms import (
    SensorsDataForm,
    UserDataForm,
    SensorsSetupForm
)
from .models import (
    SensorsData,
    UserData,
    SensorsSetup
)


def get_data(request):
    context = dict()
    if request.method == 'GET':
        in_sensors = SensorsData.objects.filter(owner=request.user.id).last()
        if in_sensors:
            context['in_data'] = deserialize_sensors(in_sensors)
        else:
            context['in_data'] = None

        out_sensors = SensorsSetup.objects.filter(owner=request.user.id).last()
        if out_sensors:
            context['out_data'] = deserialize_sensors(out_sensors)
        else:
            context['out_data'] = None
    return render(request, 'sensors/cards.html', context)


def deserialize_sensors(data):
    translator_dict = {"A": ["ИК-датчик", "invert_colors"], "B": ["Датчик освещенности", "wb_twilight"],
                       "C": ["Модуль светодиода", "lightbulb"], "D": ["Датчик ПДУ", "videogame_asset"],
                       "E": ["Датчик касания", "button"], "F": ["Динамик", "smart_button"],
                       "G": ["Пьезоизлучаетль", "notifications"], "H": ["Датчик звука 2", "circle_notifications"],
                       "I": ["Датчик наклона", "network_locked"], "J": ["Датчик вибрации", "vibration"],
                       "K": ["Датчик огня", "local_fire_department"], "L": ["Датчик магнитного поля", "noise_aware"],
                       "M": ["Датичк цвета + датчик освещенности", "wb_incandescent"],
                       "N": ["Ультразвуковой датчик расстояния", "play_for_work"],
                       "O": ["Серводвигатель", "refresh"], "P": ["Дисплей", "view_sidebar"],
                       "Q": ["MP3", "speaker"], "R": ["Двигатель", "settings_applications"],
                       "S": ["Датчик положения", "flight_land"], }
    context = dict()
    sensors = json.loads(str(data))
    for sensor in sensors:
        port = sensor['port']
        value = sensor['value']

        s_type = sensor['type'][0]
        label = translator_dict[s_type][0] + ' - ' + port
        icon = translator_dict[s_type][1]
        context[label] = [icon, port, value, sensor['type']]
    return context


@csrf_exempt
def receive_data(request):
    if request.method == 'POST':
        req = json.loads(request.body.decode("utf-8"))
        try:
            sender = User.objects.get(username=json.dumps(req['user'])[1:-1])
        except User.DoesNotExist:
            print("Receive data from non-existent user")
            return HttpResponse("User does not exist")

        SensorsData.objects.filter(owner=sender.pk).delete()

        sensors_data = {'data': json.dumps(req['data']),
                        'owner': sender.pk,
                        'date_created': timezone.now()}
        form = SensorsDataForm(sensors_data)
        if form.is_valid():
            cd = form.cleaned_data
            s = SensorsData(data=cd['data'], date_created=cd['date_created'], owner=cd['owner'])
            s.save()

        out_data = UserData.objects.filter(owner=sender.pk).last()
        if out_data:
            return HttpResponse(str(out_data))
        return HttpResponse("Only data received")
    if request.method == 'GET':
        return HttpResponse("User should not be here")


@csrf_exempt
def send_data(request):
    if request.method == 'POST':
        req = json.loads(request.body.decode("utf-8"))
        try:
            sender = User.objects.get(username=json.dumps(req['user'])[1:-1])
        except User.DoesNotExist:
            print("Send data for non-existent user")
            return HttpResponse("User does not exist")
        sensors_data = {'data': json.dumps(req['data']),
                        'owner': sender.pk,
                        'date_created': timezone.now()}
        form = UserDataForm(sensors_data)
        if form.is_valid():
            cd = form.cleaned_data
            s = UserData(data=cd['data'], date_created=cd['date_created'], owner=cd['owner'])
            s.save()
        return HttpResponse("Sensors data sent")
    if request.method == 'GET':
        return HttpResponse("User should not be here")


@csrf_exempt
def send_setup(request):
    if request.method == 'POST':
        req = json.loads(request.body.decode("utf-8"))
        try:
            sender = User.objects.get(username=json.dumps(req['user'])[1:-1])
        except User.DoesNotExist:
            print("Send setup for non-existent user")
            return HttpResponse("User does not exist")

        SensorsSetup.objects.filter(owner=sender.pk).delete() # delete all previous setups from this user

        sensors_data = {'setup': json.dumps(req['setup']),
                        'owner': sender.pk,
                        'date_created': timezone.now()}
        form = SensorsSetupForm(sensors_data)
        if form.is_valid():
            cd = form.cleaned_data
            s = SensorsSetup(setup=cd['setup'], date_created=cd['date_created'], owner=cd['owner'])
            s.save()
        return HttpResponse("Sensors setup received")
    if request.method == 'GET':
        return HttpResponse("User should not be here")


def test(request):
    return render(request, 'sensors/draw.html', {})
