from django.shortcuts import render
from django.template import loader
from .models import Sensor

# Create your views here.

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
        time_data.append(sensor.timestamp)

    tmp_avg = sum_tmp/num_data
    hum_avg = sum_hum/num_data

    data = {
        'tmp_avg': tmp_avg,
        'hum_avg': hum_avg,
        'tmp_data': tmp_data,
        'hum_data': hum_data,
        'time_data': time_data
    }

    return render(request, 'ardxbwsn_main/charts.html',
    {
        'data': data
    })
