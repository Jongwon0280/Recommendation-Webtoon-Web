# Generated by Django 4.2 on 2023-04-24 20:51

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_post_hook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
