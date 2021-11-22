from rest_framework import serializers
from .models import Insect

class InsectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insect
        fields = ('name', 'can_fly', 'number_of_legs', 'description', 'author')