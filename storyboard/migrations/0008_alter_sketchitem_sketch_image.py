# Generated by Django 3.2.23 on 2023-12-17 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storyboard', '0007_alter_sketchitem_sketch_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sketchitem',
            name='sketch_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
