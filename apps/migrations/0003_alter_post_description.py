# Generated by Django 4.2.3 on 2023-07-08 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_alter_post_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
