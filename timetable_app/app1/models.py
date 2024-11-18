from django.db import models

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.subject_name

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    subjects = models.ManyToManyField(Subject, related_name="courses")


    def __str__(self):
        return self.course_name

class Day(models.Model):
    day_name = models.CharField(max_length=20)  

    def __str__(self):
        return self.day_name
    
class Period(models.Model):
    session_name=models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.day.day_name}: {self.session_name}"
    
class Staff(models.Model):
    name = models.CharField(max_length=100)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.name
    
class Timetable(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course.course_name} : {self.day.day_name}: {self.period.session_name}: {self.subject} :({self.staff})"
    
