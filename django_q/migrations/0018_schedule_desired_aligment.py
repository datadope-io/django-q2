# Generated by Django 4.2.1 on 2023-05-09 15:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_q", "0017_task_cluster_alter"),
    ]

    operations = [
        migrations.AddField(
            model_name="schedule",
            name="desired_aligment",
            field=models.IntegerField(
                blank=True,
                help_text="Desired alignment of the executions, in seconds. Based on the unix epoch.",
                null=True,
            ),
        ),
    ]