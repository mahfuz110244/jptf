# Generated by Django 4.2.6 on 2023-11-10 16:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_alter_user_permanent_address_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birth_certificate_number",
            field=models.BigIntegerField(blank=True, null=True, verbose_name="Birth Certificate Number"),
        ),
        migrations.AlterField(
            model_name="user",
            name="nid",
            field=models.BigIntegerField(blank=True, null=True, verbose_name="NID"),
        ),
    ]
