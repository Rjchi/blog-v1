# Generated by Django 3.2.16 on 2023-02-17 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_description_post_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='excerpt',
            new_name='description',
        ),
    ]
