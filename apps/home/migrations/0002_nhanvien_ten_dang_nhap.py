# Generated by Django 3.2.16 on 2024-11-01 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nhanvien',
            name='ten_dang_nhap',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
