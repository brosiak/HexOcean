# Generated by Django 3.2.4 on 2021-06-28 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tier',
            old_name='has_fetched_url',
            new_name='can_fetch_url',
        ),
    ]