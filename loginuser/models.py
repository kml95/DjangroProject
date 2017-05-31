from django.db import models
from django.contrib.auth.models import User


class UserConfirmation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    confirmed = models.NullBooleanField(null=True)
    code = models.CharField(max_length=16, null=True)
    def __str__(self):
        return self.user.username+" "+str(self.confirmed)
