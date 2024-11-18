import random
from .models import Timetable, Day, Period, Subject, Staff

def generate_timetable(course):
    days = Day.objects.filter(day_name__in=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])  
    subjects = list(course.subjects.all())
    periods = Period.objects.all()

    if len(subjects) < 4:
        raise ValueError("Not enough subjects for 4 periods per day.")

    timetable_entries = []

    for day in days:
        random_subjects = random.sample(subjects, 4)  

        for period, subject in zip(periods[:4], random_subjects):  
            available_staff = Staff.objects.filter(subjects=subject)

            if available_staff.exists():
                staff = random.choice(available_staff)

                timetable_entries.append(Timetable(
                    course=course,
                    day=day,
                    period=period,
                    subject=subject,
                    staff=staff
                ))

    # Bulk create all the timetable entries
    Timetable.objects.bulk_create(timetable_entries)

    # Print the timetable
    print_timetable(timetable_entries)

def print_timetable(timetable_entries):
    timetable_dict = {}

    for entry in timetable_entries:
        day = entry.day.day_name
        if day not in timetable_dict:
            timetable_dict[day] = []
        timetable_dict[day].append(entry)

    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    print(f"{timetable_entries[0].course.course_name} Timetable")  
    print("------------------------------------------------------------")
    print("Day       | Period           | Subject          | Staff")
    print("------------------------------------------------------------")

    for day in days_of_week:
        if day in timetable_dict:
            for entry in timetable_dict[day]:
                period = f"{entry.period.start_time.strftime('%I:%M %p')} - {entry.period.end_time.strftime('%I:%M %p')}"
                subject = entry.subject.subject_name
                staff = entry.staff.name
                print(f"{day:<10} | {period:<17} | {subject:<17} | {staff}")
        else:
            print(f"{day:<10} | No Classes        |                   |")

    print("------------------------------------------------------------")
