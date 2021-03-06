# Generated by Django 3.2 on 2021-12-14 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_alter_work_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Built',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, max_length=50)),
                ('frontend_framework', models.CharField(blank=True, max_length=50)),
                ('backend_framework', models.CharField(blank=True, max_length=50)),
                ('database', models.CharField(blank=True, max_length=50)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.work')),
            ],
        ),
    ]
