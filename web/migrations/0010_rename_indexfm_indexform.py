# Generated by Django 4.2.7 on 2023-11-20 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_rename_contactfm_indexfm_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Indexfm',
            new_name='Indexform',
        ),
    ]