# Generated by Django 3.2.5 on 2021-09-06 07:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0002_alter_comment_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]