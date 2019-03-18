from rest_framework import serializers
from meetings.models import Meeting
from django.contrib.auth.models import User

class MeetingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')    # used only when serialized, not when deserialized
    class Meta:
        model = Meeting
        fields = ('id', 'created', 'sinceWhen', 'tillWhen', 'user')

class UserSerializer(serializers.ModelSerializer):
    meetings = serializers.PrimaryKeyRelatedField(many=True, queryset=Meeting.objects.all())    # 'meetings' 필드 추가
    class Meta:
        model = User
        fields = ('id', 'username', 'meetings')
