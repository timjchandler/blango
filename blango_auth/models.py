from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _


class BlangoUserManager(UserManager):

  def _create_user(self, email, password, **extra_fields):
    if not email:
      raise ValueError("Requires email address")
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self.db)
    return user

  def create_user(self, email, password=None, **extra_fields):
    extra_fields.set_default("is_staff", False)
    extra_fields.set_default("is_superuser", False)
    return self._create_user(email, password, **extra_fields)

  def create_superuser():
    extra_fields.set_default("is_staff", True)
    extra_fields.set_default("is_superuser", True)
    
    if extra_fields.get("is_staff") is not True:
      raise ValueError("superuser must have is_staff=True")
    if extra_fields.get("is_superuser") is not True:
      raise ValueError("superuser must have is_superuser=True")

    return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
  username = None 
  email = models.EmailField(
    _("email address"),
    unique=True,
  )

  objects = BlangoUserManager()

  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = []

  def __str__(self):
    return self.email

  