# Generated by Django 4.0.4 on 2023-01-05 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('huels', '0003_sementry_courses_ic_name_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='sementry',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='huels.courses'),
        ),
    ]