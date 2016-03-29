from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Необходимо ввести электронный адрес')

        user = self.model(
            email=UserManager.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email,
                                password=password,
                                username=username)
        user.is_admin = True
        user.save(using=self._db)
        return user


class NOTVUser(AbstractBaseUser):
    """
    Пользователь
    """
    email = models.EmailField(
        verbose_name='Электронная почта',
        max_length=32,
        unique=True,
        db_index=True,
    )

    avatar = models.ImageField(
        verbose_name='Аватар',
        upload_to='images/%Y/%m',
        blank=True,
    )

    first_name = models.CharField(
        verbose_name='Имя',
        max_length=16,
        blank=True,
    )

    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=32,
        blank=True,
    )

    department = models.CharField(
        verbose_name='Университет/Подразделение',
        max_length=255,
        blank=True,
    )

    is_admin = models.BooleanField(
        verbose_name='Является администратором?',
        default=False,
    )

    is_superuser = models.BooleanField(
        verbose_name='Является суперпользователем?',
        default=False,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def get_full_name(self):
        return '%s %s' % (self.last_name,
                          self.first_name,)

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin


class Meta:
    verbose_name = ('Пользователь')
    verbose_name_plural = ('Пользователи')