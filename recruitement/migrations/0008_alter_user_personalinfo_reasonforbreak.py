# Generated by Django 4.0.6 on 2023-04-10 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitement', '0007_alter_user_certification_certification_completion_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_personalinfo',
            name='reasonforbreak',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
