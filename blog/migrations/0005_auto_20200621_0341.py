# Generated by Django 2.2.13 on 2020-06-21 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200621_0335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cv',
            old_name='num',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='cv',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='cv',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
