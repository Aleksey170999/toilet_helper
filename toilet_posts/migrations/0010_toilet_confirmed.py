# Generated by Django 4.0.4 on 2022-04-28 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toilet_posts', '0009_toilet_user_tg_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='toilet',
            name='confirmed',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
