# Generated by Django 4.1.6 on 2023-02-13 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PreApp', '0006_alter_datos_compra_fecha'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datos_compra',
            old_name='metodo_pago',
            new_name='formapago',
        ),
    ]
