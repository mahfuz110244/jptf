# Generated by Django 4.2.6 on 2023-11-10 16:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_user_jptf_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="jptf_id",
        ),
        migrations.AddField(
            model_name="user",
            name="birth_certificate_number",
            field=models.IntegerField(blank=True, max_length=25, null=True, verbose_name="Birth Certificate Number"),
        ),
        migrations.AddField(
            model_name="user",
            name="blood_group",
            field=models.CharField(blank=True, max_length=255, verbose_name="Blood Group"),
        ),
        migrations.AddField(
            model_name="user",
            name="education_qualification",
            field=models.CharField(blank=True, max_length=255, verbose_name="Education Qualification"),
        ),
        migrations.AddField(
            model_name="user",
            name="father_mobile_number",
            field=models.CharField(blank=True, max_length=11, verbose_name="Father's Mobile Number"),
        ),
        migrations.AddField(
            model_name="user",
            name="is_verified",
            field=models.BooleanField(default=False, verbose_name="Is Verified"),
        ),
        migrations.AddField(
            model_name="user",
            name="mother_mobile_number",
            field=models.CharField(blank=True, max_length=11, verbose_name="Mother's Mobile Number"),
        ),
        migrations.AddField(
            model_name="user",
            name="nationality",
            field=models.CharField(blank=True, max_length=255, verbose_name="Nationality"),
        ),
        migrations.AddField(
            model_name="user",
            name="nid",
            field=models.IntegerField(blank=True, max_length=20, null=True, verbose_name="NID"),
        ),
        migrations.AddField(
            model_name="user",
            name="party_designation",
            field=models.CharField(blank=True, max_length=255, verbose_name="Party Designation"),
        ),
        migrations.AddField(
            model_name="user",
            name="party_id",
            field=models.CharField(blank=True, max_length=255, verbose_name="Party ID"),
        ),
        migrations.AddField(
            model_name="user",
            name="party_join_date",
            field=models.DateField(blank=True, null=True, verbose_name="Party Join Date"),
        ),
        migrations.AddField(
            model_name="user",
            name="party_type",
            field=models.CharField(blank=True, max_length=255, verbose_name="Party Type"),
        ),
        migrations.AddField(
            model_name="user",
            name="permanent_address",
            field=models.CharField(blank=True, max_length=255, verbose_name="Permanent Address"),
        ),
        migrations.AddField(
            model_name="user",
            name="present_address",
            field=models.CharField(blank=True, max_length=255, verbose_name="Present Address"),
        ),
        migrations.AddField(
            model_name="user",
            name="present_education",
            field=models.CharField(blank=True, max_length=255, verbose_name="Present Education"),
        ),
        migrations.AddField(
            model_name="user",
            name="profession",
            field=models.CharField(blank=True, max_length=255, verbose_name="Profession"),
        ),
        migrations.AddField(
            model_name="user",
            name="profile_picture",
            field=models.ImageField(blank=True, null=True, upload_to="profile_pictures/"),
        ),
        migrations.AddField(
            model_name="user",
            name="religion",
            field=models.CharField(blank=True, max_length=255, verbose_name="Religion"),
        ),
        migrations.AddField(
            model_name="user",
            name="signature_picture",
            field=models.ImageField(blank=True, null=True, upload_to="signature_pictures/"),
        ),
    ]
