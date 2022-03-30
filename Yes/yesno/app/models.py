from django.db import models

# Create your models here.


class Answer(models.Model):
    YES = 'YES'
    NO = 'NO'
    ROLES = (
        (YES, 'YES'),
        (NO, 'NO'),
    )
    answer = models.CharField(max_length=10, choices=ROLES)

    def __str__(self):
        return self.answer


