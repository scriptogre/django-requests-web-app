# Generated by Django 3.2.12 on 2022-06-16 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('requisitionform', '0003_rename_type_requisition_requisition_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisition',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
