# Generated by Django 4.2.4 on 2024-01-24 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_remove_project_date_remove_project_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecttranslation',
            name='image',
            field=models.ImageField(blank=True, upload_to='portfolio/images/'),
        ),
    ]
