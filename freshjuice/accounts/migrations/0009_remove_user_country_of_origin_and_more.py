# Generated by Django 5.1.2 on 2024-10-23 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='country_of_origin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='current_city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='current_country_or_residence',
        ),
        migrations.RemoveField(
            model_name='user',
            name='current_county',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='level_of_education',
        ),
        migrations.RemoveField(
            model_name='user',
            name='national_identification_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='school_affiliate',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='country_of_origin',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='current_city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='current_country_or_residence',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='current_county',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='level_of_education',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='national_identification_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='school_affiliate',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]