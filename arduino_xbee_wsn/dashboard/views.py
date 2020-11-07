from django.shortcuts import render
from django.template import loader
from .models import Sensor
from datetime import datetime

# Create your views here

def charts(request):
    sum_tmp = 0
    sum_hum = 0
    num_data = 0
    tmp_data = []
    hum_data = []
    time_data = []

    queryset = Sensor.objects.order_by('timestamp')

    for sensor in queryset:
        num_data = num_data + 1
        sum_tmp = sum_tmp + sensor.temperature
        sum_hum = sum_hum + sensor.humidity
        tmp_data.append(sensor.temperature)
        hum_data.append(sensor.humidity)
        dt_ob = datetime.fromtimestamp(int(sensor.timestamp))
        time_data.append(str(dt_ob))

    print("TEMPERATURE", sum_tmp)
    tmp_avg = round(sum_tmp / float(num_data), 2)
    hum_avg = round(sum_hum / float(num_data), 2)

    data = {
        'tmp_avg': tmp_avg,
        'hum_avg': hum_avg,
        'tmp_data': tmp_data,
        'hum_data': hum_data,
        'time_data': time_data
    }

    return render(request, 'dashboard/charts.html',
    {
        'data': data
    })

def charts_detail(request, sensor_id):
    sum_tmp = 0
    sum_hum = 0
    num_data = 0
    tmp_data = []
    hum_data = []
    time_data = []

    queryset = Sensor.objects.filter(sensor_id=sensor_id).order_by('timestamp')

    for sensor in queryset:
        num_data = num_data + 1
        sum_tmp = sum_tmp + sensor.temperature
        sum_hum = sum_hum + sensor.humidity
        tmp_data.append(sensor.temperature)
        hum_data.append(sensor.humidity)
        dt_ob = datetime.fromtimestamp(int(sensor.timestamp))
        time_data.append(str(dt_ob))

    tmp_avg = round(sum_tmp / float(num_data), 2)
    hum_avg = round(sum_hum / float(num_data), 2)

    data = {
        'tmp_avg': tmp_avg,
        'hum_avg': hum_avg,
        'tmp_data': tmp_data,
        'hum_data': hum_data,
        'time_data': time_data
    }

    return render(request, 'dashboard/charts.html',
    {
        'data': data
    })