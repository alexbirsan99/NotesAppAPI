# Generated by Django 3.2.9 on 2021-12-19 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notesb', '0006_tagcolors_tags'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Colors',
            new_name='Color',
        ),
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
        migrations.RenameModel(
            old_name='TagColors',
            new_name='TagColor',
        ),
    ]
