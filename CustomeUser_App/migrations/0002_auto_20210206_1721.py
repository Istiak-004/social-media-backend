# Generated by Django 3.1.6 on 2021-02-06 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CustomeUser_App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newuser',
            old_name='user_name',
            new_name='username',
        ),
    ]
