# Generated by Django 4.1.2 on 2022-10-06 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bonus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cashback', models.IntegerField(verbose_name='Cashback Percentage')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30, verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='DateRanges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Quarter')),
                ('active_start', models.DateField(verbose_name='Activate Date Start')),
                ('active_end', models.DateField(verbose_name='Activate Date End')),
            ],
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Card Name')),
                ('company', models.CharField(max_length=30, verbose_name='Card Company')),
                ('bonuses', models.ManyToManyField(to='creditspreadit.bonus', verbose_name='Bonuses')),
            ],
        ),
        migrations.AddField(
            model_name='bonus',
            name='category',
            field=models.ManyToManyField(to='creditspreadit.category', verbose_name='Bonus Category'),
        ),
        migrations.AddField(
            model_name='bonus',
            name='dates',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='creditspreadit.dateranges', verbose_name='Active Date Range'),
        ),
    ]