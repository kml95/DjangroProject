from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):
    name = models.CharField(max_length=50, null=True)

class TrainingBreak(models.Model):
    name = models.CharField(max_length=50, null=True)

class TrainingBreakExercise(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=True)
    training_break = models.ForeignKey(TrainingBreak, on_delete=models.CASCADE, null=True)
    repeats = models.DecimalField(null = True)
    series = models.DecimalField(null = True)
