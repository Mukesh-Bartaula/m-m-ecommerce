# Generated by Django 4.2.1 on 2023-07-04 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='../static/image/default_img.png', upload_to='static/products_img/'),
        ),
    ]
