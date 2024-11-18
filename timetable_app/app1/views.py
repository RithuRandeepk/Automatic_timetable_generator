import random
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages  
from app1.forms import CourseForm, PeriodForm, StaffForm, SubjectForm
from app1.models import Course, Day, Period, Staff, Timetable
from app1.utils import generate_timetable

# Create your views here.

def create_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subject saved!')  
            return redirect('create_subject')
    else:
        form = SubjectForm()
    return render(request, 'add_subject.html', {'form': form})

# Create a course
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course saved!')  
            return redirect('create_course')
    else:
        form = CourseForm()
    return render(request, 'course_form.html', {'form': form})

def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('create_course')
    else:
        form = CourseForm(instance=course)
    return render(request, 'course_form.html', {'form': form})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        # You can uncomment this if you want to show a success message
        messages.success(request, 'Deleted!')
        return redirect('course_list')
    return render(request, 'course_list.html', {'course': course})


def add_period(request):
    if request.method == "POST":
        form = PeriodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_period')  # Redirect to a list or detail page after saving
    else:
        form = PeriodForm()

    return render(request, 'add_period.html', {'form': form})

def list_period(request):
    period = Period.objects.all()
    return render(request, 'period_list.html', {'period': period})

def staff_list(request):
    staff_members = Staff.objects.all()
    return render(request, 'staff_list.html', {'staff_members': staff_members})

# Create a new staff member
def create_staff(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm()
    return render(request, 'create_staff.html', {'form': form})

# Update an existing staff member
def update_staff(request, pk):
    staff_member = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff_member)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm(instance=staff_member)
    return render(request, 'update_staff.html', {'form': form})

# Delete a staff member
def delete_staff(request, pk):
    staff_member = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        staff_member.delete()
        return redirect('staff_list')
    return render(request, 'delete_staff.html', {'staff_member': staff_member})

def generate_timetable_view(request, course_id):
    course = Course.objects.get(id=course_id)
    # Generate timetable
    generate_timetable(course)
    return redirect('timetable_list', course_id=course.id)

def timetable_list(request, course_id):
    course = Course.objects.get(id=course_id)
    timetable = Timetable.objects.filter(course=course)
    return render(request, 'timetable_list.html', {'timetable': timetable, 'course': course})


