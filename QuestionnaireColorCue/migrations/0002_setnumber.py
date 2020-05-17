# Generated by Django 2.0.2 on 2020-05-17 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionnaireColorCue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SetNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_num', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('user', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='QuestionnaireColorCue.UserDetails')),
            ],
            options={
                'verbose_name_plural': 'Set Number',
            },
        ),
    ]
