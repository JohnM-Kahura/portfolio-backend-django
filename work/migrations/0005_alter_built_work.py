# Generated by Django 3.2 on 2021-12-14 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0004_auto_20211214_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='built',
            name='work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='built', to='work.work'),
        ),
    ]
