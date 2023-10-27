# Generated by Django 3.2.6 on 2023-10-13 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_com_app', '0003_auto_20231013_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.CharField(default='', max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
