# Generated by Django 5.2.4 on 2025-07-16 16:09

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
                ('employee_name', models.CharField(max_length=128)),
                ('company_name', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=50)),
                ('org_position', models.CharField(max_length=128)),
                ('interal_phone', models.CharField(max_length=5)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]
