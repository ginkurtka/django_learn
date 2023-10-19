from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Project


@receiver(post_save, sender=Project)
def user_log(sender, instance, created, **kwargs):
  if created:
    print("пользователь создан")