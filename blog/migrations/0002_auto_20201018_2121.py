# Generated by Django 3.1.2 on 2020-10-18 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='data_posted',
            new_name='date_posted',
        ),
    ]
