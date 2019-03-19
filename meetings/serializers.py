from rest_framework import serializers
from meetings.models import Meeting
from django.contrib.auth.models import User

class MeetingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')    # used only when serialized, not when deserialized
    class Meta:
        model = Meeting
        fields = ('id', 'created', 'sinceWhen', 'tillWhen', 'user')
    def validate(self, data):
        since = data['sinceWhen']
        till = data['tillWhen']
        if (since >= till) :
            raise serializers.ValidationError("sinceWhen should be earlier than tillWhen.")
        for meeting in Meeting.objects.all():
            left = meeting.sinceWhen
            right = meeting.tillWhen
            if ((left < since and since < right) or (left < till and till < right) or (since < left and right < till)) :
                raise serializers.ValidationError("meeting time overlapped.")
        return data

class UserSerializer(serializers.ModelSerializer):
    meetings = serializers.PrimaryKeyRelatedField(many=True, queryset=Meeting.objects.all())    # 'meetings' 필드 추가
    class Meta:
        model = User
        fields = ('id', 'username', 'meetings')
