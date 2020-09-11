from django.db import models


# Create your models here.
class Student(models.Model):
    rollNo = models.IntegerField()
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)

    def __str__(self):
        return self.firstName
