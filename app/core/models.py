"""
Datebase models.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):  # user model manager
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save, and return a new user."""

        # Another thing to note is that Manager methods can access
        # self.model to get the model class to which they’re attached.
        if not email:
            raise ValueError('User must have an email address.')

        # self.model -> User
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        # Support adding multiple db(s)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Assign UserManager to User
    objects = UserManager()

    # Field that we want to use for authentication
    USERNAME_FIELD = 'email'
