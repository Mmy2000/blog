# Generated by Django 4.2.3 on 2023-07-23 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('WB', 'Web Development'), ('DB', 'Desktop Development')], max_length=20),
        ),
    ]