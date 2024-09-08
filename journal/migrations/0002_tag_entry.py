# Generated by Django 5.0.7 on 2024-08-18 22:25

import datetime
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('created_on', models.DateTimeField(default=datetime.datetime.now)),
                ('last_modified_on', models.DateTimeField(auto_now=True)),
                ('tags', models.ManyToManyField(related_name='entries', to='journal.tag')),
            ],
        ),
    ]
