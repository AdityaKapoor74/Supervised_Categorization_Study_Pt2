# Generated by Django 2.0.2 on 2020-07-09 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Questionnaire', '0005_userdetails_set_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setnumber',
            name='user',
        ),
        migrations.DeleteModel(
            name='SetNumber',
        ),
    ]