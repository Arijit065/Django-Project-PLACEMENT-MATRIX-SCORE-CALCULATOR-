from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    score = models.IntegerField()
    placed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.roll_no})"
