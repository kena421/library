# Generated by Django 4.2.10 on 2024-02-15 14:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="circulation",
            old_name="book_id",
            new_name="book",
        ),
        migrations.RenameField(
            model_name="circulation",
            old_name="member_id",
            new_name="member",
        ),
        migrations.RenameField(
            model_name="reservation",
            old_name="book_id",
            new_name="book",
        ),
        migrations.RenameField(
            model_name="reservation",
            old_name="member_id",
            new_name="member",
        ),
    ]
