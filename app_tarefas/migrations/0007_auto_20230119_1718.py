# Generated by Django 2.2 on 2023-01-19 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tarefas', '0006_tarefa_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='updated_at',
            field=models.DateField(default=None),
        ),
    ]
