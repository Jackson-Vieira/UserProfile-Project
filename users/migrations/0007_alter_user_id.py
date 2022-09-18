# Generated by Django 4.1.1 on 2022-09-17 15:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_birth_date_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('00740d4f-71d5-4297-9a89-f2feda5a6dce'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
