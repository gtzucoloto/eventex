# Generated by Django 3.1.3 on 2020-11-16 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_talk'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='talk',
            options={'verbose_name': 'palestra', 'verbose_name_plural': 'palestras'},
        ),
        migrations.AlterField(
            model_name='talk',
            name='description',
            field=models.TextField(blank=True, verbose_name='descrição'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='speakers',
            field=models.ManyToManyField(blank=True, to='core.Speaker', verbose_name='palestrantes'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='start',
            field=models.TimeField(blank=True, null=True, verbose_name='início'),
        ),
    ]