# Generated by Django 5.1.4 on 2025-01-04 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente_id', models.IntegerField()),
                ('importe', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pagada', models.BooleanField(default=False)),
            ],
        ),
    ]
