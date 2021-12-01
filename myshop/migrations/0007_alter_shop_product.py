# Generated by Django 3.2.9 on 2021-11-17 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0006_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='product',
            field=models.ManyToManyField(blank=True, null=True, related_name='shops', to='myshop.Product', verbose_name='Product'),
        ),
    ]
