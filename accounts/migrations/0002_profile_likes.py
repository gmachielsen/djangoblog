# Generated by Django 2.0.6 on 2018-08-13 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20180810_0901'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='likes',
            field=models.ManyToManyField(related_name='liked_by', to='posts.Post'),
        ),
    ]
