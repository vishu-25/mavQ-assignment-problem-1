from django.shortcuts import render
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from .models import *

from django_filters.rest_framework import DjangoFilterBackend


class TeacherViewSet(ModelViewSet):
    permission_classes = []
    authentication_classes = []
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["is_active", "name", "designation"]


class CourseViewSet(ModelViewSet):
    permission_classes = []
    authentication_classes = []
    queryset = Course.objects.all()
    serializer_class = CourseSerializerPOST

    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "course_mentor",
        "name",
        "start_date",
        "end_date",
        "description",
        "is_active",
    ]
