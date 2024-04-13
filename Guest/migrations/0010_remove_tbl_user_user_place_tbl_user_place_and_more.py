# Generated by Django 5.0.1 on 2024-02-06 13:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0007_tbl_place'),
        ('Guest', '0009_remove_tbl_user_user_district'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_user',
            name='user_place',
        ),
        migrations.AddField(
            model_name='tbl_user',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place'),
        ),
        migrations.AlterField(
            model_name='tbl_user',
            name='user_contact',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='tbl_user',
            name='user_email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tbl_user',
            name='user_password',
            field=models.CharField(max_length=50),
        ),
    ]