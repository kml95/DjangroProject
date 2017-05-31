from django.contrib import admin
from .models import Exercise, TrainingBreak, TrainingBreakExercise,Products,Types

admin.site.register(Exercise)
admin.site.register(TrainingBreak)
admin.site.register(TrainingBreakExercise)
admin.site.register(Products)
admin.site.register(Types)