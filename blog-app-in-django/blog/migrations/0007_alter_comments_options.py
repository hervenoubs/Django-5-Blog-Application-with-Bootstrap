# Generated by Django 4.2.9 on 2024-01-10 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comments_visitor_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['created_on']},
        ),
    ]
