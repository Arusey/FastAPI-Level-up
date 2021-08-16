from django.db import models
from django.db.models.expressions import F
from django.utils import timezone
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, BaseUserManager)
from django.db import transaction
# Create your models here.





class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """"creates and saves a user with the given email and password"""

        if not email:
            raise ValueError("The email must be provided")
        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise ValueError("User was not created")

    
    def _create_user(self, email, password:None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password:None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_superuser(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    """Implements a fully featured User model"""

    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    second_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # date_joined = models.DateTimeField(default=timezone)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['first_name', 'last_name']


    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        


     #   


    







