# Generated by Django 2.1 on 2018-10-15 16:35

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import library.models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_testfield'),
    ]

    operations = [
        migrations.AddField(
            model_name='testfield',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='testfield',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='testfield',
            name='array_field',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='testfield',
            name='big_int_field',
            field=models.BigIntegerField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='testfield',
            name='boolean_field',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='testfield',
            name='char_field',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='testfield',
            name='date_field',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='testfield',
            name='datetime_field',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='testfield',
            name='float_field',
            field=models.FloatField(blank=True, default=1.0, help_text='help text', null=True, verbose_name='My float name'),
        ),
        migrations.AlterField(
            model_name='testfield',
            name='json_field',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='testfield',
            name='positive_field',
            field=models.PositiveIntegerField(db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='testfield',
            name='positive_small_int_field',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='testfield',
            name='slug_field',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='testfield',
            name='small_int_field',
            field=models.SmallIntegerField(default=library.models.random_1_1000, null=True),
        ),
        migrations.AlterField(
            model_name='testfield',
            name='text_field',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='testfield',
            name='time_field',
            field=models.TimeField(null=True),
        ),
    ]
