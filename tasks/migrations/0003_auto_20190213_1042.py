# Generated by Django 2.1.5 on 2019-02-13 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20190213_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]