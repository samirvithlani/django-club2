# Generated by Django 4.2.2 on 2023-06-14 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='choice',
            field=models.CharField(choices=[('1', 'Active'), ('0', 'Inactive')], max_length=20, null=True),
        ),
    ]
