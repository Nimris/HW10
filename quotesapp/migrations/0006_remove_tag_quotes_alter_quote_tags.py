# Generated by Django 5.1.2 on 2024-10-27 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotesapp', '0005_alter_quote_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='quotes',
        ),
        migrations.AlterField(
            model_name='quote',
            name='tags',
            field=models.ManyToManyField(related_name='quotes', to='quotesapp.tag'),
        ),
    ]
