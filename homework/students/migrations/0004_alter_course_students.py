# Generated by Django 4.2 on 2023-04-21 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(related_name='student_courses', to='students.student'),
        ),
    ]
