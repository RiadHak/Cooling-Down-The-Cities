# Generated by Django 4.2.5 on 2023-12-19 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seeders',
            old_name='luchtdruk',
            new_name='AIRQUALITY',
        ),
        migrations.RenameField(
            model_name='seeders',
            old_name='luchtkwaliteit',
            new_name='HUMIDITY',
        ),
        migrations.RenameField(
            model_name='seeders',
            old_name='luchtvochtigheid',
            new_name='PRESSURE',
        ),
        migrations.RenameField(
            model_name='seeders',
            old_name='temperatuur',
            new_name='TEMPERATURE',
        ),
    ]
