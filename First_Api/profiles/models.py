from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from user_profile.models import User

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ DataBase Model for UserProfile """
    email = models.EmailField(max_length=254 , unique = True)
    name = models.CharField(max_length=250)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['name']
    
    def get_full_name(self):
        """ Get the full name of user"""
        return self.name
    