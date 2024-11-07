from rest_framework import serializers
from .models import data
class dataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = data
        fields=('poster','eve','venue','date','phone','link')