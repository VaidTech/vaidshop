# Generated by Django 3.0.3 on 2020-03-04 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendences', '0009_auto_20200303_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='exit_time',
            field=models.TimeField(blank=True, help_text='When you get home from work, fill out this field', null=True),
        ),
    ]
