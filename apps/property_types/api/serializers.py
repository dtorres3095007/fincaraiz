from ..models import PropertyType
from rest_framework import serializers

class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = "__all__"

