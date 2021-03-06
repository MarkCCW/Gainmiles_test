# Generated by Django 2.2 on 2022-06-20 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sex', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=100)),
                ('group', models.CharField(max_length=50)),
                ('last_modify_date', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
