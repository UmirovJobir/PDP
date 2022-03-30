from django.db import models


class Came(models.Model):
    PTO = "Ishlab chiqarish"
    Qurilish = "Qurilish bo'limi"
    Energetika = "Energetika bo'limi"
    Mexanika = "Mexanika bo'limi"
    Iqdisod = "Iqdisod bo'limi"
    Ijro = "Ijro intizom"
    Roles = (
        (PTO, "Ishlab chiqarish"),
        (Qurilish, "Qurilish bo'limi"),
        (Energetika, "Energetika bo'limi"),
        (Mexanika, "Mexanika bo'limi"),
        (Iqdisod, "Iqdisod bo'limi"),
        (Ijro, "Ijro intizom")
    )

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    section = models.CharField(max_length=200, choices=Roles)
    arrival_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "Came"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Went(models.Model):
    PTO = "Ishlab chiqarish"
    Qurilish = "Qurilish bo'limi"
    Energetika = "Energetika bo'limi"
    Mexanika = "Mexanika bo'limi"
    Iqdisod = "Iqdisod bo'limi"
    Ijro = "Ijro intizom"
    Roles = (
        (PTO, "Ishlab chiqarish"),
        (Qurilish, "Qurilish bo'limi"),
        (Energetika, "Energetika bo'limi"),
        (Mexanika, "Mexanika bo'limi"),
        (Iqdisod, "Iqdisod bo'limi"),
        (Ijro, "Ijro intizom")
    )

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    section = models.CharField(max_length=20, choices=Roles)
    time_to_leave = models.DateTimeField(null=True, blank=True)  # auto_now_add=True

    class Meta:
        db_table = "Went"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CameAndWent(models.Model):
    came = models.ForeignKey(Came, on_delete=models.CASCADE)
    went = models.ForeignKey(Went, on_delete=models.CASCADE)
