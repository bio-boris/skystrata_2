# Generated by Django 2.0.7 on 2018-07-24 23:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20180724_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='customer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]