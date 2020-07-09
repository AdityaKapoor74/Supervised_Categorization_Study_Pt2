# Generated by Django 2.0.2 on 2020-07-09 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Questionnaire', '0002_common_features_test_set1_common_features_test_set2_common_features_test_set3_common_features_test_s'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserResponsesForDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('set_number', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('user_id', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='Questionnaire.UserDetails')),
            ],
            options={
                'verbose_name_plural': 'User Responses for Description',
            },
        ),
    ]