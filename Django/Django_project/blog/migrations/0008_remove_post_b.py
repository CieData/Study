# Generated by Django 4.1 on 2023-01-12 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_alter_post_birth"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="b",
        ),
    ]
