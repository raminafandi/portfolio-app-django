# Generated by Django 2.1.7 on 2019-02-16 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190214_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
