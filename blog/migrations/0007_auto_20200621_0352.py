# Generated by Django 2.2.13 on 2020-06-21 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_cv_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv',
            name='author',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='id',
        ),
        migrations.AlterField(
            model_name='cv',
            name='title',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]