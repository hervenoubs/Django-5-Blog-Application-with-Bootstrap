# Generated by Django 4.2.9 on 2024-01-09 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_post_id_comments_post_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_intro',
        ),
    ]
