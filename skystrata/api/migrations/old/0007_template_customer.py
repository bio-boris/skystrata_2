# Generated by Django 2.0.7 on 2018-07-23 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_provideroption_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Customer'),
            preserve_default=False,
        ),
    ]
