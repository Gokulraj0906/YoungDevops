# Generated by Django 5.0.3 on 2024-04-02 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('organization', models.TextField()),
                ('option', models.CharField(choices=[('Software service', 'Software service'), ('Business Intelligence', 'Business Intelligence'), ('Application Maintenance And Support', 'Application Maintenance And Support')], max_length=255)),
            ],
        ),
    ]
