# Generated by Django 3.2 on 2021-12-14 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
