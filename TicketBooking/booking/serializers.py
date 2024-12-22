from rest_framework import serializers
from .models import StageEvent, StageEventShow, TicketBooking

class StageEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = StageEvent
        fields = '__all__'

class StageEventShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = StageEventShow
        fields = '__all__'

class TickerBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketBooking
        fields = '__all__'
