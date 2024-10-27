# Generated by Django 5.1.2 on 2024-10-25 10:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotesapp', '0004_alter_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to='quotesapp.author'),
        ),
    ]