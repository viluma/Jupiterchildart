# Generated by Django 3.0 on 2020-03-13 17:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20200215_1738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postview',
            old_name='POST',
            new_name='post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='coment_cout',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
