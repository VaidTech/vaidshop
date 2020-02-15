# Generated by Django 3.0.3 on 2020-02-15 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0002_auto_20200205_0003'),
        ('employees', '0003_auto_20200213_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='owners.Owner'),
        ),
    ]
