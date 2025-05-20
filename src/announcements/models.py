from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class AnnouncementImage(models.Model):
    announcement = models.ForeignKey(
        "Announcement", related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="announcement_images/")

    def __str__(self):
        return f"Zdjęcie ogłoszenia: {self.image.url}"


class Announcement(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    seller_type = models.CharField(max_length=20, choices=[
                                   ("private", "Private"), ("company", "Company")])
    category = models.CharField(max_length=50, choices=[
        ("meat", "Meat"),
        ("dairy", "Dairy"),
        ("fruits", "Fruits"),
        ("vegetables", "Vegetables"),
        ("preserves", "Preserves"),
        ("jars", "Jars"),
        ("other", "Other"),
    ])
    label = models.CharField(max_length=100)
    location = models.CharField(max_length=80, blank=True, null=True)
    description = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    show_email = models.BooleanField(default=False)
    show_phone = models.BooleanField(default=False)
    exchange_type = models.CharField(max_length=20, choices=[
        ("sale", "For Sale"),
        ("trade", "For Trade"),
        ("both", "Sale or Trade"),
    ])
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label
