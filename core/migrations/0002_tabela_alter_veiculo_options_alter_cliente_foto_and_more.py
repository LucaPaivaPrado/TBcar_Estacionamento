# Generated by Django 4.1.7 on 2023-04-14 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tabela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
            ],
            options={
                'verbose_name_plural': 'Tabelas',
            },
        ),
        migrations.AlterModelOptions(
            name='veiculo',
            options={'verbose_name_plural': 'Veículos'},
        ),
        migrations.AlterField(
            model_name='cliente',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='cliente_foto', verbose_name=' '),
        ),
        migrations.AlterField(
            model_name='marca',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Marca'),
        ),
    ]
