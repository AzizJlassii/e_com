# Generated by Django 3.2.6 on 2023-10-13 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_com_app', '0002_auto_20231010_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='products', to='e_com_app.Category'),
        ),
    ]
