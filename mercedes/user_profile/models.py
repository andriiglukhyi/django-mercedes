from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
# from multiselectfield import MultiSelectField


class UserProfile(models.Model):
    '''Model for a user profile.'''

    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE
    )
    bio = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=180, blank=True, null=True)
    website = models.URLField(max_length=180, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    @classmethod
    def active(cls):
        return cls.objects.filter(is_active=True)

    def __str__(self):
        return self.user.username


@receiver(models.signals.post_save, sender=User)
def create_profile(sender, **kwargs):
    if kwargs['created']:
        # Token.objects.create(user=kwargs['instance'])
        profile = UserProfile(user=kwargs['instance'])
        profile.save()