# Generated by Django 4.2.5 on 2023-12-20 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_rename_airquality_seeders_luchtdruk_and_more'),
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