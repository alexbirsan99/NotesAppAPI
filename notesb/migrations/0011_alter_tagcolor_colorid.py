# Generated by Django 3.2.9 on 2022-03-07 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notesb', '0010_alter_note_tagid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagcolor',
            name='colorID',
            field=models.TextField(blank=True, null=True),
        ),
    ]
