# Generated by Django 5.0.3 on 2024-04-04 17:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(default='User', max_length=80)),
                ('member_type', models.CharField(default='Team Member', max_length=50)),
                ('member_phone', models.CharField(default=None, max_length=10)),
                ('member_instagram_link', models.CharField(default='https://www.instagram.com/', max_length=200)),
                ('member_linkedin_link', models.CharField(default='https://www.linkedin.com/feed/', max_length=200)),
                ('member_facebook_link', models.CharField(default='https://www.facebook.com/home.php', max_length=200)),
                ('member_twitter_link', models.CharField(default='https://twitter.com/home', max_length=200)),
                ('join_date', models.DateField(verbose_name=datetime.datetime(2024, 4, 4, 17, 45, 29, 887995, tzinfo=datetime.timezone.utc))),
                ('update_date', models.DateField(verbose_name=datetime.datetime(2024, 4, 4, 17, 45, 29, 887995, tzinfo=datetime.timezone.utc))),
                ('image', models.ImageField(default='default.jpg', upload_to='member/images')),
            ],
        ),
    ]