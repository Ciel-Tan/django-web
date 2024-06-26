# Generated by Django 5.0.4 on 2024-05-21 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    def update_order_detail_prices(apps, schema_editor):
        OrderDetail = apps.get_model('app', 'OrderDetail')
        for order_detail in OrderDetail.objects.all():
            order_detail.price = order_detail.product.price * order_detail.quantity
            order_detail.save()

    dependencies = [
        ('app', '0002_alter_product_price'),
    ]

    operations = [
        migrations.RunPython(update_order_detail_prices),
        migrations.AlterField(
            model_name='orderdetail',
            name='price',
            field=models.IntegerField(),
        ),
    ]
