# Generated by Django 4.1.7 on 2023-04-28 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rotativo_mensalista'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='tabela',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Tabela'),
        ),
    ]
