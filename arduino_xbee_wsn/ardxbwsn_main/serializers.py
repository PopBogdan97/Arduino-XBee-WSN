from rest_framework import serializers
from .models import Sensor

class SensorSerializer(serializers.Serializer):
    class Meta:
        model = Sensor
        fields = ['id', 'sensor_id', 'temperature', 'humidity', 'timestamp']

def create(self, validated_data):
    """
    Create a return a new Sensor instance, given the validated data
    """
    return Sensor.objects.create(**validated_data)

def update(self, instance, validated_data):
    instance.sensor_id = validated_data.get('sensor_id', instance.sensor_id)
    instance.temperature = validated_data.get('temperature', instance.temperature)
    instance.humidity = validated_data.get('humidity', instance.humidity)
    instance.timestamp = validated_data.get('timestamp', instance.timestamp)
    instance.save()
    return instance