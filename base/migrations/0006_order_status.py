# Generated by Django 4.2.5 on 2023-11-27 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
