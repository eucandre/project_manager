# Generated by Django 2.2 on 2023-01-18 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Marco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('inicio', models.DateField()),
                ('fim', models.DateField()),
                ('objetivo', models.TextField()),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('integrantes', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='names', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Marco de tarefas realizadas',
            },
        ),
    ]
