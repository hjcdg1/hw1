from rest_framework import serializers
from meetings.models import Meeting

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ('id', 'created', 'sinceWhen', 'tillWhen')
