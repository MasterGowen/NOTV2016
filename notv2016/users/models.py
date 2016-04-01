from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Необходимо ввести электронный адрес')

        user = self.model(
            email=UserManager.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(password=password,
                                email=email)
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
        max_length=1024,
        blank=True,
    )

    position = models.CharField(
        verbose_name='Должность',
        max_length=255,
        blank=True,
    )

    tel = models.CharField(
        verbose_name='Телефон',
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

    is_active = models.BooleanField(
        verbose_name='Активный',
        default=True,
    )


    is_paid = models.BooleanField(
        verbose_name='Оплатил',
        default=False,
    )

    online = 'online'
    offline = 'offline'
    STATUS = (
        (online, 'Заочно'),
        (offline, 'Очно')
    )

    status = models.CharField("Статус", max_length=7, choices=STATUS, default=offline)

    date = models.DateField(auto_now_add=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        return '%s %s' % (self.last_name,
                          self.first_name,)

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Meta:
    verbose_name = ('Пользователь')
    verbose_name_plural = ('Пользователи')
