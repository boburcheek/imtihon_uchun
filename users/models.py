from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as AbstractUserManager
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(AbstractUserManager):
    def _create_user(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError("Phone number must be set")

        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("for supperusser is_staff must be True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("for supperusser is_superuser must be True")
        if extra_fields.get("is_active") is not True:
            raise ValueError("for supperusser is_active must be True")
        return self._create_user(phone_number, password, **extra_fields)

    def create_user(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = None
    phone_number = PhoneNumberField(unique=True)
    objects = UserManager()

    USERNAME_FIELD = "phone_number"
    EMAIL_FIELD = None
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.phone_number} - {self.id}"


