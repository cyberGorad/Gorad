# Generated by Django 5.1.4 on 2025-01-09 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bandwidthusage',
            name='received',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='bandwidthusage',
            name='sent',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='bandwidthusage',
            name='total',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='establishedconnection',
            name='ip',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='openport',
            name='pid',
            field=models.IntegerField(),
        ),
    ]
