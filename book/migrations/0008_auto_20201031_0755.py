# Generated by Django 3.1 on 2020-10-31 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_auto_20201031_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='phone',
            field=models.PositiveBigIntegerField(null=True),
        ),
    ]
