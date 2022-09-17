# Generated by Django 4.1.1 on 2022-09-17 10:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0005_remove_subject_enrolled_student_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrolled',
            fields=[
                ('subject_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=200)),
                ('semester', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2)])),
                ('academic_year', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('num_seats', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='enroll_subject',
            field=models.ManyToManyField(blank=True, related_name='studentenroll', to='university.subject'),
        ),
    ]
