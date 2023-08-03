from django.db import models

# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField()
    designation = models.CharField(max_length=50)


class Course(models.Model):
    course_mentor = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, null=True, related_name="teacher"
    )
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    is_active = models.BooleanField()
