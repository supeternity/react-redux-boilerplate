# Generated by Django 2.0.4 on 2018-10-30 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(default='', max_length=20, verbose_name='Телефон'),
        ),
    ]
