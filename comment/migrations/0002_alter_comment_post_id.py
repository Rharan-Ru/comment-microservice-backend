# Generated by Django 4.0 on 2022-01-01 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post_id',
            field=models.IntegerField(),
        ),
    ]
