# Generated by Django 3.1.1 on 2020-09-14 12:36

from django.db import migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='bio',
            field=django_markdown.models.MarkdownField(blank=True),
        ),
    ]
