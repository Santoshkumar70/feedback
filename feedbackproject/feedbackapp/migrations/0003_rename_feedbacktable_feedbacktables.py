# Generated by Django 5.0.1 on 2024-01-18 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedbackapp', '0002_rename_feedbackmodel_feedbacktable'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='feedbacktable',
            new_name='feedbacktables',
        ),
    ]
