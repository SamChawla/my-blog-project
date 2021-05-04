from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    GENDER = (("MALE", "MALE"), ("FEMALE", "FEMALE"), ("SKIP", "SKIP"))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    gender = models.CharField(max_length=6, choices=GENDER, default="SKIP")

    def __str__(self):
        return f"{self.user.username}"
