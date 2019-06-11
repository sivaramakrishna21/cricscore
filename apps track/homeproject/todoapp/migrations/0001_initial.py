# Generated by Django 2.2.1 on 2019-06-07 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todoitem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=128)),
                ('duedate', models.DateField()),
                ('completed', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'todoitem',
            },
        ),
        migrations.CreateModel(
            name='Todolist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'todolist',
            },
        ),
    ]
