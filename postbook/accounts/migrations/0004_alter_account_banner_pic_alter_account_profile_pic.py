# Generated by Django 5.0.2 on 2024-03-01 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_banner_pic_alter_account_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='banner_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile/images/'),
        ),
        migrations.AlterField(
            model_name='account',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile/images/'),
        ),
    ]
