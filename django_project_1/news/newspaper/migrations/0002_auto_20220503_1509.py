# Generated by Django 2.2 on 2022-05-03 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['created_at']},
        ),
    ]
