import os
import django
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enrollment.settings")
django.setup()

from students.models import Student, Enrollment

# Clear existing sample records
Student.objects.all().delete()

students_data = [
    {
        "student_id": "2023-001",
        "first_name": "Peter",
        "middle_name": "Benjamin",
        "last_name": "Santos",
        "birth_date": date(2004, 8, 10),
        "gender": "Male",
        "nationality": "Filipino",
        "email": "peter.santos@example.com",
        "phone_number": "09171234501",
        "address": "San Pablo City, Laguna",
        "course": "BSIT",
        "previous_school": "San Pablo City National High School",
        "educational_background": "Senior High School - STEM",
        "guardian_name": "Richard Santos",
        "guardian_relationship": "Father",
        "guardian_contact": "09181234501",
        "admission_date": date(2023, 6, 15),
        "enrollments": [
            ("2023-2024", "1st Semester", 1, "BSIT-1A", date(2023, 6, 15), date(2023, 6, 20), "Enrolled"),
            ("2024-2025", "1st Semester", 2, "BSIT-2A", date(2024, 6, 13), date(2024, 6, 18), "Enrolled"),
            ("2025-2026", "1st Semester", 3, "BSIT-3A", date(2025, 6, 12), date(2025, 6, 17), "Enrolled"),
            ("2026-2027", "1st Semester", 4, "BSIT-4A", date(2026, 6, 10), date(2026, 6, 15), "Enrolled"),
        ],
    },
    {
        "student_id": "2023-002",
        "first_name": "Walter",
        "middle_name": "Hartwell",
        "last_name": "Cruz",
        "birth_date": date(2004, 3, 7),
        "gender": "Male",
        "nationality": "Filipino",
        "email": "walter.cruz@example.com",
        "phone_number": "09171234502",
        "address": "Calamba City, Laguna",
        "course": "BSCS",
        "previous_school": "Calamba Integrated School",
        "educational_background": "Senior High School - STEM",
        "guardian_name": "Michael Cruz",
        "guardian_relationship": "Father",
        "guardian_contact": "09181234502",
        "admission_date": date(2023, 6, 16),
        "enrollments": [
            ("2023-2024", "1st Semester", 1, "BSCS-1A", date(2023, 6, 16), date(2023, 6, 21), "Enrolled"),
            ("2024-2025", "1st Semester", 2, "BSCS-2A", date(2024, 6, 14), date(2024, 6, 19), "Enrolled"),
            ("2025-2026", "1st Semester", 3, "BSCS-3A", date(2025, 6, 13), date(2025, 6, 18), "Enrolled"),
            ("2026-2027", "1st Semester", 4, "BSCS-4A", date(2026, 6, 16), None, "Pending"),
        ],
    },
    {
        "student_id": "2024-001",
        "first_name": "Justin",
        "middle_name": "Drew",
        "last_name": "Reyes",
        "birth_date": date(2005, 2, 14),
        "gender": "Male",
        "nationality": "Filipino",
        "email": "justin.reyes@example.com",
        "phone_number": "09171234503",
        "address": "Los Baños, Laguna",
        "course": "BSIT",
        "previous_school": "Los Baños Senior High School",
        "educational_background": "Senior High School - ICT",
        "guardian_name": "Daniel Reyes",
        "guardian_relationship": "Father",
        "guardian_contact": "09181234503",
        "admission_date": date(2024, 6, 14),
        "enrollments": [
            ("2024-2025", "1st Semester", 1, "BSIT-1B", date(2024, 6, 15), date(2024, 6, 20), "Enrolled"),
            ("2025-2026", "1st Semester", 2, "BSIT-2B", date(2025, 6, 14), date(2025, 6, 19), "Enrolled"),
            ("2026-2027", "1st Semester", 3, "BSIT-3B", date(2026, 6, 12), date(2026, 6, 17), "Enrolled"),
        ],
    },
    {
        "student_id": "2025-001",
        "first_name": "Barbie",
        "middle_name": "Millicent",
        "last_name": "Garcia",
        "birth_date": date(2006, 7, 21),
        "gender": "Female",
        "nationality": "Filipino",
        "email": "barbie.garcia@example.com",
        "phone_number": "09171234504",
        "address": "Santa Cruz, Laguna",
        "course": "BSCS",
        "previous_school": "Santa Cruz National High School",
        "educational_background": "Senior High School - STEM",
        "guardian_name": "Robert Garcia",
        "guardian_relationship": "Father",
        "guardian_contact": "09181234504",
        "admission_date": date(2025, 6, 13),
        "enrollments": [
            ("2025-2026", "1st Semester", 1, "BSCS-1B", date(2025, 6, 15), date(2025, 6, 20), "Enrolled"),
            ("2026-2027", "1st Semester", 2, "BSCS-2B", date(2026, 6, 13), date(2026, 6, 18), "Enrolled"),
        ],
    },
    {
        "student_id": "2026-001",
        "first_name": "Mario",
        "middle_name": "Luigi",
        "last_name": "Flores",
        "birth_date": date(2007, 11, 5),
        "gender": "Male",
        "nationality": "Filipino",
        "email": "mario.flores@example.com",
        "phone_number": "09171234505",
        "address": "San Pablo City, Laguna",
        "course": "BSIT",
        "previous_school": "San Pablo City Science Integrated High School",
        "educational_background": "Senior High School - ICT",
        "guardian_name": "Antonio Flores",
        "guardian_relationship": "Father",
        "guardian_contact": "09181234505",
        "admission_date": date(2026, 6, 12),
        "enrollments": [
            ("2026-2027", "1st Semester", 1, "BSIT-1A", date(2026, 6, 14), date(2026, 6, 19), "Enrolled"),
        ],
    },
    {
        "student_id": "2026-002",
        "first_name": "Wednesday",
        "middle_name": "Friday",
        "last_name": "Dela Cruz",
        "birth_date": date(2007, 9, 13),
        "gender": "Female",
        "nationality": "Filipino",
        "email": "wednesday.delacruz@example.com",
        "phone_number": "09171234506",
        "address": "Alaminos, Laguna",
        "course": "BSCS",
        "previous_school": "Alaminos National High School",
        "educational_background": "Senior High School - STEM",
        "guardian_name": "Gomez Dela Cruz",
        "guardian_relationship": "Father",
        "guardian_contact": "09181234506",
        "admission_date": date(2026, 6, 12),
        "enrollments": [
            ("2026-2027", "1st Semester", 1, "BSCS-1A", date(2026, 6, 15), date(2026, 6, 20), "Dropped"),
        ],
    },
]

for data in students_data:
    enrollment_data = data.pop("enrollments")
    student = Student.objects.create(**data)

    for record in enrollment_data:
        (
            academic_year,
            semester,
            year_level,
            section,
            application_date,
            enrollment_date,
            status
        ) = record

        Enrollment.objects.create(
            student=student,
            academic_year=academic_year,
            semester=semester,
            year_level=year_level,
            section=section,
            application_date=application_date,
            enrollment_date=enrollment_date,
            status=status,
        )

print("Successfully created sample records!")
print("Students:", Student.objects.count())
print("Enrollments:", Enrollment.objects.count())
