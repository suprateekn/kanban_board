from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    profile_pic = models.ImageField(upload_to='images/', blank=True, null=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    verified = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, raw, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
