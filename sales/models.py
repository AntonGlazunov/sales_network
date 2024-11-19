from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Factory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', unique=True)
    contact = models.OneToOneField('sales.Contacts', on_delete=models.SET_NULL, verbose_name='Контакты', **NULLABLE)
    product = models.ManyToManyField('sales.Product', verbose_name='Продукты', **NULLABLE)
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания', **NULLABLE)

    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'

    def __str__(self):
        return f'{self.name}'



class Retail(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', unique=True)
    contact = models.OneToOneField('sales.Contacts', on_delete=models.SET_NULL, verbose_name='Контакты', **NULLABLE)
    product = models.ManyToManyField('sales.Product', verbose_name='Продукты', **NULLABLE)
    supplier = models.ForeignKey('sales.Factory', verbose_name='Поставщик', on_delete=models.SET_NULL, **NULLABLE)
    debt = models.IntegerField(verbose_name='Задолженость', help_text='Значение в копейках')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'

    def __str__(self):
        return f'{self.name}'


class IE(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', unique=True)
    contact = models.OneToOneField('sales.Contacts', on_delete=models.SET_NULL, verbose_name='Контакты', **NULLABLE)
    product = models.ManyToManyField('sales.Product', verbose_name='Продукты', **NULLABLE)
    supplier = models.ForeignKey('sales.Retail', verbose_name='Поставщик', on_delete=models.SET_NULL, **NULLABLE)
    debt = models.IntegerField(verbose_name='Задолженость')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Индивидуальный предприниматель'
        verbose_name_plural = 'Индивидуальные предприниматели'

    def __str__(self):
        return f'{self.name}'


class Contacts(models.Model):
    email = models.EmailField(verbose_name='e-mail', unique=True)
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.IntegerField(verbose_name='Номер дома')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f'{self.email}'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    model = models.CharField(max_length=100, verbose_name='Модель')
    date_release = models.DateField(verbose_name='Дата выхода')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name}'

