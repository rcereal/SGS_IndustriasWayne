# Generated by Django 5.1.3 on 2024-11-20 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_de_seguranca', '0006_alter_profile_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='cargo',
            new_name='cargo_choices',
        ),
    ]
