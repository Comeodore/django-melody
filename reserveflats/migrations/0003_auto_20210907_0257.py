# Generated by Django 3.2.7 on 2021-09-06 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserveflats', '0002_auto_20210905_1501'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reserveflats',
            options={'ordering': ['id'], 'verbose_name': 'квартиру', 'verbose_name_plural': 'квартиры'},
        ),
        migrations.AddField(
            model_name='reserveflats',
            name='floor',
            field=models.IntegerField(default=1, verbose_name='Этаж'),
            preserve_default=False,
        ),
    ]
