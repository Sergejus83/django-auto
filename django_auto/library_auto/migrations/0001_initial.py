# Generated by Django 4.1.3 on 2022-11-07 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_auto', models.CharField(help_text='Enter name of car', max_length=100, verbose_name='Auto name')),
                ('model_auto', models.CharField(help_text='Enter model of car', max_length=100, verbose_name='Auto model')),
            ],
        ),
    ]
