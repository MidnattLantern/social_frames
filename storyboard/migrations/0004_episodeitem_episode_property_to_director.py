# Generated by Django 3.2.23 on 2023-12-15 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('storyboard', '0003_alter_projectitem_project_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='episodeitem',
            name='episode_property_to_director',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
