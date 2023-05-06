from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, image=None, role=None, job=None, workplace=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            image=image,
            role=role,
            job=job,
            workplace=workplace,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, image=None, role='admin', job=None, workplace=None):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
            image=image,
            role=role,
            job=job,
            workplace=workplace,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    username = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='users/', null=True, blank=True)
    role = models.CharField(max_length=10, choices=[('admin', 'Admin'), ('guest', 'Guest')], default='guest')
    job = models.CharField(max_length=100, null=True, blank=True)
    workplace = models.CharField(max_length=100, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
