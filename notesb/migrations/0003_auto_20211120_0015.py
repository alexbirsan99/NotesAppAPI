# Generated by Django 3.2.9 on 2021-11-19 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notesb', '0002_auto_20211120_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='createDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='modifyDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
