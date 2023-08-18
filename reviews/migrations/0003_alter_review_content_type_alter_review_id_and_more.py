# Generated by Django 4.2.3 on 2023-08-01 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0002_review_model_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_type_set_for_%(class)s', to='contenttypes.contenttype', verbose_name='content type'),
        ),
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_comments', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]