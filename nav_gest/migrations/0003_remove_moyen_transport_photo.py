# Generated by Django 5.0.6 on 2024-08-01 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nav_gest', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moyen_transport',
            name='photo',
        ),
    ]
