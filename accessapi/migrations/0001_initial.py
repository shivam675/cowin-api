# Generated by Django 3.2 on 2021-05-05 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pincode', models.IntegerField(default='000000')),
                ('date_of_check', models.CharField(default='00-00-0000', max_length=10)),
            ],
        ),
    ]