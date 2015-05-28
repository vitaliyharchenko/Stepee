# coding=utf-8
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.core.mail import send_mail
from django.utils import timezone

from teaching.models import Grade


class AbstractUserManager(BaseUserManager):
    # TODO: при создании юзера открывать ему только первые главы в предметах
    # TODO: refactoring users creation, add grade selection
    # create user with options is staff and etc
    def _create_user(self, email, password, is_staff, is_superuser, first_name, last_name, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('Email должен быть задан')
        email = self.normalize_email(email)
        is_active = extra_fields.pop("is_active", True)
        # TODO: grade not null
        grade = extra_fields.pop("grade", False)
        user = self.model(
            email=self.normalize_email(email),
            is_staff=is_staff,
            is_active=is_active,
            is_superuser=is_superuser,
            first_name=first_name,
            last_name=last_name,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # create regular user
    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class AbstractUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Email', max_length=255, unique=True, db_index=True)

    is_staff = models.BooleanField('Статус сотрудника', default=False,
                                   help_text="Определяет , может ли пользователь войти в админку")
    is_active = models.BooleanField('Активность', default=True,
                                    help_text="Сделайте неактивным вместо удаления аккаунта")

    date_joined = models.DateTimeField('Дата регистрации', default=timezone.now)
    # bdate = models.DateField('Дата рождения', auto_now_add=False)

    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)

    grade = models.ForeignKey(Grade, blank=True, null=True)
    # vkuserid = models.IntegerField(unique=True, null=True, blank=True)
    # sex = models.CharField(max_length=1, choices=(('m', 'М'), ('f', 'Ж')), verbose_name='Пол')
    # phone = PhoneNumberField(verbose_name='Телефон', help_text='В формате +7xxxxxxxxxx', unique=True)
    # TODO: setup phonenumber_field
    # city = models.ForeignKey(City)
    # TODO: add city model
    # school = models.ForeignKey(School)
    # TODO: add school model
    # stats = models.OneToOneField('customuser.UserLearnStats', verbose_name='Учебная статистика')
    # TODO: add stats model
    # settings = models.OneToOneField('users.UserSettings', verbose_name='Настройки')
    # TODO: add settings model

    objects = AbstractUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'
        abstract = True

    def get_full_name(self):
        return u'{} {}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __unicode__(self):
        return u'{} {}'.format(self.first_name, self.last_name)


class User(AbstractUser):

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'