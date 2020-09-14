# Generated by Django 3.0.5 on 2020-09-14 12:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.CharField(max_length=9)),
                ('batch', models.CharField(max_length=4)),
                ('bio', models.TextField(blank=True)),
                ('linkedin', models.URLField(null=True)),
                ('github', models.URLField(null=True)),
                ('instagram', models.URLField(null=True)),
                ('facebook', models.URLField(null=True)),
                ('twitter', models.URLField(null=True)),
                ('clubs', models.CharField(blank=True, max_length=300)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
