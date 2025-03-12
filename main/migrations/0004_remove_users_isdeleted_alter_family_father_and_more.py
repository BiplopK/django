# Generated by Django 5.1.7 on 2025-03-11 09:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_users_is_deleted"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="users",
            name="Isdeleted",
        ),
        migrations.AlterField(
            model_name="family",
            name="father",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="father_of_families",
                to="main.users",
            ),
        ),
        migrations.AlterField(
            model_name="family",
            name="mother",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="mother_f_families",
                to="main.users",
            ),
        ),
    ]
