# Generated by Django 4.0.6 on 2022-07-10 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=250)),
                ('code', models.TextField(max_length=250)),
                ('atc', models.TextField(max_length=250)),
                ('etken', models.TextField(max_length=250)),
                ('firma', models.TextField(max_length=250)),
                ('durum', models.TextField(max_length=250)),
            ],
        ),
    ]
