# Generated by Django 3.2.5 on 2022-04-28 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("requestform", "0003_alter_request_attachment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="request",
            name="state",
        ),
    ]
