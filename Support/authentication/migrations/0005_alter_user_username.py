# Generated by Django 3.2.5 on 2021-09-03 07:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(db_index=True, max_length=54, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_username', inverse_match=True, message='Only use letters, numbers - and _', regex='[^0-9a-zA-Z-_]')]),
        ),
    ]
