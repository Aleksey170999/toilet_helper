from rest_framework import serializers
from toilet_posts.models import Toilet


class ToiletLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toilet
        fields = '__all__'


class ToiletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toilet
        fields = '__all__'
