# Generated by Django 4.2.6 on 2023-11-10 12:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="jptf_id",
            field=models.CharField(blank=True, max_length=255, verbose_name="JPTF ID"),
        ),
    ]
