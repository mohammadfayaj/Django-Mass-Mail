# Generated by Django 3.1.7 on 2021-04-13 05:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mass_mail', '0002_auto_20210413_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selectuser',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
