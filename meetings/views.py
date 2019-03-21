from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from meetings.models import Meeting
from meetings.serializers import MeetingSerializer, UserSerializer
from meetings.permissions import OnlyUserCanAccess
#from django.http import HttpResponse, JsonResponse, Http404
#from django.views.decorators.csrf import csrf_exempt
#from rest_framework import mixins, status
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser
#from rest_framework.decorators import api_view
#from rest_framework.views import APIView

class MeetingList(generics.ListCreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class MeetingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, OnlyUserCanAccess)
    '''
    def update(self, request, *args, **kwargs):
        self_meeting = self.get_object()
        serializer = MeetingSerializer(self_meeting, data=request.data)
        serializer.is_valid(raise_exception=True)
        since = str(serializer['sinceWhen']) #request.data.__getitem__('sinceWhen')
        till = str(serializer['tillWhen']) #request.data.__getitem__('tillWhen')
        if (since >= till) :
            raise serializers.ValidationError("sinceWhen should be earlier than tillWhen.")
        for meeting in Meeting.objects.all():
            if (self_meeting.id == meeting.id):
                continue
            left = str(meeting.sinceWhen)
            right = str(meeting.tillWhen)
            if ((left < since and since < right) or (left < till and till < right) or (since < left and right < till)) :
                raise serializers.ValidationError("meeting time overlapped.")
        serializer.is_valid(raise_exception=True)
        return self.perform_update(serializer)
        #return Response(serializer.data)
    '''

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
