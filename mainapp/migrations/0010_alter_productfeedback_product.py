# Generated by Django 4.1.4 on 2023-04-10 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_productfeedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productfeedback',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product', verbose_name='Product'),
        ),
    ]
