# Generated by Django 5.1.6 on 2025-04-10 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_userselection_user_selection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='industry_mapping',
            name='id',
        ),
        migrations.AlterField(
            model_name='industry_mapping',
            name='industry_name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
