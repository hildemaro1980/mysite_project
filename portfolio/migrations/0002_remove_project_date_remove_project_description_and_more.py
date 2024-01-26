# Generated by Django 4.2.4 on 2024-01-24 12:28

import datetime
from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.RemoveField(
            model_name='project',
            name='title',
        ),
        migrations.RemoveField(
            model_name='project',
            name='url',
        ),
        migrations.CreateModel(
            name='ProjectTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='portfolio/images/')),
                ('url', models.URLField(blank=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='portfolio.project')),
            ],
            options={
                'verbose_name': 'project Translation',
                'db_table': 'portfolio_project_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
    ]
