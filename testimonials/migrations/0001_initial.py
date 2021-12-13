# Generated by Django 4.0 on 2021-12-13 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('img', models.CharField(max_length=50)),
                ('icon', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=50)),
                ('social', models.CharField(max_length=50)),
                ('featured', models.BooleanField()),
            ],
        ),
    ]
