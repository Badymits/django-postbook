# Generated by Django 5.0.2 on 2024-02-13 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_post_dislikes_post_likes_alter_post_image_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(blank=True, max_length=955, null=True),
        ),
    ]
