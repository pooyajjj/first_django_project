# Generated by Django 4.0.6 on 2022-09-06 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_delete_posts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('status', models.BooleanField(default=True)),
                ('position', models.IntegerField()),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categorys',
                'ordering': ['position'],
            },
        ),
    ]
