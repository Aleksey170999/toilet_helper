# Generated by Django 4.0.4 on 2022-04-27 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toilet_posts', '0002_toilet_delete_toiletmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toilet',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='toilet_posts.author'),
        ),
    ]
