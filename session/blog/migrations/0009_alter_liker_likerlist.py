# Generated by Django 4.2 on 2023-04-13 08:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_remove_comment_liker_blog_liker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liker',
            name='likerList',
            field=models.ManyToManyField(related_name='likerList', to=settings.AUTH_USER_MODEL),
        ),
    ]
