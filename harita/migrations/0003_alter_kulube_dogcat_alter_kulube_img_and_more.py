# Generated by Django 4.0.3 on 2022-04-29 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harita', '0002_alter_person_options_rename_acıklama_kulube_aciklama_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kulube',
            name='dogcat',
            field=models.CharField(default='Kedi', max_length=20),
        ),
        migrations.AlterField(
            model_name='kulube',
            name='img',
            field=models.CharField(default='1.jpeg', max_length=100),
        ),
        migrations.AlterField(
            model_name='kulube',
            name='sayac',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='beslemesayisi',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='person',
            name='bildirmesayisi',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='person',
            name='mamakilo',
            field=models.IntegerField(default=0),
        ),
    ]