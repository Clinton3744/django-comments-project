# Generated by Django 4.2.5 on 2023-09-29 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('commands', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
