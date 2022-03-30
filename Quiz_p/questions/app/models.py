from django.db import models


# Create your models here.
class Question(models.Model):
    question = models.TextField()

    def __str__(self):
        return self.question


class Answer(models.Model):
    questions = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE)

    text = models.CharField(max_length=256)
    is_true = models.BooleanField()

    def __str__(self):
        return self.text
