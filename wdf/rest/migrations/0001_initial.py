# Generated by Django 3.2.9 on 2021-11-28 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name='date created')),
                ('user_id', models.IntegerField()),
            ],
        ),
    ]
