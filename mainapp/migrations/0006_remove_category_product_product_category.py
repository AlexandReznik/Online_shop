# Generated by Django 4.1.4 on 2023-03-28 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.category'),
        ),
    ]
