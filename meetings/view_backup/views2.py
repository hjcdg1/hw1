from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from meetings.models import Meeting
from meetings.serializers import MeetingSerializer

@api_view(['GET', 'POST'])
def meeting_list(request, format=None):
    """
    List all meetings, or create a new meeting.
    """
    if request.method == 'GET':
        meetings = Meeting.objects.all()
        serializer = MeetingSerializer(meetings, many=True)		# 객체 -> 시리얼라이저
        return Response(serializer.data)		                # 시리얼라이저 -> 내용 -> JSON

    elif request.method == 'POST':
        serializer = MeetingSerializer(data=request.data)		# JSON -> 내용 -> 시리얼라이저
        if serializer.is_valid():
            serializer.save()									# 시리얼라이저 -> 객체
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def meeting_detail(request, pk, format=None):
    """
    Retrieve, update or delete a meeting.
    """
    try:
        meeting = Meeting.objects.get(pk=pk)
    except Meeting.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MeetingSerializer(meeting)					        # 객체 -> 시리얼라이저
        return Response(serializer.data)					            # 시리얼라이저 -> 내용 -> JSON

    elif request.method == 'PUT':
        serializer = SnippetSerializer(meeting, data=request.data)		# (객체 -> 시리얼라이저) + (JSON -> 내용 -> 시리얼라이저)
        if serializer.is_valid():
            serializer.save()									        # 시리얼라이저 -> 객체
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        meeting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
