# Generated by Django 4.0.6 on 2022-08-17 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_postcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='text',
            field=models.TextField(),
        ),
    ]
