# Generated by Django 5.0.3 on 2024-04-08 18:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depart', '0002_rename_member_instagram_link_member_member_instagram_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_date', models.DateField(verbose_name=datetime.datetime(2024, 4, 8, 18, 23, 29, 262255, tzinfo=datetime.timezone.utc))),
                ('update_date', models.DateField(verbose_name=datetime.datetime(2024, 4, 8, 18, 23, 29, 262255, tzinfo=datetime.timezone.utc))),
                ('image', models.ImageField(default='default.jpg', upload_to='Hero/images')),
            ],
        ),
        migrations.AlterField(
            model_name='member',
            name='join_date',
            field=models.DateField(verbose_name=datetime.datetime(2024, 4, 8, 18, 23, 29, 262255, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='update_date',
            field=models.DateField(verbose_name=datetime.datetime(2024, 4, 8, 18, 23, 29, 262255, tzinfo=datetime.timezone.utc)),
        ),
    ]
