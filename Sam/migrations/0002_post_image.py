# Generated by Django 2.1.5 on 2021-03-17 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='posts_pics'),
        ),
    ]
