from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from meetings.models import Meeting
from meetings.serializers import MeetingSerializer

@csrf_exempt
def meeting_list(request):
    """
    List all meetings, or create a new meeting.
    """
    if request.method == 'GET':
        meetings = Meeting.objects.all()
        serializer = MeetingSerializer(meetings, many=True)		# 객체 -> 시리얼라이저
        return JsonResponse(serializer.data, safe=False)		# 시리얼라이저 -> 내용 -> JSON

    elif request.method == 'POST':
        data = JSONParser().parse(request)						# JSON -> 내용
        serializer = MeetingSerializer(data=data)				# 내용 -> 시리얼라이저
        if serializer.is_valid():
            serializer.save()									# 시리얼라이저 -> 객체
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def meeting_detail(request, pk):
    """
    Retrieve, update or delete a meeting.
    """
    try:
        meeting = Meeting.objects.get(pk=pk)
    except Meeting.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MeetingSerializer(meeting)					# 객체 -> 시리얼라이저
        return JsonResponse(serializer.data)					# 시리얼라이저 -> 내용 -> JSON

    elif request.method == 'PUT':
        data = JSONParser().parse(request)						# JSON -> 내용
        serializer = SnippetSerializer(meeting, data=data)		# (객체 -> 시리얼라이저) + (내용 -> 시리얼라이저)
        if serializer.is_valid():
            serializer.save()									# 시리얼라이저 -> 객체
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        meeting.delete()
        return HttpResponse(status=204)
