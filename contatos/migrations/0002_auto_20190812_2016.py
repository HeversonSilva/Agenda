# Generated by Django 2.2.4 on 2019-08-12 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='listado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='contato',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contatos.Categoria'),
        ),
    ]
