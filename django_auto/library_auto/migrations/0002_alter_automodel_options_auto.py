# Generated by Django 4.1.3 on 2022-11-07 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library_auto', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='automodel',
            options={'ordering': ['name_auto', 'model_auto']},
        ),
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate_number', models.CharField(max_length=50, verbose_name='license plate number')),
                ('vin_code', models.CharField(max_length=50, verbose_name='VIN code')),
                ('client', models.CharField(max_length=100, verbose_name='client')),
                ('model_auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_auto.automodel', verbose_name='auto model')),
            ],
        ),
    ]