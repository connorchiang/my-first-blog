# Generated by Django 2.2.13 on 2020-06-21 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200621_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='num',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
