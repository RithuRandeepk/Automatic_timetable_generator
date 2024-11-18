from django.contrib import admin

# Register your models here.
from .models import Course, Subject, Day, Period, Staff, Timetable

admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Day)
admin.site.register(Period)
admin.site.register(Staff)
admin.site.register(Timetable)
