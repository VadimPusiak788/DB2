# Generated by Django 3.1.7 on 2021-03-29 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatmodel',
            old_name='author',
            new_name='author_email',
        ),
    ]
