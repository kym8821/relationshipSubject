# Generated by Django 4.2 on 2023-04-12 11:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_tag_blog_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Liker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('times', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'liker',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='likeTimes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='blog',
            name='liker',
            field=models.ManyToManyField(related_name='liker', to=settings.AUTH_USER_MODEL),
        ),
    ]
