# Generated by Django 3.2.9 on 2022-01-26 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20220126_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsimagemodel',
            name='pictures',
            field=models.ImageField(blank=True, null=True, upload_to='image/20220126104453/'),
        ),
        migrations.AlterField(
            model_name='productsmodeltranslation',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='file/20220126104453'),
        ),
        migrations.AlterField(
            model_name='productsmodeltranslation',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='image/prod_model/20220126104453/'),
        ),
    ]