from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, mobile_number, otp, **extra_fields):
        user = self.model(mobile_number=mobile_number, otp=otp, **extra_fields)
        user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile_number, otp, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(mobile_number, otp, **extra_fields)
