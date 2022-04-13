# Generated by Django 4.0.3 on 2022-04-13 05:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sponsors',
            field=models.ManyToManyField(through='products.Sponsor', to=settings.AUTH_USER_MODEL),
        ),
    ]