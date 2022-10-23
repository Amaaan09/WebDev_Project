# Generated by Django 4.1.2 on 2022-10-21 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "course_name",
                    models.CharField(
                        choices=[
                            ("CompSci", "ComputerScience"),
                            ("Math-course1", "Maths 101"),
                            ("WebDev", "Website Development"),
                            ("AI", "Intro to AI"),
                            ("FOML", "Fundamentals of Machine Learning"),
                            ("DBMS", "Database Managment Services"),
                        ],
                        default="default_course",
                        max_length=100,
                    ),
                ),
                ("description", models.CharField(max_length=400)),
                ("resource_link", models.CharField(max_length=50)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"verbose_name_plural": "Courses",},
        ),
    ]