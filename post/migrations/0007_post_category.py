# Generated by Django 4.2.3 on 2023-07-23 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_alter_post_email_alter_post_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Web Development', 'WB'), ('Desktop Development', 'DB')], default='WB', max_length=20),
            preserve_default=False,
        ),
    ]