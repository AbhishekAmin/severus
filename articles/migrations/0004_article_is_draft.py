# Generated by Django 2.2.4 on 2019-08-13 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_draft',
            field=models.BooleanField(default=True),
        ),
    ]
