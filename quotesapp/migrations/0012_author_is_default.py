# Generated by Django 5.1.2 on 2024-10-29 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotesapp', '0011_remove_tag_quotes_alter_quote_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='is_default',
            field=models.BooleanField(default=False),
        ),
    ]
