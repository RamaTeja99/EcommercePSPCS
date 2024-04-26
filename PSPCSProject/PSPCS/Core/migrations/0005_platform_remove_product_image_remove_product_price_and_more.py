# Generated by Django 5.0 on 2024-04-26 10:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0004_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.CreateModel(
            name='ProductPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/product_images/')),
                ('link', models.URLField(blank=True)),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.platform')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.product')),
            ],
        ),
    ]