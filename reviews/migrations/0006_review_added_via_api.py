# Generated by Django 4.2.3 on 2023-08-18 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_alter_review_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='added_via_api',
            field=models.BooleanField(default=False),
        ),
    ]