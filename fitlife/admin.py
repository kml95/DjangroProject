from django.contrib import admin
from .models import Exercise, TrainingBreak, TrainingBreakExercise

admin.site.register(Exercise)
admin.site.register(TrainingBreak)
admin.site.register(TrainingBreakExercise)