from django.contrib.auth.models import AbstractUser
from django.db import models

""" Модель пользователя для регистрации"""


class User(AbstractUser):
    class Role(models.TextChoices):
        ANONYM = "anonym", "Anonym"
        USER = "user", "User"
        ADMIN = "admin", "Admin"

    email = models.EmailField(blank=False, unique=True,
                              verbose_name="Электронная почта")
    bio = models.TextField(blank=True, verbose_name="Биография")
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.USER,
        verbose_name="Роль"
    )
    confirmation_code = models.CharField(max_length=100, blank=True,
                                         verbose_name="Код подтверждения")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class CharacterCard(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя персонажа")
    number = models.IntegerField(null=True, blank=True, verbose_name="Уникальный номер")
    status = models.IntegerField(null=True, blank=True, verbose_name="Статус карты")
    position = models.IntegerField(null=True, blank=True, verbose_name="Порядковый номер на поле")
    killer_status = models.IntegerField(null=True, blank=True, verbose_name="Статус убийцы")
    police_status = models.IntegerField(null=True, blank=True, verbose_name="Статус инспектора")
    image_back = models.ImageField(upload_to="nuar/", null=True, blank=True,
                              verbose_name="Картинка рубашки карты")
    image_front = models.ImageField(upload_to="nuar/", null=True, blank=True,
                              verbose_name="Картинка лицевой стороны карты")
    image_dead = models.ImageField(upload_to="nuar/", null=True, blank=True,
                              verbose_name="Картинка 'погиб'")
    image_acquitted = models.ImageField(upload_to="nuar/", null=True, blank=True,
                              verbose_name="Картинка 'невиновен'")
    class Meta:
        verbose_name = "Карта персонажа"
        verbose_name_plural = "Карты персонажа"

    def __str__(self):
        return self.name
