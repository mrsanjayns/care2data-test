# Generated by Django 5.1 on 2024-09-02 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0002_rename_study_student_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_description',
            new_name='study_description',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_name',
            new_name='study_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_phase',
            new_name='study_phase',
        ),
    ]
