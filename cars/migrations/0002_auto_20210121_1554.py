# Generated by Django 3.1.5 on 2021-01-21 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'Автомобиль', 'verbose_name_plural': 'Автомобили'},
        ),
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'verbose_name': 'Производитель', 'verbose_name_plural': 'Производители'},
        ),
    ]
