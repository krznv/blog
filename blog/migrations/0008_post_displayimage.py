# Generated by Django 2.2.8 on 2020-10-31 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='displayImage',
            field=models.BooleanField(default=False),
        ),
    ]
