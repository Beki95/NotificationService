# Generated by Django 3.2 on 2022-02-20 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendingMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('text', models.CharField(max_length=100)),
                ('choice_filter', models.CharField(choices=[('tag', 'tag'), ('code', 'code')], default='code', max_length=10)),
                ('end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='client_notifications', to='clients.client')),
                ('sending_message', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='send_notifications', to='notifications.sendingmessages')),
            ],
        ),
    ]
