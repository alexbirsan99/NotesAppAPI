# Generated by Django 3.2.9 on 2022-03-16 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notesb', '0011_alter_tagcolor_colorid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='colorID',
            field=models.TextField(blank=True, null=True),
        ),
    ]
