# Generated by Django 5.0 on 2024-03-16 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminside', '0003_alter_order_tracking_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='tracking_number',
            field=models.CharField(default='EXWA69608c42-d67e-4881-ORDER', max_length=30, unique=True),
        ),
    ]
