# Generated by Django 4.2.7 on 2023-11-12 16:18

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name="Ім'я")),
                ('surname', models.CharField(max_length=100, verbose_name='Прізвище')),
                ('bio', models.TextField(blank=True, max_length=1000, verbose_name='Біографія')),
                ('avatar', models.ImageField(upload_to='profile/%Y/%m/%d/')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Користувач')),
            ],
        ),
    ]