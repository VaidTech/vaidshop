# Generated by Django 3.0.3 on 2020-02-13 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20200205_0003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['-created_at']},
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='timestamp',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='updated',
            new_name='updated_at',
        ),
    ]
