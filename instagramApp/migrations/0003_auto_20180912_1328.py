# Generated by Django 2.1.1 on 2018-09-12 13:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('instagramApp', '0002_auto_20180911_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='instagram',
            name='followers',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='instagram',
            name='followings',
            field=models.IntegerField(null=True),
        ),
    ]