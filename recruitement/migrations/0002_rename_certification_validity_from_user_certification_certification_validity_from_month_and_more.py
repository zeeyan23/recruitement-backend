# Generated by Django 4.0.6 on 2023-04-11 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_certification',
            old_name='certification_validity_from',
            new_name='certification_validity_from_month',
        ),
        migrations.RenameField(
            model_name='user_certification',
            old_name='certification_validity_to',
            new_name='certification_validity_from_year',
        ),
        migrations.AddField(
            model_name='user_certification',
            name='certification_validity_to_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user_certification',
            name='certification_validity_to_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patent',
            name='issue_date_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patent',
            name='issue_date_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_workstatus',
            name='duration_to_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_workstatus',
            name='duration_to_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
