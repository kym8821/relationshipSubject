# Generated by Django 4.2 on 2023-04-13 07:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_remove_blog_liker_blog_liker'),
    ]

    operations = [
        migrations.RenameField(
            model_name='liker',
            old_name='times',
            new_name='likeTimes',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='likeTimes',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='liker',
        ),
        migrations.AddField(
            model_name='comment',
            name='liker',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.liker'),
        ),
        migrations.AddField(
            model_name='liker',
            name='likerList',
            field=models.ManyToManyField(related_name='liker', to=settings.AUTH_USER_MODEL),
        ),
    ]