# Generated by Django 4.1.7 on 2023-03-11 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0007_product_digital'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
