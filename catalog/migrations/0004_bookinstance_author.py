# Generated by Django 5.0 on 2023-12-20 11:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_bookinstance_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.author'),
        ),
    ]
