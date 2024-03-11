from django.contrib import admin
from .models import School, StudentClass, Student, Subject, AssessmentAreas, Awards, Answers, Summary

# Register your models here.
admin.site.register(School)
admin.site.register(StudentClass)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(AssessmentAreas)
admin.site.register(Awards)
admin.site.register(Answers)
admin.site.register(Summary)
