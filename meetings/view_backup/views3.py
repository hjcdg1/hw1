from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from meetings.models import Meeting
from meetings.serializers import MeetingSerializer

class MeetingList(APIView):
    """
    List all meetings, or create a new meeting.
    """
    def get(self, request, format=None):
        meetings = Meeting.objects.all()
        serializer = MeetingSerializer(meetings, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MeetingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MeetingDetail(APIView):
    """
    Retrieve, update or delete a meeting instance.
    """
    def get_object(self, pk):
        try:
            return Meeting.objects.get(pk=pk)
        except Meeting.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        meeting = self.get_object(pk)
        serializer = MeetingSerializer(meeting)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        meeting = self.get_object(pk)
        serializer = MeetingSerializer(meeting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        meeting = self.get_object(pk)
        meeting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


