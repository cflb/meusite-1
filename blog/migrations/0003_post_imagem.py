# Generated by Django 3.0.4 on 2020-03-04 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200304_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagem',
            field=models.ImageField(default=1, upload_to='imagens', verbose_name='Imagem'),
            preserve_default=False,
        ),
    ]
