# Generated by Django 5.2 on 2025-04-16 09:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapi', '0006_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=500, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmsapi.student')),
            ],
        ),
    ]
