# Generated by Django 4.2.4 on 2024-01-27 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_teacher_out_of_department_alter_routine_session_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='post',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
