from rest_framework import serializers
from toilet_posts.models import Toilet


class ToiletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toilet
        fields = '__all__'