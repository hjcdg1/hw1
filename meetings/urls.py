from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from meetings import views

urlpatterns = [
    path('meetings/', views.MeetingList.as_view()),
    path('meetings/<int:pk>/', views.MeetingDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
