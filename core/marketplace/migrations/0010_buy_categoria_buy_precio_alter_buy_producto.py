# Generated by Django 4.2 on 2023-05-21 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0009_buy'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchases_as_category', to='marketplace.product'),
        ),
        migrations.AddField(
            model_name='buy',
            name='precio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchases_as_price', to='marketplace.product'),
        ),
        migrations.AlterField(
            model_name='buy',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='marketplace.product'),
        ),
    ]
