# Generated by Django 4.1.2 on 2023-10-05 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='img',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
