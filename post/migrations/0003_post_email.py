# Generated by Django 4.2.3 on 2023-07-23 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.EmailField(default='test@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]
