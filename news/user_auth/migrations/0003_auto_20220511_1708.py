# Generated by Django 2.2 on 2022-05-11 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_auto_20220511_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=11, verbose_name='Номер телефона'),
        ),
    ]
