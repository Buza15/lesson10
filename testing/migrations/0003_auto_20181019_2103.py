# Generated by Django 2.1 on 2018-10-19 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0002_auto_20181019_1958'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='test',
            options={'verbose_name': 'Test', 'verbose_name_plural': 'Test'},
        ),
        migrations.AddField(
            model_name='test',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='name',
            field=models.CharField(max_length=255, verbose_name='new name'),
        ),
    ]
