# Generated by Django 5.0 on 2024-07-14 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payrollApp', '0007_alter_employee_empcountry_alter_employee_empdept'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartTimeEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=60)),
                ('lastName', models.CharField(max_length=60)),
                ('titleName', models.CharField(max_length=60)),
            ],
        ),
    ]
