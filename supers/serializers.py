from rest_framework import serializers
from . import Super

class Superserializer(serializers.ModelSerializer):
    class Meta:
        model = Super
        fields = ['id', 'name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catchphrase']