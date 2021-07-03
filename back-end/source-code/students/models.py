from django.db import models


class StudentModel(models.Model):
    names = models.CharField(max_length=120)
    file = models.IntegerField()

    def __str__(self):
        return "Names: " + self.names + "\n File: " + str(self.file)
