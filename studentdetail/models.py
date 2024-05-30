from django.db import models
from res_app.models import OneTeamBatch

class Student(models.Model):
    batch_name = models.ForeignKey(OneTeamBatch, on_delete=models.CASCADE, limit_choices_to={"isactive": True})
    student_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    has_laptop = models.BooleanField(default=False)

    def __str__(self):
        return self.student_name



