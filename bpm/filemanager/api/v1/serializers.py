from rest_framework import serializers
from bpm.filemanager.models import Image


class ImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Image
        fields = '__all__'
    

class ImageCreateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = Image
        fields = '__all__'