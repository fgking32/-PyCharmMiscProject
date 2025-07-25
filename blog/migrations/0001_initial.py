# Generated by Django 4.1 on 2025-07-07 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='文章标题')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '博客文章',
                'verbose_name_plural': '博客文章',
                'ordering': ['-created_time'],
            },
        ),
    ]
