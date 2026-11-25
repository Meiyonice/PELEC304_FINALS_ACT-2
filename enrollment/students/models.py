from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)

    # Personal Information
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    gender = models.CharField(max_length=20)
    nationality = models.CharField(max_length=50)

    # Contact Information
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    # Academic Background
    course = models.CharField(max_length=100)
    previous_school = models.CharField(max_length=200)
    educational_background = models.TextField(blank=True)

    # Guardian Information
    guardian_name = models.CharField(max_length=200)
    guardian_relationship = models.CharField(max_length=50)
    guardian_contact = models.CharField(max_length=20)

    # Admission Information
    admission_date = models.DateField()

    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return " ".join(
            part for part in [
                self.first_name,
                self.middle_name,
                self.last_name
            ] if part
        )

class Enrollment(models.Model):

    SEMESTER_CHOICES = [
        ("1st Semester", "1st Semester"),
        ("2nd Semester", "2nd Semester"),
        ("Summer", "Summer"),
    ]

    STATUS_CHOICES = [
        ("Enrolled", "Enrolled"),
        ("Pending", "Pending"),
        ("Dropped", "Dropped"),
        ("Cancelled", "Cancelled"),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="enrollments"
    )

    academic_year = models.CharField(max_length=9)
    semester = models.CharField(
        max_length=20,
        choices=SEMESTER_CHOICES
    )

    year_level = models.PositiveIntegerField()
    section = models.CharField(max_length=50)

    # Enrollment Dates
    application_date = models.DateField()
    enrollment_date = models.DateField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    class Meta:
        ordering = ["-academic_year", "semester"]
        constraints = [
            models.UniqueConstraint(
                fields=["student", "academic_year", "semester"],
                name="unique_student_semester_enrollment"
            )
        ]

    def __str__(self):
        return (
            f"{self.student.student_id} - "
            f"{self.academic_year} - {self.semester}"
        )
