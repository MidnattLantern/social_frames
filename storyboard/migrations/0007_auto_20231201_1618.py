# Generated by Django 3.2.23 on 2023-12-01 16:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('storyboard', '0006_sketchitemcomment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sketchitemcomment',
            options={'ordering': ['creation_date']},
        ),
        migrations.AddField(
            model_name='sketchitemcomment',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
