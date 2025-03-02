# Generated by Django 5.0.3 on 2024-04-06 12:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_image'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='allproducts', to='categories.category'),
        ),
    ]
