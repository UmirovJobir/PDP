from django.db import models


# Create your models here.

class Speciality(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField(default=0)
    start_date = models.DateField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    PROFESSOR = "Professor"
    PHD = "Phd"
    N_A = "N/A"
    ROLES = (
        (PROFESSOR, "Professor"),
        (PHD, "Phd"),
        (N_A, "N/A")
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=10, choices=ROLES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Subject(models.Model):
    name = models.CharField(max_length=100)
    specialities = models.ManyToManyField(Speciality)
    teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.name
