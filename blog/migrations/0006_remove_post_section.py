# Generated by Django 4.1.7 on 2023-03-18 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='section',
        ),
    ]
