# Generated by Django 4.1.7 on 2023-02-28 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_insta_loguser'),
    ]

    operations = [
        migrations.AddField(
            model_name='insta',
            name='accound',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='insta',
            name='answer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='insta',
            name='question',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
