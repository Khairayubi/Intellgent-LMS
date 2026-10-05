from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        SUPER_ADMIN = "SUPER_ADMIN", "Super Admin"
        INSTITUTE_ADMIN = "INSTITUTE_ADMIN", "Institute Admin"
        PRINCIPAL = "PRINCIPAL", "Principal / Director"
        DEPARTMENT_HEAD = "DEPARTMENT_HEAD", "Department Head"
        TEACHER = "TEACHER", "Teacher / Instructor"
        STUDENT = "STUDENT", "Student"
        GUARDIAN = "GUARDIAN", "Parent / Guardian"
        ACCOUNTANT = "ACCOUNTANT", "Accountant"
        REGISTRAR = "REGISTRAR", "Registrar"
        LIBRARIAN = "LIBRARIAN", "Librarian"
        HR = "HR", "HR / Staff Admin"

    class AccountStatus(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        SUSPENDED = "SUSPENDED", "Suspended"
        GRADUATED = "GRADUATED", "Graduated"
        WITHDRAWN = "WITHDRAWN", "Withdrawn"
        ARCHIVED = "ARCHIVED", "Archived"

    role = models.CharField(
        max_length=30,
        choices=Role.choices,
        default=Role.STUDENT,
    )

    status = models.CharField(
        max_length=20,
        choices=AccountStatus.choices,
        default=AccountStatus.ACTIVE,
    )

    phone = models.CharField(
        max_length=30,
        blank=True,
    )

    profile_photo = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username