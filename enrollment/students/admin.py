from django.contrib import admin
from .models import Student, Enrollment

class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 0

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "student_id",
        "full_name",
        "course",
        "admission_date",
    )

    search_fields = (
        "student_id",
        "first_name",
        "middle_name",
        "last_name",
        "email",
    )

    list_filter = ("course", "admission_date")

    inlines = [EnrollmentInline]

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "academic_year",
        "semester",
        "year_level",
        "section",
        "status",
    )

    list_filter = (
        "academic_year",
        "semester",
        "year_level",
        "status",
    )

    search_fields = (
        "student__student_id",
        "student__first_name",
        "student__last_name",
    )
