# Generated by Django 5.2 on 2025-04-15 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapi', '0003_alter_admin_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]
