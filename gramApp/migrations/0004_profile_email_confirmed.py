# Generated by Django 2.2 on 2019-10-16 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gramApp', '0003_image_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
