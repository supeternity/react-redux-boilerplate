# Generated by Django 2.0 on 2019-07-22 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0002_auto_20190722_1646'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientlink',
            options={'ordering': ('-created_dt', '-modified_dt'), 'verbose_name': 'Клиентская ссылка', 'verbose_name_plural': 'Клиентские ссылки'},
        ),
    ]
