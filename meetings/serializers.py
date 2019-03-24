from rest_framework import serializers
from meetings.models import Meeting
from django.contrib.auth.models import User

class MeetingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')    # used only when serialized, not when deserialized
    class Meta:
        model = Meeting
        fields = ('id', 'created', 'sinceWhen', 'tilWhen', 'user')

    def validate(self, data):
        since = data['sinceWhen']
        til = data['tilWhen']
        if (since >= til) :
            raise serializers.ValidationError("sinceWhen should be earlier than tilWhen.")
        # put
        if (self.instance) :
            for meeting in Meeting.objects.all():
                if (self.instance.id == meeting.id):
                    continue
                left = meeting.sinceWhen
                right = meeting.tilWhen
                if (since < right and left < til) :
                    raise serializers.ValidationError("meeting time overlapped.")
            return data
        # post
        else :
            for meeting in Meeting.objects.all():
                left = meeting.sinceWhen
                right = meeting.tilWhen
                if (since < right and left < til) :
                    raise serializers.ValidationError("meeting time overlapped.")
            return data

class UserSerializer(serializers.ModelSerializer):
    meetings = serializers.PrimaryKeyRelatedField(many=True, queryset=Meeting.objects.all())    # 'meetings' 필드 추가
    class Meta:
        model = User
        fields = ('id', 'username', 'meetings')
