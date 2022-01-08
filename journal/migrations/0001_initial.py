# Generated by Django 4.0 on 2022-01-04 01:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_name', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField()),
            ],
        ),
    ]