# Generated by Django 4.0.6 on 2023-04-10 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitement', '0006_rename_certification_validity_user_certification_certification_validity_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_certification',
            name='certification_completion_id',
            field=models.CharField(max_length=50),
        ),
    ]
