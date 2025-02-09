# Generated by Django 5.0.2 on 2024-02-20 15:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_remove_dislikemodel_user_remove_likemodel_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dislikemodel',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='comment_dislikes', to='home.comment'),
        ),
        migrations.AlterField(
            model_name='dislikemodel',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='post_dislikes', to='home.post'),
        ),
        migrations.AlterField(
            model_name='likemodel',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='comment_likes', to='home.comment'),
        ),
        migrations.AlterField(
            model_name='likemodel',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='post_likes', to='home.post'),
        ),
    ]
