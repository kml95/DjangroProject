from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):
    name = models.CharField(max_length=50, null=True)
    sex = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.name
    

class TrainingBreak(models.Model):
    name = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.name

class TrainingBreakExercise(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=True)
    training_break = models.ForeignKey(TrainingBreak, on_delete=models.CASCADE, null=True)
    repeats = models.DecimalField(null = True, decimal_places=0, max_digits=2)
    series = models.DecimalField(null = True, decimal_places=0, max_digits=2)
    def __str__(self):
        return self.exercise.__str__ + " " + self.training_break.__str__

class Types(models.Model):
    typical = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.typical

class Products(models.Model):
    name = models.CharField(max_length=50, null=True)
    typical = models.ForeignKey(Types, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

