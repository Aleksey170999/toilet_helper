# Generated by Django 4.0.4 on 2022-05-03 15:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toilet_posts', '0014_alter_toilet_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='toilet',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 3, 15, 11, 38, 73803), null=True),
        ),
        migrations.CreateModel(
            name='ToiletPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, upload_to='images/gallery')),
                ('toilet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toilet_posts.toilet')),
            ],
        ),
    ]
