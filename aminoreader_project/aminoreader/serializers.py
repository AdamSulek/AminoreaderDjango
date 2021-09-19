from rest_framework import serializers
from .models import Aminoreader

class FileSerializer(serializers.ModelSerializer):
    class Meta():
        model = Aminoreader
        fields = '__all__'
