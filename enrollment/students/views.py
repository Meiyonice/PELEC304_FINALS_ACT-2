from django.shortcuts import render, get_object_or_404
from .models import Student

CURRENT_ACADEMIC_YEAR = "2026-2027"
CURRENT_SEMESTER = "1st Semester"

def student_list(request):
    students = Student.objects.prefetch_related("enrollments").order_by(
        "student_id"
    )

    for student in students:
        current_enrollment = student.enrollments.filter(
            academic_year=CURRENT_ACADEMIC_YEAR,
            semester=CURRENT_SEMESTER
        ).first()

        student.current_enrollment = current_enrollment
        student.current_status = (
            current_enrollment.status if current_enrollment else "Not Enrolled"
        )

    # Dashboard Summary
    total_students = len(students)

    enrolled_count = sum(
        student.current_status == "Enrolled" for student in students
    )

    pending_count = sum(
        student.current_status == "Pending" for student in students
    )

    dropped_count = sum(
        student.current_status == "Dropped" for student in students
    )

    return render(request, "students/student_list.html", {
        "students": students,
        "current_academic_year": CURRENT_ACADEMIC_YEAR,
        "current_semester": CURRENT_SEMESTER,
        "total_students": total_students,
        "enrolled_count": enrolled_count,
        "pending_count": pending_count,
        "dropped_count": dropped_count,
    })

def student_profile(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)

    enrollments = student.enrollments.all()

    current_enrollment = enrollments.filter(
        academic_year=CURRENT_ACADEMIC_YEAR,
        semester=CURRENT_SEMESTER
    ).first()

    return render(request, "students/student_profile.html", {
        "student": student,
        "enrollments": enrollments,
        "current_enrollment": current_enrollment,
        "current_academic_year": CURRENT_ACADEMIC_YEAR,
        "current_semester": CURRENT_SEMESTER,
    })
