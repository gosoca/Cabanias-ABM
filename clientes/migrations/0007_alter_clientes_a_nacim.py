# Generated by Django 4.2 on 2023-07-27 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_alter_clientes_a_nacim_alter_clientes_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='A_nacim',
            field=models.DateField(null=True),
        ),
    ]
