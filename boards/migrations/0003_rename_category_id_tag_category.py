# Generated by Django 3.2.2 on 2021-10-23 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_alter_board_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='category_id',
            new_name='category',
        ),
    ]