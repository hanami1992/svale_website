# Generated by Django 3.2.9 on 2021-12-13 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20211203_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsmodeltranslation',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='image/prod_model/20211213095433/'),
        ),
        migrations.AlterField(
            model_name='productsimagemodel',
            name='pictures',
            field=models.ImageField(blank=True, null=True, upload_to='image/20211213095433/'),
        ),
        migrations.AlterField(
            model_name='productsmodeltranslation',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='file/20211213095433'),
        ),
    ]