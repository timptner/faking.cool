# Generated by Django 3.1.1 on 2020-10-13 19:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoring', '0002_mentee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentee',
            name='email',
        ),
        migrations.AddField(
            model_name='mentor',
            name='nick',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='color',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Die Farben sind nur als Hexadezimal-Code erlaubt.', regex='^#[0-9A-F]{6}$')]),
        ),
        migrations.AlterField(
            model_name='mentee',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='mentee',
            name='phone',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message="Die Mobilnummer ist nur im Format '+49123456789' erlaubt.", regex='^\\+[1-9]{1}[0-9]{3,14}$')]),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='phone',
            field=models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator(message="Die Mobilnummer ist nur im Format '+49123456789' erlaubt.", regex='^\\+[1-9]{1}[0-9]{3,14}$')]),
        ),
    ]
