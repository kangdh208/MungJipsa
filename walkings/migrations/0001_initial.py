# Generated by Django 3.2.13 on 2022-11-28 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manageNo', models.CharField(max_length=200)),
                ('parkName', models.CharField(max_length=300)),
                ('parkType', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('latitude', models.CharField(max_length=200)),
                ('longitude', models.CharField(max_length=200)),
                ('size', models.CharField(max_length=200)),
            ],
        ),
    ]