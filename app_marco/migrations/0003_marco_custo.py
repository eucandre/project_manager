# Generated by Django 2.2 on 2023-01-18 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_marco', '0002_marco_id_projeto'),
    ]

    operations = [
        migrations.AddField(
            model_name='marco',
            name='custo',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
