# Generated by Django 5.1.2 on 2024-10-18 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients_App', '0002_rename_name_client_client_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=20, null=True),
        ),
    ]
