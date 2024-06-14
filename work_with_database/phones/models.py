from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=25)
    price = models.DecimalField(verbose_name='Цена', max_digits=8, decimal_places=2)
    image = models.ImageField('Фото')
    release_date = models.DateTimeField(verbose_name='Дата релиза', auto_now=True)
    lte_exists = models.BooleanField(default=True, verbose_name='Наличие')
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")

    def __str__(self):
        return self.name
