# Generated by Django 3.2.23 on 2023-11-23 18:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mood_tracker', '0005_auto_20231122_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievements',
            name='achievement_user',
            field=models.ManyToManyField(blank=True, related_name='achievements', to=settings.AUTH_USER_MODEL),
        ),
    ]
