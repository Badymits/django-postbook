# Generated by Django 5.0.2 on 2024-02-13 04:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_post_body'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislikes',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=955)),
                ('image', models.ImageField(blank=True, default='images', null=True, upload_to='')),
                ('likes', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('dislikes', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('main_comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.comment')),
                ('main_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
