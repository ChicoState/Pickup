# Generated by Django 4.2.16 on 2024-10-04 18:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Pickup', '0002_alter_post_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_title',
            field=models.CharField(default='tengo', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='rsvp_list',
            field=models.ManyToManyField(related_name='rsvp', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_loc',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=models.CharField(max_length=255),
        ),
    ]