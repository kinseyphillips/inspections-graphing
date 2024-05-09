# Generated by Django 5.0.6 on 2024-05-09 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Features_Graph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(blank=True, max_length=100, unique=True)),
                ('percent', models.FloatField()),
            ],
        ),
    ]