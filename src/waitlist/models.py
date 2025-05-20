from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL  # 'auth.User'

# Create your models here.


class WaitlistEntry(models.Model):
    user = models.ForeignKey(
        User, default=None, null=True, blank=True, on_delete=models.SET_NULL)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    label = models.CharField(max_length=40)
