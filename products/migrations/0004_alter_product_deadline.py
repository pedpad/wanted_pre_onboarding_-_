# Generated by Django 4.0.3 on 2022-04-13 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='deadline',
            field=models.DateField(),
        ),
    ]
