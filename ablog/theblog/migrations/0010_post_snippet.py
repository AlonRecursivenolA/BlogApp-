# Generated by Django 4.2.10 on 2024-02-27 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0009_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='click this to see the post above', max_length=255),
        ),
    ]
