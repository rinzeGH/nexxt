# Generated by Django 4.0.2 on 2022-03-14 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_profile_views_profileviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='vk_url',
            field=models.CharField(default='None', max_length=50, verbose_name='Ссылка ВК'),
        ),
    ]