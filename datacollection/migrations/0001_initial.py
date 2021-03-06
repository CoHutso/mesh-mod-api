# Generated by Django 3.2.6 on 2021-08-29 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('age', models.IntegerField()),
                ('reg_date', models.DateTimeField(auto_now=True, verbose_name='registration date')),
            ],
        ),
    ]
