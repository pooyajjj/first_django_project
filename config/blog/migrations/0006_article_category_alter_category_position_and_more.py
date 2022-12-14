# Generated by Django 4.0.6 on 2022-09-06 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(to='blog.category', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='position',
            field=models.IntegerField(verbose_name='position'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='category addres'),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=True, verbose_name='show'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=200, verbose_name='category name'),
        ),
    ]
