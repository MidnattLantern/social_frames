# Generated by Django 3.2.23 on 2023-12-18 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storyboard', '0004_alter_projectitem_project_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectitem',
            name='project_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]