# Generated by Django 4.2.1 on 2023-05-10 12:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_q", "0019_remove_schedule_desired_aligment_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="schedule",
            name="alignment",
            field=models.BooleanField(
                default=False, help_text="If executions should be aligned with interval"
            ),
        ),
    ]