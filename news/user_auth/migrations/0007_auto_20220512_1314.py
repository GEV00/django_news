# Generated by Django 2.2 on 2022-05-12 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0006_auto_20220512_1132'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': (('verify', 'Can Verify Users'),)},
        ),
    ]
