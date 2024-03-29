# Generated by Django 2.2.6 on 2019-10-19 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20191019_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
        migrations.AddField(
            model_name='question',
            name='poll',
            field=models.TextField(default='poll_text', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
    ]
