# Generated by Django 2.2.4 on 2019-08-13 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0002_auto_20190812_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='foto',
            field=models.ImageField(blank=True, upload_to='pictures/%y/%m/%d'),
        ),
    ]