# Generated by Django 4.0.2 on 2023-01-06 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('huels', '0007_remove_sementry_ic_name_courses_ic_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='course',
            new_name='reviewed_course',
        ),
    ]