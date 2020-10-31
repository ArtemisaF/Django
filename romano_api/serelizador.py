from rest_framework import serializers

class RomanoSerializer(serializers.Serializer):
    numero= serializers.CharField(max_length=10)