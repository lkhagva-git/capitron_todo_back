from django.db import models

from io import BytesIO
from django.core.files import File
from django.utils import timezone

from main.choices import *

from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

import uuid

import os


def path_and_rename(path):
    return os.path.join(path, uuid.uuid4().hex)

class Image(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    photo = models.ImageField(upload_to=path_and_rename("anket"))


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=500, verbose_name="Нэр", null=True, blank=True)
    last_name = models.CharField(max_length=500, verbose_name="Овог", null=True, blank=True)
    email = models.CharField(max_length=500, verbose_name='Имэйл хаяг', null=True, blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        return super(Profile, self).save(*args, **kwargs)

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()


class Category(models.Model):
    name = models.CharField(max_length=500, verbose_name='Нэр', null=True, blank=True)
    created_at = models.DateField(null=True, blank=True)

    
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=500, verbose_name ='Даалгаврын нэр', null=True, blank=True)
    deadline = models.DateTimeField(verbose_name ='Даалгаврын эцсийн хугацаа', null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, verbose_name="Даалгаврийн төлөв", null=True, blank=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, verbose_name="Даалгаврийн priority", null=True, blank=True)
    created_at = models.DateField(verbose_name ='Даалгавар үүссэн огноо', null=True, blank=True)
    updated_at = models.DateField(verbose_name ='Даалгавар шинэчилсэн огноо', null=True, blank=True)
     
    

    






