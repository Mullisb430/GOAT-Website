# Generated by Django 4.0.5 on 2022-06-26 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='answer_four',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='questions',
            name='answer_one',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='questions',
            name='answer_three',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='questions',
            name='answer_two',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question',
            field=models.TextField(max_length=250),
        ),
    ]