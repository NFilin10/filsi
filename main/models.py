from django.db import models

class SliderInfo(models.Model):
    title = models.CharField('Заголовок', max_length=80)
    slider_content = models.TextField('Контент')

    class Meta:
        verbose_name = 'Slider Info'
        verbose_name_plural = 'Slider Info'

class About(models.Model):
    title1 = models.CharField('Заголовок1', max_length=80)
    about_content1 = models.TextField('Контент')
    title2 = models.CharField('Заголовок2', max_length=80)
    about_content2 = models.TextField('Контент')

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'about'

class Kontakt(models.Model):
    name = models.CharField('Имя', max_length=30)
    position = models.CharField('Должность', max_length=30)
    email = models.CharField('Почта', max_length=30)
    telefon = models.CharField('Телефон', max_length=30)
    second_telefon = models.CharField('Второй телефон', max_length=30)

    class Meta:
        verbose_name = 'Kontakts'
        verbose_name_plural = 'Kontakt'

