# Generated by Django 4.0 on 2021-12-13 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('img', models.CharField(max_length=255)),
            ],
        ),
    ]
