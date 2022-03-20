# Generated by Django 3.2.9 on 2022-03-04 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notesb', '0008_tagnote'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='tagID',
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='colorID',
            field=models.UUIDField(blank=True, null=True),
        ),
    ]