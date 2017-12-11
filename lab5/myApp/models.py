from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,
    AbstractUser)
from django.contrib.postgres import fields
from django.db import models

# Create your models here.
from django.utils import six


class Products(models.Model):
    name = models.CharField(max_length=100, null=True)
    specifications = fields.JSONField(null=True)
    price = fields.FloatRangeField(null=True)


class UserShop(AbstractUser):
    username = fields.CICharField(max_length=20, unique=True, null=True)
    first_name = fields.CICharField(max_length=50, null=True)
    last_name = fields.CICharField(max_length=50, null=True)
    email = fields.CIEmailField(null=True)

    date_of_birth = fields.DateRangeField(null=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'

    class Meta(AbstractBaseUser.Meta):
        swappable = 'AUTH_USER_MODEL'
