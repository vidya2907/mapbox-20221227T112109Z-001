# Generated by Django 3.2 on 2021-06-24 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lang', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
