from rest_framework import serializers
from .models import *


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class CourseSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

    def to_representation(self, instance):
        serializer = CourseSerializerGET(instance)
        return serializer.data


class CourseSerializerGET(serializers.ModelSerializer):
    course_mentor = TeacherSerializer()

    class Meta:
        model = Course
        fields = "__all__"
