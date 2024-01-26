# Generated by Django 4.2.3 on 2023-07-23 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('WB', 'Web Development'), ('DB', 'Desktop Development'), ('DS', 'Data Science')], max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]