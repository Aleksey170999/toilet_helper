# Generated by Django 4.0.4 on 2022-05-03 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toilet_posts', '0013_toilet_img_alter_toilet_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toilet',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
