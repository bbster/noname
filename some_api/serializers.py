from rest_framework.serializers import ModelSerializer
from .models import Some_Table


class SomeSerializer(ModelSerializer):
    class Meta:
        model = Some_Table
        fields = '__all__'
