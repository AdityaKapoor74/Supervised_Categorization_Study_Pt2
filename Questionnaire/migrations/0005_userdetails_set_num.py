# Generated by Django 2.0.2 on 2020-07-09 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Questionnaire', '0004_auto_20200709_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='set_num',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
    ]