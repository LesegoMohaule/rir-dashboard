# Generated by Django 3.2.8 on 2022-01-25 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rir_data', '0020_auto_20220120_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicator',
            name='max_value',
            field=models.FloatField(default=100, help_text='Maximum value for the indicator that can received', verbose_name='Maximum Value'),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='min_value',
            field=models.FloatField(default=0, help_text='Minimum value for the indicator that can received', verbose_name='Minimum Value'),
        ),
    ]
