# Generated by Django 4.1.2 on 2022-10-05 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Card Name')),
                ('company', models.CharField(max_length=30, verbose_name='Card Company')),
            ],
        ),
    ]
