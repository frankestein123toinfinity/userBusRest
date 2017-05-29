#api/serializers.py

from rest_framework import serializers
from .models import BusDatalist

class BusDatalistSerializer(serializers.ModelSerializer):

	class Meta:

		model = BusDatalist
		fields = ('id', 'busStopId', 'date_created', 'date_modified')
		read_only_fields = ('date_created', 'date_modified')