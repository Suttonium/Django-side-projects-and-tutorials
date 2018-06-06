from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


# Create your models here.
# class UserProfileManager(models.Manager):
#     def get_queryset(self):
#         return super(UserProfileManager, self).get_queryset().filter(city='London')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone_number = models.IntegerField(default=0)

    # london = UserProfileManager()

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:  # if user object has been created
        UserProfile.objects.create(user=kwargs['instance'])  # make the users profile


post_save.connect(create_profile, sender=User)
