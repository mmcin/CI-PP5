# Generated by Django 4.1.1 on 2022-11-30 09:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_productreviews'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductReviews',
            new_name='ProductReview',
        ),
    ]