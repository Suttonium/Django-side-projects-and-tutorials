from django.db import models
from django.contrib.auth.models import User


# User automatically comes with a first and last name field, an email field, and ...

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)

    # additional classes
    portfolio_site = models.URLField(blank=True)  # blank indicates whether or not it is required by the user

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
