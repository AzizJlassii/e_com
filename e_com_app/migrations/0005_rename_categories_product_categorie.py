# Generated by Django 3.2.6 on 2023-10-13 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e_com_app', '0004_auto_20231013_1722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categories',
            new_name='categorie',
        ),
    ]
