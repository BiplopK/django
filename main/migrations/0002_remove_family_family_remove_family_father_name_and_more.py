# Generated by Django 5.1.7 on 2025-03-11 09:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="family",
            name="family",
        ),
        migrations.RemoveField(
            model_name="family",
            name="father_name",
        ),
        migrations.RemoveField(
            model_name="family",
            name="mother_name",
        ),
        migrations.AddField(
            model_name="family",
            name="father",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="father_of_families",
                to="main.users",
            ),
        ),
        migrations.AddField(
            model_name="family",
            name="mother",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="mother_f_families",
                to="main.users",
            ),
        ),
        migrations.AddField(
            model_name="users",
            name="Isdeleted",
            field=models.BooleanField(default=False),
        ),
    ]
