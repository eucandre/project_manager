# Generated by Django 4.2 on 2024-06-09 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_project', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='cost',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]