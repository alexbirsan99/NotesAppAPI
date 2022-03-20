# Generated by Django 3.2.9 on 2021-12-19 17:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('notesb', '0007_auto_20211219_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagNote',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('tagID', models.UUIDField(null=True)),
                ('noteID', models.UUIDField(null=True)),
            ],
        ),
    ]
