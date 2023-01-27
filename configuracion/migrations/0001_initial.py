# Generated by Django 4.1.1 on 2023-01-26 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.TextField(max_length=50, verbose_name='Correo')),
                ('password', models.TextField(max_length=50, verbose_name='Password')),
                ('perfil', models.TextField(max_length=255, verbose_name='Profile')),
                ('userestado', models.TextField(max_length=1, verbose_name='Userestado')),
                ('empleadoid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.empleado', verbose_name='Empleado')),
            ],
        ),
    ]
