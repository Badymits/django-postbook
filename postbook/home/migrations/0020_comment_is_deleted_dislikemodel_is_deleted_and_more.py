# Generated by Django 4.1 on 2024-03-15 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_comment_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dislikemodel',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='likemodel',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='savedpostsmodel',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
