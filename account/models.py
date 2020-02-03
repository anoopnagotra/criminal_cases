from django.db import models
# Create your models here.
from django.contrib.auth.models import User
import datetime
import uuid
from base.models import  TimeStampedUUIDModel, UUIDModel


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    role = models.CharField(default=False,max_length=200,blank=True)
    attorney_no = models.CharField(max_length=255,blank=True,null=True,verbose_name="Attorney No")
    city = models.CharField(max_length=200,blank=True)
    country = models.CharField(max_length=200,blank=True)
    address = models.CharField(max_length=200,blank=True)
    
    def __str__(self):
        return self.user

    class Meta:
        pass
        # db_table = "user_profile"


# Create your models here.
class Roles(TimeStampedUUIDModel):
    USER_ROLE = (
        ('attorney', 'attorney'),
        ('juror', 'juror'),
        ('user', 'user')
    )

    role = models.CharField(max_length=120, null=False, blank=False, choices=USER_ROLE, help_text='Designates whether the user')

    def __str__(self):
        return self.role 

    class Meta:
        pass
        # db_table = "user_roles"
        verbose_name = ('Roles')
        verbose_name_plural = ('Roles')
