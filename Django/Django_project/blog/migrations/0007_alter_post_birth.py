# Generated by Django 4.1 on 2023-01-12 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_remove_post_bool_post_b"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="birth",
            field=models.DateField(),
        ),
    ]
