from django.db import models
from django.contrib.auth.models import User


class UserExtended(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_slug = models.SlugField(blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    description = models.TextField(blank=True, help_text="256 Characters only")
    facebook = models.CharField(blank=True, max_length=255)
    whatsapp = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return f"{ self.user.username } Profile"
