# Generated by Django 5.0 on 2024-01-09 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electro_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_request',
            name='date',
            field=models.CharField(max_length=20),
        ),
    ]
