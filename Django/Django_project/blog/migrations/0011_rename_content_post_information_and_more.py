# Generated by Django 4.1 on 2023-01-13 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0010_post_hobby_post_need_post_url1_post_url2"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="content",
            new_name="information",
        ),
        migrations.RenameField(
            model_name="post",
            old_name="title",
            new_name="name",
        ),
    ]
