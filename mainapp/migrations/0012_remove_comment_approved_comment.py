# Generated by Django 4.1.4 on 2023-04-10 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_comment_delete_productfeedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved_comment',
        ),
    ]