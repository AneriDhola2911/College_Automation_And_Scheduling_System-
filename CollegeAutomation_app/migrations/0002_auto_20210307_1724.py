# Generated by Django 3.1.7 on 2021-03-07 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CollegeAutomation_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavereportstudent',
            name='leave_status',
            field=models.IntegerField(default=0),
        ),
    ]
