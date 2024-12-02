# Generated by Django 5.1.2 on 2024-10-24 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_userprofile_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='receive_newsletter',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='receive_newsletter',
            field=models.BooleanField(default=False),
        ),
    ]