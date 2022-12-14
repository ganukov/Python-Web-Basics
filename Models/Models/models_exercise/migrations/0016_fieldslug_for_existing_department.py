# Generated by Django 4.1 on 2022-10-15 10:34

from django.db import migrations
from django.utils.text import slugify


def add_slugs(apps, schema_editor):
    Department = apps.get_model("models_exercise", "Department")
    departments = Department.objects.all()

    for department in departments:
        department.slug = slugify(department.name)

    Department.objects.bulk_update(departments,['slug'])


class Migration(migrations.Migration):
    dependencies = [
        ('models_exercise', '0015_department_slug'),
    ]

    operations = [
        migrations.RunPython(add_slugs)
    ]
