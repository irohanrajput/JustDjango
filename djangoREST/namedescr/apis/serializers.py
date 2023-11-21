from rest_framework import serializers
from .models import justModel

class justSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = justModel
		fields = ('title', 'description')
