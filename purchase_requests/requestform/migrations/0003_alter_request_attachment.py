# Generated by Django 3.2.5 on 2022-04-26 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestform', '0002_request_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
