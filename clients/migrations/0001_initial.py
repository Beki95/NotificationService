# Generated by Django 3.2 on 2022-02-19 16:15

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('mobile_code', models.IntegerField()),
                ('tag', models.CharField(max_length=10)),
                ('time_zone', models.CharField(max_length=20)),
            ],
        ),
    ]
