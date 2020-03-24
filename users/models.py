# -*- coding: utf-8 -*-

# Standard Library
import datetime

# Third Party Stuff
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core import validators
from django.db import models, IntegrityError
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
# from versatileimagefield.fields import PPOIField, VersatileImageField
from django.core.files.temp import NamedTemporaryFile
from django.core.files import File

# Electric_Soul Stuff
from base.models import TimeStampedUUIDModel, UUIDModel
from django_extensions.db.models import TimeStampedModel

# from urllib import parse
import json
import requests



class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, TimeStampedUUIDModel):
    USER_ROLE = (
        ('attorney', 'attorney'),
        ('juror', 'juror')
       )

    first_name = models.CharField(_('First Name'), max_length=120, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=120, blank=True)
    email = models.EmailField(_('email address'), unique=True, db_index=True)
    username = models.CharField(_('username'), max_length=30, unique=True,
                                help_text=_('Required. 30 characters or fewer. Letters, digits and '
                                            './+/-/_ only.'),
                                validators=[validators.RegexValidator(r'^[\w.+-]+$',
                                                                      _('Value may contain only letters,'
                                                                        'numbers and ./+/-/_ characters.')), ],
                                error_messages={'unique': _("A user with that username already exists."),
                                                })

    # image = VersatileImageField(upload_to=upload_to, blank=True, null=True, ppoi_field='cover_image_poi',
                                      # verbose_name="cover image")
    profile_image = models.ImageField(upload_to = "profileImages", default = '', verbose_name="Profile Image")
    
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text='Designates whether the user can log into this admin site.')

    is_active = models.BooleanField('active', default=True,
                                    help_text='Designates whether this user should be treated as '
                                              'active. Unselect this instead of deleting accounts.')
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    role = models.CharField(max_length=120, null=True, blank=True, choices=USER_ROLE, help_text='Designates whether the user is  or scanner.')

    # country = models.ForeignKey(GeoCountry, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()

    # birthdate = models.DateField(null=True, blank=True)
    age_group = models.CharField(max_length=120, null=True, blank=True, choices=USER_ROLE, help_text='Designates whether the user is  or scanner.')

    # mobile_number = models.CharField(null=True, blank=True, max_length=80)
    mobile_number = models.CharField(null=True, blank=True, max_length=80)
    address = models.CharField(null=True, blank=True, max_length=200)
    city = models.CharField(null=True, blank=True, max_length=80)
    state = models.CharField(null=True, blank=True, max_length=80)
    country = models.CharField(null=True, blank=True, max_length=80)

    class Meta:
    	# db_table = "user_"
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name.strip()

    def clean(self):
        self.username = self.username.lower()

    def save(self, *args, **kwargs):
        # print " >>>>>>>>>>>>>>>>>>>>>> "
        # print "final in save"
        # if self.cover_image:
        #     self.cover_image = compress_image(self.cover_image)
        super(User, self).save(*args, **kwargs)
      
    # def get_json(self):
    #     temp_doc = serializers.serialize('json', [self, ])
    #     doc = json.loads(temp_doc)[0]
    #     if doc['fields']['image']:
    #         doc['fields']['image'] = settings.ELASTICSEARCH_MEDIA_URL + doc['fields']['image']
    #     if doc['fields']['cover_image']:
    #         doc['fields']['cover_image'] = settings.ELASTICSEARCH_MEDIA_URL + doc['fields']['cover_image']
    #     doc['fields']['has_usable_password'] = self.has_usable_password()
    #     return doc
